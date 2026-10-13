---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient
title: Class DeploymentResourcePoolServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:44.836719+00:00
---

# Class DeploymentResourcePoolServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DeploymentResourcePoolServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/DeploymentResourcePoolServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service that manages the DeploymentResourcePool resource.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeploymentResourcePoolName name =
           DeploymentResourcePoolName.of("[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]");
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.getDeploymentResourcePool(name);
     }
     

Note: close() needs to be called on the DeploymentResourcePoolServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDeploymentResourcePool |  Create a DeploymentResourcePool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDeploymentResourcePoolAsync(LocationName parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId) 
  * createDeploymentResourcePoolAsync(String parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDeploymentResourcePoolOperationCallable() 
  * createDeploymentResourcePoolCallable() 

  
GetDeploymentResourcePool |  Get a DeploymentResourcePool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDeploymentResourcePool(GetDeploymentResourcePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDeploymentResourcePool(DeploymentResourcePoolName name) 
  * getDeploymentResourcePool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDeploymentResourcePoolCallable() 

  
ListDeploymentResourcePools |  List DeploymentResourcePools in a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDeploymentResourcePools(ListDeploymentResourcePoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDeploymentResourcePools(ProjectName parent) 
  * listDeploymentResourcePools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDeploymentResourcePoolsPagedCallable() 
  * listDeploymentResourcePoolsCallable() 

  
UpdateDeploymentResourcePool |  Update a DeploymentResourcePool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDeploymentResourcePoolAsync(DeploymentResourcePool deploymentResourcePool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDeploymentResourcePoolOperationCallable() 
  * updateDeploymentResourcePoolCallable() 

  
DeleteDeploymentResourcePool |  Delete a DeploymentResourcePool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDeploymentResourcePoolAsync(DeploymentResourcePoolName name) 
  * deleteDeploymentResourcePoolAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDeploymentResourcePoolOperationCallable() 
  * deleteDeploymentResourcePoolCallable() 

  
QueryDeployedModels |  List DeployedModels that have been deployed on this DeploymentResourcePool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryDeployedModels(QueryDeployedModelsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryDeployedModels(String deploymentResourcePool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryDeployedModelsPagedCallable() 
  * queryDeployedModelsCallable() 

  
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

This class can be customized by passing in a custom instance of DeploymentResourcePoolServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeploymentResourcePoolServiceSettings deploymentResourcePoolServiceSettings =
         DeploymentResourcePoolServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create(deploymentResourcePoolServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DeploymentResourcePoolServiceSettings deploymentResourcePoolServiceSettings =
         DeploymentResourcePoolServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create(deploymentResourcePoolServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeploymentResourcePoolServiceClient

## Static Methods 

### create()
    
    
    public static final DeploymentResourcePoolServiceClient create()

Constructs an instance of DeploymentResourcePoolServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeploymentResourcePoolServiceSettings settings)
    
    
    public static final DeploymentResourcePoolServiceClient create(DeploymentResourcePoolServiceSettings settings)

Constructs an instance of DeploymentResourcePoolServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeploymentResourcePoolServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DeploymentResourcePoolServiceStub stub)
    
    
    public static final DeploymentResourcePoolServiceClient create(DeploymentResourcePoolServiceStub stub)

Constructs an instance of DeploymentResourcePoolServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DeploymentResourcePoolServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeploymentResourcePoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DeploymentResourcePoolServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient)` |   
  
## Constructors 

### DeploymentResourcePoolServiceClient(DeploymentResourcePoolServiceSettings settings)
    
    
    protected DeploymentResourcePoolServiceClient(DeploymentResourcePoolServiceSettings settings)

Constructs an instance of DeploymentResourcePoolServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DeploymentResourcePoolServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceSettings)`  
  
  
### DeploymentResourcePoolServiceClient(DeploymentResourcePoolServiceStub stub)
    
    
    protected DeploymentResourcePoolServiceClient(DeploymentResourcePoolServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DeploymentResourcePoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DeploymentResourcePoolServiceStub)`  
  
  
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

### createDeploymentResourcePoolAsync(@Nullable LocationName parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId)
    
    
    public final OperationFuture<DeploymentResourcePool,CreateDeploymentResourcePoolOperationMetadata> createDeploymentResourcePoolAsync(@Nullable LocationName parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId)

Create a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       DeploymentResourcePool deploymentResourcePool = DeploymentResourcePool.newBuilder().build();
       String deploymentResourcePoolId = "deploymentResourcePoolId1805697578";
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient
               .createDeploymentResourcePoolAsync(
                   parent, deploymentResourcePool, deploymentResourcePoolId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent location resource where this DeploymentResourcePool will be created. Format: `projects/{project}/locations/{location}`  
`deploymentResourcePool` | `[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)`  
Required. The DeploymentResourcePool to create.  
`deploymentResourcePoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the DeploymentResourcePool, which will become the final component of the DeploymentResourcePool's resource name. The maximum length is 63 characters, and valid characters are `/^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[CreateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolOperationMetadata)>` |   
  
### createDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest request)
    
    
    public final OperationFuture<DeploymentResourcePool,CreateDeploymentResourcePoolOperationMetadata> createDeploymentResourcePoolAsync(CreateDeploymentResourcePoolRequest request)

Create a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       CreateDeploymentResourcePoolRequest request =
           CreateDeploymentResourcePoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setDeploymentResourcePoolId("deploymentResourcePoolId1805697578")
               .build();
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.createDeploymentResourcePoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[CreateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolOperationMetadata)>` |   
  
### createDeploymentResourcePoolAsync(String parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId)
    
    
    public final OperationFuture<DeploymentResourcePool,CreateDeploymentResourcePoolOperationMetadata> createDeploymentResourcePoolAsync(String parent, DeploymentResourcePool deploymentResourcePool, String deploymentResourcePoolId)

Create a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       DeploymentResourcePool deploymentResourcePool = DeploymentResourcePool.newBuilder().build();
       String deploymentResourcePoolId = "deploymentResourcePoolId1805697578";
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient
               .createDeploymentResourcePoolAsync(
                   parent, deploymentResourcePool, deploymentResourcePoolId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent location resource where this DeploymentResourcePool will be created. Format: `projects/{project}/locations/{location}`  
`deploymentResourcePool` | `[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)`  
Required. The DeploymentResourcePool to create.  
`deploymentResourcePoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the DeploymentResourcePool, which will become the final component of the DeploymentResourcePool's resource name. The maximum length is 63 characters, and valid characters are `/^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[CreateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolOperationMetadata)>` |   
  
### createDeploymentResourcePoolCallable()
    
    
    public final UnaryCallable<CreateDeploymentResourcePoolRequest,Operation> createDeploymentResourcePoolCallable()

Create a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       CreateDeploymentResourcePoolRequest request =
           CreateDeploymentResourcePoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setDeploymentResourcePoolId("deploymentResourcePoolId1805697578")
               .build();
       ApiFuture<Operation> future =
           deploymentResourcePoolServiceClient
               .createDeploymentResourcePoolCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDeploymentResourcePoolOperationCallable()
    
    
    public final OperationCallable<CreateDeploymentResourcePoolRequest,DeploymentResourcePool,CreateDeploymentResourcePoolOperationMetadata> createDeploymentResourcePoolOperationCallable()

Create a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       CreateDeploymentResourcePoolRequest request =
           CreateDeploymentResourcePoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setDeploymentResourcePoolId("deploymentResourcePoolId1805697578")
               .build();
       OperationFuture<DeploymentResourcePool, CreateDeploymentResourcePoolOperationMetadata>
           future =
               deploymentResourcePoolServiceClient
                   .createDeploymentResourcePoolOperationCallable()
                   .futureCall(request);
       // Do something.
       DeploymentResourcePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolRequest),[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[CreateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDeploymentResourcePoolOperationMetadata)>` |   
  
### deleteDeploymentResourcePoolAsync(@Nullable DeploymentResourcePoolName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDeploymentResourcePoolAsync(@Nullable DeploymentResourcePoolName name)

Delete a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeploymentResourcePoolName name =
           DeploymentResourcePoolName.of("[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]");
       deploymentResourcePoolServiceClient.deleteDeploymentResourcePoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DeploymentResourcePoolName`  
Required. The name of the DeploymentResourcePool to delete. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDeploymentResourcePoolAsync(DeleteDeploymentResourcePoolRequest request)

Delete a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeleteDeploymentResourcePoolRequest request =
           DeleteDeploymentResourcePoolRequest.newBuilder()
               .setName(
                   DeploymentResourcePoolName.of(
                           "[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
                       .toString())
               .build();
       deploymentResourcePoolServiceClient.deleteDeploymentResourcePoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDeploymentResourcePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDeploymentResourcePoolAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteDeploymentResourcePoolAsync(String name)

Delete a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       String name =
           DeploymentResourcePoolName.of("[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
               .toString();
       deploymentResourcePoolServiceClient.deleteDeploymentResourcePoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DeploymentResourcePool to delete. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteDeploymentResourcePoolCallable()
    
    
    public final UnaryCallable<DeleteDeploymentResourcePoolRequest,Operation> deleteDeploymentResourcePoolCallable()

Delete a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeleteDeploymentResourcePoolRequest request =
           DeleteDeploymentResourcePoolRequest.newBuilder()
               .setName(
                   DeploymentResourcePoolName.of(
                           "[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           deploymentResourcePoolServiceClient
               .deleteDeploymentResourcePoolCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDeploymentResourcePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDeploymentResourcePoolOperationCallable()
    
    
    public final OperationCallable<DeleteDeploymentResourcePoolRequest,Empty,DeleteOperationMetadata> deleteDeploymentResourcePoolOperationCallable()

Delete a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeleteDeploymentResourcePoolRequest request =
           DeleteDeploymentResourcePoolRequest.newBuilder()
               .setName(
                   DeploymentResourcePoolName.of(
                           "[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           deploymentResourcePoolServiceClient
               .deleteDeploymentResourcePoolOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDeploymentResourcePoolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getDeploymentResourcePool(@Nullable DeploymentResourcePoolName name)
    
    
    public final DeploymentResourcePool getDeploymentResourcePool(@Nullable DeploymentResourcePoolName name)

Get a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeploymentResourcePoolName name =
           DeploymentResourcePoolName.of("[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]");
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.getDeploymentResourcePool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DeploymentResourcePoolName`  
Required. The name of the DeploymentResourcePool to retrieve. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)` |   
  
### getDeploymentResourcePool(GetDeploymentResourcePoolRequest request)
    
    
    public final DeploymentResourcePool getDeploymentResourcePool(GetDeploymentResourcePoolRequest request)

Get a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetDeploymentResourcePoolRequest request =
           GetDeploymentResourcePoolRequest.newBuilder()
               .setName(
                   DeploymentResourcePoolName.of(
                           "[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
                       .toString())
               .build();
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.getDeploymentResourcePool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDeploymentResourcePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)` |   
  
### getDeploymentResourcePool(String name)
    
    
    public final DeploymentResourcePool getDeploymentResourcePool(String name)

Get a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       String name =
           DeploymentResourcePoolName.of("[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
               .toString();
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.getDeploymentResourcePool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DeploymentResourcePool to retrieve. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)` |   
  
### getDeploymentResourcePoolCallable()
    
    
    public final UnaryCallable<GetDeploymentResourcePoolRequest,DeploymentResourcePool> getDeploymentResourcePoolCallable()

Get a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetDeploymentResourcePoolRequest request =
           GetDeploymentResourcePoolRequest.newBuilder()
               .setName(
                   DeploymentResourcePoolName.of(
                           "[PROJECT]", "[LOCATION]", "[DEPLOYMENT_RESOURCE_POOL]")
                       .toString())
               .build();
       ApiFuture<DeploymentResourcePool> future =
           deploymentResourcePoolServiceClient
               .getDeploymentResourcePoolCallable()
               .futureCall(request);
       // Do something.
       DeploymentResourcePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDeploymentResourcePoolRequest),[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = deploymentResourcePoolServiceClient.getIamPolicy(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           deploymentResourcePoolServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = deploymentResourcePoolServiceClient.getLocation(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           deploymentResourcePoolServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DeploymentResourcePoolServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceSettings` |   
  
### getStub()
    
    
    public DeploymentResourcePoolServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.DeploymentResourcePoolServiceStub)` |   
  
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
  
### listDeploymentResourcePools(@Nullable ProjectName parent)
    
    
    public final DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse listDeploymentResourcePools(@Nullable ProjectName parent)

List DeploymentResourcePools in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (DeploymentResourcePool element :
           deploymentResourcePoolServiceClient.listDeploymentResourcePools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ProjectName`  
Required. The parent Location which owns this collection of DeploymentResourcePools. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse)` |   
  
### listDeploymentResourcePools(ListDeploymentResourcePoolsRequest request)
    
    
    public final DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse listDeploymentResourcePools(ListDeploymentResourcePoolsRequest request)

List DeploymentResourcePools in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListDeploymentResourcePoolsRequest request =
           ListDeploymentResourcePoolsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DeploymentResourcePool element :
           deploymentResourcePoolServiceClient.listDeploymentResourcePools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDeploymentResourcePoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse)` |   
  
### listDeploymentResourcePools(String parent)
    
    
    public final DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse listDeploymentResourcePools(String parent)

List DeploymentResourcePools in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (DeploymentResourcePool element :
           deploymentResourcePoolServiceClient.listDeploymentResourcePools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent Location which owns this collection of DeploymentResourcePools. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse)` |   
  
### listDeploymentResourcePoolsCallable()
    
    
    public final UnaryCallable<ListDeploymentResourcePoolsRequest,ListDeploymentResourcePoolsResponse> listDeploymentResourcePoolsCallable()

List DeploymentResourcePools in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListDeploymentResourcePoolsRequest request =
           ListDeploymentResourcePoolsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListDeploymentResourcePoolsResponse response =
             deploymentResourcePoolServiceClient.listDeploymentResourcePoolsCallable().call(request);
         for (DeploymentResourcePool element : response.getDeploymentResourcePoolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDeploymentResourcePoolsRequest),[ListDeploymentResourcePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDeploymentResourcePoolsResponse)>` |   
  
### listDeploymentResourcePoolsPagedCallable()
    
    
    public final UnaryCallable<ListDeploymentResourcePoolsRequest,DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse> listDeploymentResourcePoolsPagedCallable()

List DeploymentResourcePools in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListDeploymentResourcePoolsRequest request =
           ListDeploymentResourcePoolsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DeploymentResourcePool> future =
           deploymentResourcePoolServiceClient
               .listDeploymentResourcePoolsPagedCallable()
               .futureCall(request);
       // Do something.
       for (DeploymentResourcePool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDeploymentResourcePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDeploymentResourcePoolsRequest),[ListDeploymentResourcePoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListDeploymentResourcePoolsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DeploymentResourcePoolServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           deploymentResourcePoolServiceClient.listLocations(request).iterateAll()) {
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
`[DeploymentResourcePoolServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             deploymentResourcePoolServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DeploymentResourcePoolServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           deploymentResourcePoolServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.ListLocationsPagedResponse)>` |   
  
### queryDeployedModels(QueryDeployedModelsRequest request)
    
    
    public final DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse queryDeployedModels(QueryDeployedModelsRequest request)

List DeployedModels that have been deployed on this DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       QueryDeployedModelsRequest request =
           QueryDeployedModelsRequest.newBuilder()
               .setDeploymentResourcePool("deploymentResourcePool-1928845137")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DeployedModel element :
           deploymentResourcePoolServiceClient.queryDeployedModels(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryDeployedModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryDeployedModelsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse)` |   
  
### queryDeployedModels(String deploymentResourcePool)
    
    
    public final DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse queryDeployedModels(String deploymentResourcePool)

List DeployedModels that have been deployed on this DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       String deploymentResourcePool = "deploymentResourcePool-1928845137";
       for (DeployedModel element :
           deploymentResourcePoolServiceClient
               .queryDeployedModels(deploymentResourcePool)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`deploymentResourcePool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the target DeploymentResourcePool to query. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse)` |   
  
### queryDeployedModelsCallable()
    
    
    public final UnaryCallable<QueryDeployedModelsRequest,QueryDeployedModelsResponse> queryDeployedModelsCallable()

List DeployedModels that have been deployed on this DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       QueryDeployedModelsRequest request =
           QueryDeployedModelsRequest.newBuilder()
               .setDeploymentResourcePool("deploymentResourcePool-1928845137")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryDeployedModelsResponse response =
             deploymentResourcePoolServiceClient.queryDeployedModelsCallable().call(request);
         for (DeployedModel element : response.getDeployedModelsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDeployedModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryDeployedModelsRequest),[QueryDeployedModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryDeployedModelsResponse)>` |   
  
### queryDeployedModelsPagedCallable()
    
    
    public final UnaryCallable<QueryDeployedModelsRequest,DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse> queryDeployedModelsPagedCallable()

List DeployedModels that have been deployed on this DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       QueryDeployedModelsRequest request =
           QueryDeployedModelsRequest.newBuilder()
               .setDeploymentResourcePool("deploymentResourcePool-1928845137")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DeployedModel> future =
           deploymentResourcePoolServiceClient
               .queryDeployedModelsPagedCallable()
               .futureCall(request);
       // Do something.
       for (DeployedModel element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDeployedModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.QueryDeployedModelsRequest),[QueryDeployedModelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePoolServiceClient.QueryDeployedModelsPagedResponse)>` |   
  
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = deploymentResourcePoolServiceClient.setIamPolicy(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
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
           deploymentResourcePoolServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           deploymentResourcePoolServiceClient.testIamPermissions(request);
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
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           deploymentResourcePoolServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateDeploymentResourcePoolAsync(DeploymentResourcePool deploymentResourcePool, FieldMask updateMask)
    
    
    public final OperationFuture<DeploymentResourcePool,UpdateDeploymentResourcePoolOperationMetadata> updateDeploymentResourcePoolAsync(DeploymentResourcePool deploymentResourcePool, FieldMask updateMask)

Update a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       DeploymentResourcePool deploymentResourcePool = DeploymentResourcePool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient
               .updateDeploymentResourcePoolAsync(deploymentResourcePool, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`deploymentResourcePool` | `[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool)`  
Required. The DeploymentResourcePool to update. The DeploymentResourcePool's `name` field is used to identify the DeploymentResourcePool to update. Format: `projects/{project}/locations/{location}/deploymentResourcePools/{deployment_resource_pool}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[UpdateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolOperationMetadata)>` |   
  
### updateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest request)
    
    
    public final OperationFuture<DeploymentResourcePool,UpdateDeploymentResourcePoolOperationMetadata> updateDeploymentResourcePoolAsync(UpdateDeploymentResourcePoolRequest request)

Update a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       UpdateDeploymentResourcePoolRequest request =
           UpdateDeploymentResourcePoolRequest.newBuilder()
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DeploymentResourcePool response =
           deploymentResourcePoolServiceClient.updateDeploymentResourcePoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[UpdateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolOperationMetadata)>` |   
  
### updateDeploymentResourcePoolCallable()
    
    
    public final UnaryCallable<UpdateDeploymentResourcePoolRequest,Operation> updateDeploymentResourcePoolCallable()

Update a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       UpdateDeploymentResourcePoolRequest request =
           UpdateDeploymentResourcePoolRequest.newBuilder()
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           deploymentResourcePoolServiceClient
               .updateDeploymentResourcePoolCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDeploymentResourcePoolOperationCallable()
    
    
    public final OperationCallable<UpdateDeploymentResourcePoolRequest,DeploymentResourcePool,UpdateDeploymentResourcePoolOperationMetadata> updateDeploymentResourcePoolOperationCallable()

Update a DeploymentResourcePool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DeploymentResourcePoolServiceClient deploymentResourcePoolServiceClient =
         DeploymentResourcePoolServiceClient.create()) {
       UpdateDeploymentResourcePoolRequest request =
           UpdateDeploymentResourcePoolRequest.newBuilder()
               .setDeploymentResourcePool(DeploymentResourcePool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<DeploymentResourcePool, UpdateDeploymentResourcePoolOperationMetadata>
           future =
               deploymentResourcePoolServiceClient
                   .updateDeploymentResourcePoolOperationCallable()
                   .futureCall(request);
       // Do something.
       DeploymentResourcePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDeploymentResourcePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolRequest),[DeploymentResourcePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeploymentResourcePool),[UpdateDeploymentResourcePoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDeploymentResourcePoolOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
