---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient
title: Class EndpointServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:53:47.319730+00:00
---

# Class EndpointServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EndpointServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/EndpointServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing Vertex AI's Endpoints.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName name =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       Endpoint response = endpointServiceClient.getEndpoint(name);
     }
     

Note: close() needs to be called on the EndpointServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateEndpoint |  Creates an Endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEndpointAsync(CreateEndpointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEndpointAsync(LocationName parent, Endpoint endpoint) 
  * createEndpointAsync(String parent, Endpoint endpoint) 
  * createEndpointAsync(LocationName parent, Endpoint endpoint, String endpointId) 
  * createEndpointAsync(String parent, Endpoint endpoint, String endpointId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEndpointOperationCallable() 
  * createEndpointCallable() 

  
GetEndpoint |  Gets an Endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEndpoint(GetEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEndpoint(EndpointName name) 
  * getEndpoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEndpointCallable() 

  
ListEndpoints |  Lists Endpoints in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEndpoints(ListEndpointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEndpoints(LocationName parent) 
  * listEndpoints(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEndpointsPagedCallable() 
  * listEndpointsCallable() 

  
UpdateEndpoint |  Updates an Endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEndpoint(UpdateEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateEndpoint(Endpoint endpoint, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEndpointCallable() 

  
UpdateEndpointLongRunning |  Updates an Endpoint with a long running operation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEndpointLongRunningAsync(UpdateEndpointLongRunningRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEndpointLongRunningAsync(Endpoint endpoint) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEndpointLongRunningOperationCallable() 
  * updateEndpointLongRunningCallable() 

  
DeleteEndpoint |  Deletes an Endpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEndpointAsync(DeleteEndpointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEndpointAsync(EndpointName name) 
  * deleteEndpointAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEndpointOperationCallable() 
  * deleteEndpointCallable() 

  
DeployModel |  Deploys a Model into this Endpoint, creating a DeployedModel within it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployModelAsync(DeployModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deployModelAsync(EndpointName endpoint, DeployedModel deployedModel, Map<String, Integer> trafficSplit) 
  * deployModelAsync(String endpoint, DeployedModel deployedModel, Map<String, Integer> trafficSplit) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployModelOperationCallable() 
  * deployModelCallable() 

  
UndeployModel |  Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeployModelAsync(UndeployModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeployModelAsync(EndpointName endpoint, String deployedModelId, Map<String, Integer> trafficSplit) 
  * undeployModelAsync(String endpoint, String deployedModelId, Map<String, Integer> trafficSplit) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeployModelOperationCallable() 
  * undeployModelCallable() 

  
MutateDeployedModel |  Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * mutateDeployedModelAsync(MutateDeployedModelRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * mutateDeployedModelAsync(EndpointName endpoint, DeployedModel deployedModel, FieldMask updateMask) 
  * mutateDeployedModelAsync(String endpoint, DeployedModel deployedModel, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * mutateDeployedModelOperationCallable() 
  * mutateDeployedModelCallable() 

  
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

This class can be customized by passing in a custom instance of EndpointServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EndpointServiceSettings endpointServiceSettings =
         EndpointServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     EndpointServiceClient endpointServiceClient =
         EndpointServiceClient.create(endpointServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EndpointServiceSettings endpointServiceSettings =
         EndpointServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     EndpointServiceClient endpointServiceClient =
         EndpointServiceClient.create(endpointServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > EndpointServiceClient

## Static Methods 

### create()
    
    
    public static final EndpointServiceClient create()

Constructs an instance of EndpointServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EndpointServiceSettings settings)
    
    
    public static final EndpointServiceClient create(EndpointServiceSettings settings)

Constructs an instance of EndpointServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(EndpointServiceStub stub)
    
    
    public static final EndpointServiceClient create(EndpointServiceStub stub)

Constructs an instance of EndpointServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(EndpointServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.EndpointServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient)` |   
  
## Constructors 

### EndpointServiceClient(EndpointServiceSettings settings)
    
    
    protected EndpointServiceClient(EndpointServiceSettings settings)

Constructs an instance of EndpointServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[EndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceSettings)`  
  
  
### EndpointServiceClient(EndpointServiceStub stub)
    
    
    protected EndpointServiceClient(EndpointServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.EndpointServiceStub)`  
  
  
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

### createEndpointAsync(@Nullable LocationName parent, Endpoint endpoint)
    
    
    public final OperationFuture<Endpoint,CreateEndpointOperationMetadata> createEndpointAsync(@Nullable LocationName parent, Endpoint endpoint)

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Endpoint endpoint = Endpoint.newBuilder().build();
       Endpoint response = endpointServiceClient.createEndpointAsync(parent, endpoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the Endpoint in. Format: `projects/{project}/locations/{location}`  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### createEndpointAsync(@Nullable LocationName parent, Endpoint endpoint, String endpointId)
    
    
    public final OperationFuture<Endpoint,CreateEndpointOperationMetadata> createEndpointAsync(@Nullable LocationName parent, Endpoint endpoint, String endpointId)

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Endpoint endpoint = Endpoint.newBuilder().build();
       String endpointId = "endpointId-1837754992";
       Endpoint response =
           endpointServiceClient.createEndpointAsync(parent, endpoint, endpointId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the Endpoint in. Format: `projects/{project}/locations/{location}`  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint to create.  
`endpointId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### createEndpointAsync(CreateEndpointRequest request)
    
    
    public final OperationFuture<Endpoint,CreateEndpointOperationMetadata> createEndpointAsync(CreateEndpointRequest request)

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       CreateEndpointRequest request =
           CreateEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpoint(Endpoint.newBuilder().build())
               .setEndpointId("endpointId-1837754992")
               .build();
       Endpoint response = endpointServiceClient.createEndpointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### createEndpointAsync(String parent, Endpoint endpoint)
    
    
    public final OperationFuture<Endpoint,CreateEndpointOperationMetadata> createEndpointAsync(String parent, Endpoint endpoint)

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Endpoint endpoint = Endpoint.newBuilder().build();
       Endpoint response = endpointServiceClient.createEndpointAsync(parent, endpoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the Endpoint in. Format: `projects/{project}/locations/{location}`  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### createEndpointAsync(String parent, Endpoint endpoint, String endpointId)
    
    
    public final OperationFuture<Endpoint,CreateEndpointOperationMetadata> createEndpointAsync(String parent, Endpoint endpoint, String endpointId)

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Endpoint endpoint = Endpoint.newBuilder().build();
       String endpointId = "endpointId-1837754992";
       Endpoint response =
           endpointServiceClient.createEndpointAsync(parent, endpoint, endpointId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the Endpoint in. Format: `projects/{project}/locations/{location}`  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint to create.  
`endpointId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Immutable. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. If the first character is a letter, this value may be up to 63 characters, and valid characters are `[a-z0-9-]`. The last character must be a letter or number. If the first character is a number, this value may be up to 9 characters, and valid characters are `[0-9]` with no leading zeros. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### createEndpointCallable()
    
    
    public final UnaryCallable<CreateEndpointRequest,Operation> createEndpointCallable()

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       CreateEndpointRequest request =
           CreateEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpoint(Endpoint.newBuilder().build())
               .setEndpointId("endpointId-1837754992")
               .build();
       ApiFuture<Operation> future =
           endpointServiceClient.createEndpointCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEndpointOperationCallable()
    
    
    public final OperationCallable<CreateEndpointRequest,Endpoint,CreateEndpointOperationMetadata> createEndpointOperationCallable()

Creates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       CreateEndpointRequest request =
           CreateEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setEndpoint(Endpoint.newBuilder().build())
               .setEndpointId("endpointId-1837754992")
               .build();
       OperationFuture<Endpoint, CreateEndpointOperationMetadata> future =
           endpointServiceClient.createEndpointOperationCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[CreateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateEndpointOperationMetadata)>` |   
  
### deleteEndpointAsync(@Nullable EndpointName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEndpointAsync(@Nullable EndpointName name)

Deletes an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName name =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       endpointServiceClient.deleteEndpointAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint resource to be deleted. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEndpointAsync(DeleteEndpointRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEndpointAsync(DeleteEndpointRequest request)

Deletes an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeleteEndpointRequest request =
           DeleteEndpointRequest.newBuilder()
               .setName(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .build();
       endpointServiceClient.deleteEndpointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEndpointAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteEndpointAsync(String name)

Deletes an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String name =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       endpointServiceClient.deleteEndpointAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint resource to be deleted. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteEndpointCallable()
    
    
    public final UnaryCallable<DeleteEndpointRequest,Operation> deleteEndpointCallable()

Deletes an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeleteEndpointRequest request =
           DeleteEndpointRequest.newBuilder()
               .setName(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           endpointServiceClient.deleteEndpointCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEndpointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEndpointOperationCallable()
    
    
    public final OperationCallable<DeleteEndpointRequest,Empty,DeleteOperationMetadata> deleteEndpointOperationCallable()

Deletes an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeleteEndpointRequest request =
           DeleteEndpointRequest.newBuilder()
               .setName(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           endpointServiceClient.deleteEndpointOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteEndpointRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deployModelAsync(@Nullable EndpointName endpoint, DeployedModel deployedModel, Map<String,Integer> trafficSplit)
    
    
    public final OperationFuture<DeployModelResponse,DeployModelOperationMetadata> deployModelAsync(@Nullable EndpointName endpoint, DeployedModel deployedModel, Map<String,Integer> trafficSplit)

Deploys a Model into this Endpoint, creating a DeployedModel within it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       DeployedModel deployedModel = DeployedModel.newBuilder().build();
       Map<String, Integer> trafficSplit = new HashMap<>();
       DeployModelResponse response =
           endpointServiceClient.deployModelAsync(endpoint, deployedModel, trafficSplit).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint resource into which to deploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModel` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
Required. The DeployedModel to be created within the Endpoint. Note that Endpoint.traffic_split must be updated for the DeployedModel to start receiving traffic, either as part of this call, or via EndpointService.UpdateEndpoint.  
`trafficSplit` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If this field is non-empty, then the Endpoint's traffic_split will be overwritten with it. To refer to the ID of the just being deployed Model, a "0" should be used, and the actual ID of the new DeployedModel will be filled in its place by this method. The traffic percentage values must add up to 100. If this field is empty, then the Endpoint's traffic_split is not updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse),[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata)>` |   
  
### deployModelAsync(DeployModelRequest request)
    
    
    public final OperationFuture<DeployModelResponse,DeployModelOperationMetadata> deployModelAsync(DeployModelRequest request)

Deploys a Model into this Endpoint, creating a DeployedModel within it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       DeployModelResponse response = endpointServiceClient.deployModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse),[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata)>` |   
  
### deployModelAsync(String endpoint, DeployedModel deployedModel, Map<String,Integer> trafficSplit)
    
    
    public final OperationFuture<DeployModelResponse,DeployModelOperationMetadata> deployModelAsync(String endpoint, DeployedModel deployedModel, Map<String,Integer> trafficSplit)

Deploys a Model into this Endpoint, creating a DeployedModel within it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       DeployedModel deployedModel = DeployedModel.newBuilder().build();
       Map<String, Integer> trafficSplit = new HashMap<>();
       DeployModelResponse response =
           endpointServiceClient.deployModelAsync(endpoint, deployedModel, trafficSplit).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint resource into which to deploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModel` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
Required. The DeployedModel to be created within the Endpoint. Note that Endpoint.traffic_split must be updated for the DeployedModel to start receiving traffic, either as part of this call, or via EndpointService.UpdateEndpoint.  
`trafficSplit` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If this field is non-empty, then the Endpoint's traffic_split will be overwritten with it. To refer to the ID of the just being deployed Model, a "0" should be used, and the actual ID of the new DeployedModel will be filled in its place by this method. The traffic percentage values must add up to 100. If this field is empty, then the Endpoint's traffic_split is not updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse),[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata)>` |   
  
### deployModelCallable()
    
    
    public final UnaryCallable<DeployModelRequest,Operation> deployModelCallable()

Deploys a Model into this Endpoint, creating a DeployedModel within it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       ApiFuture<Operation> future = endpointServiceClient.deployModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployModelOperationCallable()
    
    
    public final OperationCallable<DeployModelRequest,DeployModelResponse,DeployModelOperationMetadata> deployModelOperationCallable()

Deploys a Model into this Endpoint, creating a DeployedModel within it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       DeployModelRequest request =
           DeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       OperationFuture<DeployModelResponse, DeployModelOperationMetadata> future =
           endpointServiceClient.deployModelOperationCallable().futureCall(request);
       // Do something.
       DeployModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelRequest),[DeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelResponse),[DeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployModelOperationMetadata)>` |   
  
### getEndpoint(@Nullable EndpointName name)
    
    
    public final Endpoint getEndpoint(@Nullable EndpointName name)

Gets an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName name =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       Endpoint response = endpointServiceClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint resource. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### getEndpoint(GetEndpointRequest request)
    
    
    public final Endpoint getEndpoint(GetEndpointRequest request)

Gets an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .build();
       Endpoint response = endpointServiceClient.getEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### getEndpoint(String name)
    
    
    public final Endpoint getEndpoint(String name)

Gets an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String name =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       Endpoint response = endpointServiceClient.getEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint resource. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### getEndpointCallable()
    
    
    public final UnaryCallable<GetEndpointRequest,Endpoint> getEndpointCallable()

Gets an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetEndpointRequest request =
           GetEndpointRequest.newBuilder()
               .setName(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .build();
       ApiFuture<Endpoint> future = endpointServiceClient.getEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = endpointServiceClient.getIamPolicy(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = endpointServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = endpointServiceClient.getLocation(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = endpointServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable EndpointServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointServiceSettings` |   
  
### getStub()
    
    
    public EndpointServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.EndpointServiceStub)` |   
  
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
  
### listEndpoints(@Nullable LocationName parent)
    
    
    public final EndpointServiceClient.ListEndpointsPagedResponse listEndpoints(@Nullable LocationName parent)

Lists Endpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Endpoint element : endpointServiceClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the Endpoints. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(ListEndpointsRequest request)
    
    
    public final EndpointServiceClient.ListEndpointsPagedResponse listEndpoints(ListEndpointsRequest request)

Lists Endpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Endpoint element : endpointServiceClient.listEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpoints(String parent)
    
    
    public final EndpointServiceClient.ListEndpointsPagedResponse listEndpoints(String parent)

Lists Endpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Endpoint element : endpointServiceClient.listEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the Endpoints. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[EndpointServiceClient.ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListEndpointsPagedResponse)` |   
  
### listEndpointsCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,ListEndpointsResponse> listEndpointsCallable()

Lists Endpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEndpointsResponse response =
             endpointServiceClient.listEndpointsCallable().call(request);
         for (Endpoint element : response.getEndpointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEndpointsRequest),[ListEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEndpointsResponse)>` |   
  
### listEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListEndpointsRequest,EndpointServiceClient.ListEndpointsPagedResponse> listEndpointsPagedCallable()

Lists Endpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListEndpointsRequest request =
           ListEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Endpoint> future =
           endpointServiceClient.listEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (Endpoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListEndpointsRequest),[ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListEndpointsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final EndpointServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : endpointServiceClient.listLocations(request).iterateAll()) {
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
`[EndpointServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             endpointServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,EndpointServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           endpointServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EndpointServiceClient.ListLocationsPagedResponse)>` |   
  
### mutateDeployedModelAsync(@Nullable EndpointName endpoint, DeployedModel deployedModel, FieldMask updateMask)
    
    
    public final OperationFuture<MutateDeployedModelResponse,MutateDeployedModelOperationMetadata> mutateDeployedModelAsync(@Nullable EndpointName endpoint, DeployedModel deployedModel, FieldMask updateMask)

Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       DeployedModel deployedModel = DeployedModel.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MutateDeployedModelResponse response =
           endpointServiceClient.mutateDeployedModelAsync(endpoint, deployedModel, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModel` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
Required. The DeployedModel to be mutated within the Endpoint. Only the following fields can be mutated: 

  * `min_replica_count` in either DedicatedResources or AutomaticResources
  * `max_replica_count` in either DedicatedResources or AutomaticResources
  * `required_replica_count` in DedicatedResources
  * autoscaling_metric_specs
  * `disable_container_logging` (v1 only) 
  * `enable_container_logging` (v1beta1 only) 

  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. See google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelResponse),[MutateDeployedModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelOperationMetadata)>` |   
  
### mutateDeployedModelAsync(MutateDeployedModelRequest request)
    
    
    public final OperationFuture<MutateDeployedModelResponse,MutateDeployedModelOperationMetadata> mutateDeployedModelAsync(MutateDeployedModelRequest request)

Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       MutateDeployedModelRequest request =
           MutateDeployedModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       MutateDeployedModelResponse response =
           endpointServiceClient.mutateDeployedModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MutateDeployedModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelResponse),[MutateDeployedModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelOperationMetadata)>` |   
  
### mutateDeployedModelAsync(String endpoint, DeployedModel deployedModel, FieldMask updateMask)
    
    
    public final OperationFuture<MutateDeployedModelResponse,MutateDeployedModelOperationMetadata> mutateDeployedModelAsync(String endpoint, DeployedModel deployedModel, FieldMask updateMask)

Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       DeployedModel deployedModel = DeployedModel.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       MutateDeployedModelResponse response =
           endpointServiceClient.mutateDeployedModelAsync(endpoint, deployedModel, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint resource into which to mutate a DeployedModel. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModel` | `[DeployedModel](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedModel)`  
Required. The DeployedModel to be mutated within the Endpoint. Only the following fields can be mutated: 

  * `min_replica_count` in either DedicatedResources or AutomaticResources
  * `max_replica_count` in either DedicatedResources or AutomaticResources
  * `required_replica_count` in DedicatedResources
  * autoscaling_metric_specs
  * `disable_container_logging` (v1 only) 
  * `enable_container_logging` (v1beta1 only) 

  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. See google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelResponse),[MutateDeployedModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelOperationMetadata)>` |   
  
### mutateDeployedModelCallable()
    
    
    public final UnaryCallable<MutateDeployedModelRequest,Operation> mutateDeployedModelCallable()

Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       MutateDeployedModelRequest request =
           MutateDeployedModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           endpointServiceClient.mutateDeployedModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MutateDeployedModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### mutateDeployedModelOperationCallable()
    
    
    public final OperationCallable<MutateDeployedModelRequest,MutateDeployedModelResponse,MutateDeployedModelOperationMetadata> mutateDeployedModelOperationCallable()

Updates an existing deployed model. Updatable fields include `min_replica_count`, `max_replica_count`, `required_replica_count`, `autoscaling_metric_specs`, `disable_container_logging` (v1 only), and `enable_container_logging` (v1beta1 only).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       MutateDeployedModelRequest request =
           MutateDeployedModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModel(DeployedModel.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<MutateDeployedModelResponse, MutateDeployedModelOperationMetadata> future =
           endpointServiceClient.mutateDeployedModelOperationCallable().futureCall(request);
       // Do something.
       MutateDeployedModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MutateDeployedModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelRequest),[MutateDeployedModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelResponse),[MutateDeployedModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedModelOperationMetadata)>` |   
  
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = endpointServiceClient.setIamPolicy(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = endpointServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = endpointServiceClient.testIamPermissions(request);
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
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           endpointServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### undeployModelAsync(@Nullable EndpointName endpoint, String deployedModelId, Map<String,Integer> trafficSplit)
    
    
    public final OperationFuture<UndeployModelResponse,UndeployModelOperationMetadata> undeployModelAsync(@Nullable EndpointName endpoint, String deployedModelId, Map<String,Integer> trafficSplit)

Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       EndpointName endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]");
       String deployedModelId = "deployedModelId-1817547906";
       Map<String, Integer> trafficSplit = new HashMap<>();
       UndeployModelResponse response =
           endpointServiceClient.undeployModelAsync(endpoint, deployedModelId, trafficSplit).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.EndpointName`  
Required. The name of the Endpoint resource from which to undeploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DeployedModel to be undeployed from the Endpoint.  
`trafficSplit` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
If this field is provided, then the Endpoint's traffic_split will be overwritten with it. If last DeployedModel is being undeployed from the Endpoint, the [Endpoint.traffic_split] will always end up empty when this call returns. A DeployedModel will be successfully undeployed only if it doesn't have any traffic assigned to it when this method executes, or if this field unassigns any traffic to it.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelResponse),[UndeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelOperationMetadata)>` |   
  
### undeployModelAsync(UndeployModelRequest request)
    
    
    public final OperationFuture<UndeployModelResponse,UndeployModelOperationMetadata> undeployModelAsync(UndeployModelRequest request)

Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       UndeployModelResponse response = endpointServiceClient.undeployModelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelResponse),[UndeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelOperationMetadata)>` |   
  
### undeployModelAsync(String endpoint, String deployedModelId, Map<String,Integer> trafficSplit)
    
    
    public final OperationFuture<UndeployModelResponse,UndeployModelOperationMetadata> undeployModelAsync(String endpoint, String deployedModelId, Map<String,Integer> trafficSplit)

Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       String endpoint =
           EndpointName.ofProjectLocationEndpointName("[PROJECT]", "[LOCATION]", "[ENDPOINT]")
               .toString();
       String deployedModelId = "deployedModelId-1817547906";
       Map<String, Integer> trafficSplit = new HashMap<>();
       UndeployModelResponse response =
           endpointServiceClient.undeployModelAsync(endpoint, deployedModelId, trafficSplit).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Endpoint resource from which to undeploy a Model. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`deployedModelId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DeployedModel to be undeployed from the Endpoint.  
`trafficSplit` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
If this field is provided, then the Endpoint's traffic_split will be overwritten with it. If last DeployedModel is being undeployed from the Endpoint, the [Endpoint.traffic_split] will always end up empty when this call returns. A DeployedModel will be successfully undeployed only if it doesn't have any traffic assigned to it when this method executes, or if this field unassigns any traffic to it.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelResponse),[UndeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelOperationMetadata)>` |   
  
### undeployModelCallable()
    
    
    public final UnaryCallable<UndeployModelRequest,Operation> undeployModelCallable()

Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       ApiFuture<Operation> future =
           endpointServiceClient.undeployModelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeployModelOperationCallable()
    
    
    public final OperationCallable<UndeployModelRequest,UndeployModelResponse,UndeployModelOperationMetadata> undeployModelOperationCallable()

Undeploys a Model from an Endpoint, removing a DeployedModel from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UndeployModelRequest request =
           UndeployModelRequest.newBuilder()
               .setEndpoint(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setDeployedModelId("deployedModelId-1817547906")
               .putAllTrafficSplit(new HashMap<String, Integer>())
               .build();
       OperationFuture<UndeployModelResponse, UndeployModelOperationMetadata> future =
           endpointServiceClient.undeployModelOperationCallable().futureCall(request);
       // Do something.
       UndeployModelResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelRequest),[UndeployModelResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelResponse),[UndeployModelOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployModelOperationMetadata)>` |   
  
### updateEndpoint(Endpoint endpoint, FieldMask updateMask)
    
    
    public final Endpoint updateEndpoint(Endpoint endpoint, FieldMask updateMask)

Updates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       Endpoint endpoint = Endpoint.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Endpoint response = endpointServiceClient.updateEndpoint(endpoint, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. See google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### updateEndpoint(UpdateEndpointRequest request)
    
    
    public final Endpoint updateEndpoint(UpdateEndpointRequest request)

Updates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UpdateEndpointRequest request =
           UpdateEndpointRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Endpoint response = endpointServiceClient.updateEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)` |   
  
### updateEndpointCallable()
    
    
    public final UnaryCallable<UpdateEndpointRequest,Endpoint> updateEndpointCallable()

Updates an Endpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UpdateEndpointRequest request =
           UpdateEndpointRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Endpoint> future =
           endpointServiceClient.updateEndpointCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)>` |   
  
### updateEndpointLongRunningAsync(Endpoint endpoint)
    
    
    public final OperationFuture<Endpoint,UpdateEndpointOperationMetadata> updateEndpointLongRunningAsync(Endpoint endpoint)

Updates an Endpoint with a long running operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       Endpoint endpoint = Endpoint.newBuilder().build();
       Endpoint response = endpointServiceClient.updateEndpointLongRunningAsync(endpoint).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint)`  
Required. The Endpoint which replaces the resource on the server. Currently we only support updating the `client_connection_config` field, all the other fields' update will be blocked.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[UpdateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointOperationMetadata)>` |   
  
### updateEndpointLongRunningAsync(UpdateEndpointLongRunningRequest request)
    
    
    public final OperationFuture<Endpoint,UpdateEndpointOperationMetadata> updateEndpointLongRunningAsync(UpdateEndpointLongRunningRequest request)

Updates an Endpoint with a long running operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UpdateEndpointLongRunningRequest request =
           UpdateEndpointLongRunningRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .build();
       Endpoint response = endpointServiceClient.updateEndpointLongRunningAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEndpointLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointLongRunningRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[UpdateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointOperationMetadata)>` |   
  
### updateEndpointLongRunningCallable()
    
    
    public final UnaryCallable<UpdateEndpointLongRunningRequest,Operation> updateEndpointLongRunningCallable()

Updates an Endpoint with a long running operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UpdateEndpointLongRunningRequest request =
           UpdateEndpointLongRunningRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           endpointServiceClient.updateEndpointLongRunningCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEndpointLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointLongRunningRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEndpointLongRunningOperationCallable()
    
    
    public final OperationCallable<UpdateEndpointLongRunningRequest,Endpoint,UpdateEndpointOperationMetadata> updateEndpointLongRunningOperationCallable()

Updates an Endpoint with a long running operation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (EndpointServiceClient endpointServiceClient = EndpointServiceClient.create()) {
       UpdateEndpointLongRunningRequest request =
           UpdateEndpointLongRunningRequest.newBuilder()
               .setEndpoint(Endpoint.newBuilder().build())
               .build();
       OperationFuture<Endpoint, UpdateEndpointOperationMetadata> future =
           endpointServiceClient.updateEndpointLongRunningOperationCallable().futureCall(request);
       // Do something.
       Endpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEndpointLongRunningRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointLongRunningRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Endpoint),[UpdateEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateEndpointOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
