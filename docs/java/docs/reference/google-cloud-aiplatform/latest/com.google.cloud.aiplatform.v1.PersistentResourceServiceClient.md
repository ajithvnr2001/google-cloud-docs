---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient
title: Class PersistentResourceServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:24.605389+00:00
---

# Class PersistentResourceServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PersistentResourceServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/PersistentResourceServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing Vertex AI's machine learning PersistentResource.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       PersistentResourceName name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]");
       PersistentResource response = persistentResourceServiceClient.getPersistentResource(name);
     }
     

Note: close() needs to be called on the PersistentResourceServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreatePersistentResource |  Creates a PersistentResource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPersistentResourceAsync(CreatePersistentResourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPersistentResourceAsync(LocationName parent, PersistentResource persistentResource, String persistentResourceId) 
  * createPersistentResourceAsync(String parent, PersistentResource persistentResource, String persistentResourceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPersistentResourceOperationCallable() 
  * createPersistentResourceCallable() 

  
GetPersistentResource |  Gets a PersistentResource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPersistentResource(GetPersistentResourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPersistentResource(PersistentResourceName name) 
  * getPersistentResource(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPersistentResourceCallable() 

  
ListPersistentResources |  Lists PersistentResources in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPersistentResources(ListPersistentResourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPersistentResources(LocationName parent) 
  * listPersistentResources(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPersistentResourcesPagedCallable() 
  * listPersistentResourcesCallable() 

  
DeletePersistentResource |  Deletes a PersistentResource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePersistentResourceAsync(DeletePersistentResourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePersistentResourceAsync(PersistentResourceName name) 
  * deletePersistentResourceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePersistentResourceOperationCallable() 
  * deletePersistentResourceCallable() 

  
UpdatePersistentResource |  Updates a PersistentResource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updatePersistentResourceAsync(UpdatePersistentResourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updatePersistentResourceAsync(PersistentResource persistentResource, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updatePersistentResourceOperationCallable() 
  * updatePersistentResourceCallable() 

  
RebootPersistentResource |  Reboots a PersistentResource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rebootPersistentResourceAsync(RebootPersistentResourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * rebootPersistentResourceAsync(PersistentResourceName name) 
  * rebootPersistentResourceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rebootPersistentResourceOperationCallable() 
  * rebootPersistentResourceCallable() 

  
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

This class can be customized by passing in a custom instance of PersistentResourceServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PersistentResourceServiceSettings persistentResourceServiceSettings =
         PersistentResourceServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create(persistentResourceServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PersistentResourceServiceSettings persistentResourceServiceSettings =
         PersistentResourceServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create(persistentResourceServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PersistentResourceServiceClient

## Static Methods 

### create()
    
    
    public static final PersistentResourceServiceClient create()

Constructs an instance of PersistentResourceServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PersistentResourceServiceSettings settings)
    
    
    public static final PersistentResourceServiceClient create(PersistentResourceServiceSettings settings)

Constructs an instance of PersistentResourceServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PersistentResourceServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PersistentResourceServiceStub stub)
    
    
    public static final PersistentResourceServiceClient create(PersistentResourceServiceStub stub)

Constructs an instance of PersistentResourceServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PersistentResourceServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PersistentResourceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PersistentResourceServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient)` |   
  
## Constructors 

### PersistentResourceServiceClient(PersistentResourceServiceSettings settings)
    
    
    protected PersistentResourceServiceClient(PersistentResourceServiceSettings settings)

Constructs an instance of PersistentResourceServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PersistentResourceServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceSettings)`  
  
  
### PersistentResourceServiceClient(PersistentResourceServiceStub stub)
    
    
    protected PersistentResourceServiceClient(PersistentResourceServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PersistentResourceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PersistentResourceServiceStub)`  
  
  
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

### createPersistentResourceAsync(@Nullable LocationName parent, PersistentResource persistentResource, String persistentResourceId)
    
    
    public final OperationFuture<PersistentResource,CreatePersistentResourceOperationMetadata> createPersistentResourceAsync(@Nullable LocationName parent, PersistentResource persistentResource, String persistentResourceId)

Creates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PersistentResource persistentResource = PersistentResource.newBuilder().build();
       String persistentResourceId = "persistentResourceId-2123080768";
       PersistentResource response =
           persistentResourceServiceClient
               .createPersistentResourceAsync(parent, persistentResource, persistentResourceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the PersistentResource in. Format: `projects/{project}/locations/{location}`  
`persistentResource` | `[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)`  
Required. The PersistentResource to create.  
`persistentResourceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the PersistentResource, which become the final component of the PersistentResource's resource name. The maximum length is 63 characters, and valid characters are `/^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[CreatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceOperationMetadata)>` |   
  
### createPersistentResourceAsync(CreatePersistentResourceRequest request)
    
    
    public final OperationFuture<PersistentResource,CreatePersistentResourceOperationMetadata> createPersistentResourceAsync(CreatePersistentResourceRequest request)

Creates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       CreatePersistentResourceRequest request =
           CreatePersistentResourceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setPersistentResourceId("persistentResourceId-2123080768")
               .build();
       PersistentResource response =
           persistentResourceServiceClient.createPersistentResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[CreatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceOperationMetadata)>` |   
  
### createPersistentResourceAsync(String parent, PersistentResource persistentResource, String persistentResourceId)
    
    
    public final OperationFuture<PersistentResource,CreatePersistentResourceOperationMetadata> createPersistentResourceAsync(String parent, PersistentResource persistentResource, String persistentResourceId)

Creates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PersistentResource persistentResource = PersistentResource.newBuilder().build();
       String persistentResourceId = "persistentResourceId-2123080768";
       PersistentResource response =
           persistentResourceServiceClient
               .createPersistentResourceAsync(parent, persistentResource, persistentResourceId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the PersistentResource in. Format: `projects/{project}/locations/{location}`  
`persistentResource` | `[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)`  
Required. The PersistentResource to create.  
`persistentResourceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the PersistentResource, which become the final component of the PersistentResource's resource name. The maximum length is 63 characters, and valid characters are `/^[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[CreatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceOperationMetadata)>` |   
  
### createPersistentResourceCallable()
    
    
    public final UnaryCallable<CreatePersistentResourceRequest,Operation> createPersistentResourceCallable()

Creates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       CreatePersistentResourceRequest request =
           CreatePersistentResourceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setPersistentResourceId("persistentResourceId-2123080768")
               .build();
       ApiFuture<Operation> future =
           persistentResourceServiceClient.createPersistentResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPersistentResourceOperationCallable()
    
    
    public final OperationCallable<CreatePersistentResourceRequest,PersistentResource,CreatePersistentResourceOperationMetadata> createPersistentResourceOperationCallable()

Creates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       CreatePersistentResourceRequest request =
           CreatePersistentResourceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setPersistentResourceId("persistentResourceId-2123080768")
               .build();
       OperationFuture<PersistentResource, CreatePersistentResourceOperationMetadata> future =
           persistentResourceServiceClient
               .createPersistentResourceOperationCallable()
               .futureCall(request);
       // Do something.
       PersistentResource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceRequest),[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[CreatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePersistentResourceOperationMetadata)>` |   
  
### deletePersistentResourceAsync(@Nullable PersistentResourceName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePersistentResourceAsync(@Nullable PersistentResourceName name)

Deletes a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       PersistentResourceName name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]");
       persistentResourceServiceClient.deletePersistentResourceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PersistentResourceName`  
Required. The name of the PersistentResource to be deleted. Format: `projects/{project}/locations/{location}/persistentResources/{persistent_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePersistentResourceAsync(DeletePersistentResourceRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePersistentResourceAsync(DeletePersistentResourceRequest request)

Deletes a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       DeletePersistentResourceRequest request =
           DeletePersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       persistentResourceServiceClient.deletePersistentResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePersistentResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePersistentResourceAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePersistentResourceAsync(String name)

Deletes a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       String name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]").toString();
       persistentResourceServiceClient.deletePersistentResourceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PersistentResource to be deleted. Format: `projects/{project}/locations/{location}/persistentResources/{persistent_resource}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePersistentResourceCallable()
    
    
    public final UnaryCallable<DeletePersistentResourceRequest,Operation> deletePersistentResourceCallable()

Deletes a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       DeletePersistentResourceRequest request =
           DeletePersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           persistentResourceServiceClient.deletePersistentResourceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePersistentResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePersistentResourceOperationCallable()
    
    
    public final OperationCallable<DeletePersistentResourceRequest,Empty,DeleteOperationMetadata> deletePersistentResourceOperationCallable()

Deletes a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       DeletePersistentResourceRequest request =
           DeletePersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           persistentResourceServiceClient
               .deletePersistentResourceOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePersistentResourceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = persistentResourceServiceClient.getIamPolicy(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           persistentResourceServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = persistentResourceServiceClient.getLocation(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           persistentResourceServiceClient.getLocationCallable().futureCall(request);
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
  
### getPersistentResource(@Nullable PersistentResourceName name)
    
    
    public final PersistentResource getPersistentResource(@Nullable PersistentResourceName name)

Gets a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       PersistentResourceName name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]");
       PersistentResource response = persistentResourceServiceClient.getPersistentResource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PersistentResourceName`  
Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)` |   
  
### getPersistentResource(GetPersistentResourceRequest request)
    
    
    public final PersistentResource getPersistentResource(GetPersistentResourceRequest request)

Gets a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetPersistentResourceRequest request =
           GetPersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       PersistentResource response = persistentResourceServiceClient.getPersistentResource(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetPersistentResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)` |   
  
### getPersistentResource(String name)
    
    
    public final PersistentResource getPersistentResource(String name)

Gets a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       String name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]").toString();
       PersistentResource response = persistentResourceServiceClient.getPersistentResource(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)` |   
  
### getPersistentResourceCallable()
    
    
    public final UnaryCallable<GetPersistentResourceRequest,PersistentResource> getPersistentResourceCallable()

Gets a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       GetPersistentResourceRequest request =
           GetPersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       ApiFuture<PersistentResource> future =
           persistentResourceServiceClient.getPersistentResourceCallable().futureCall(request);
       // Do something.
       PersistentResource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetPersistentResourceRequest),[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)>` |   
  
### getSettings()
    
    
    public final @Nullable PersistentResourceServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PersistentResourceServiceSettings` |   
  
### getStub()
    
    
    public PersistentResourceServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PersistentResourceServiceStub)` |   
  
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
    
    
    public final PersistentResourceServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : persistentResourceServiceClient.listLocations(request).iterateAll()) {
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
`[PersistentResourceServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             persistentResourceServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,PersistentResourceServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           persistentResourceServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListLocationsPagedResponse)>` |   
  
### listPersistentResources(@Nullable LocationName parent)
    
    
    public final PersistentResourceServiceClient.ListPersistentResourcesPagedResponse listPersistentResources(@Nullable LocationName parent)

Lists PersistentResources in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PersistentResource element :
           persistentResourceServiceClient.listPersistentResources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the PersistentResources from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient.ListPersistentResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListPersistentResourcesPagedResponse)` |   
  
### listPersistentResources(ListPersistentResourcesRequest request)
    
    
    public final PersistentResourceServiceClient.ListPersistentResourcesPagedResponse listPersistentResources(ListPersistentResourcesRequest request)

Lists PersistentResources in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListPersistentResourcesRequest request =
           ListPersistentResourcesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (PersistentResource element :
           persistentResourceServiceClient.listPersistentResources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPersistentResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPersistentResourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient.ListPersistentResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListPersistentResourcesPagedResponse)` |   
  
### listPersistentResources(String parent)
    
    
    public final PersistentResourceServiceClient.ListPersistentResourcesPagedResponse listPersistentResources(String parent)

Lists PersistentResources in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PersistentResource element :
           persistentResourceServiceClient.listPersistentResources(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the PersistentResources from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PersistentResourceServiceClient.ListPersistentResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListPersistentResourcesPagedResponse)` |   
  
### listPersistentResourcesCallable()
    
    
    public final UnaryCallable<ListPersistentResourcesRequest,ListPersistentResourcesResponse> listPersistentResourcesCallable()

Lists PersistentResources in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListPersistentResourcesRequest request =
           ListPersistentResourcesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListPersistentResourcesResponse response =
             persistentResourceServiceClient.listPersistentResourcesCallable().call(request);
         for (PersistentResource element : response.getPersistentResourcesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPersistentResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPersistentResourcesRequest),[ListPersistentResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPersistentResourcesResponse)>` |   
  
### listPersistentResourcesPagedCallable()
    
    
    public final UnaryCallable<ListPersistentResourcesRequest,PersistentResourceServiceClient.ListPersistentResourcesPagedResponse> listPersistentResourcesPagedCallable()

Lists PersistentResources in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       ListPersistentResourcesRequest request =
           ListPersistentResourcesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<PersistentResource> future =
           persistentResourceServiceClient
               .listPersistentResourcesPagedCallable()
               .futureCall(request);
       // Do something.
       for (PersistentResource element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPersistentResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPersistentResourcesRequest),[ListPersistentResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResourceServiceClient.ListPersistentResourcesPagedResponse)>` |   
  
### rebootPersistentResourceAsync(@Nullable PersistentResourceName name)
    
    
    public final OperationFuture<PersistentResource,RebootPersistentResourceOperationMetadata> rebootPersistentResourceAsync(@Nullable PersistentResourceName name)

Reboots a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       PersistentResourceName name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]");
       PersistentResource response =
           persistentResourceServiceClient.rebootPersistentResourceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PersistentResourceName`  
Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[RebootPersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceOperationMetadata)>` |   
  
### rebootPersistentResourceAsync(RebootPersistentResourceRequest request)
    
    
    public final OperationFuture<PersistentResource,RebootPersistentResourceOperationMetadata> rebootPersistentResourceAsync(RebootPersistentResourceRequest request)

Reboots a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       RebootPersistentResourceRequest request =
           RebootPersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       PersistentResource response =
           persistentResourceServiceClient.rebootPersistentResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RebootPersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[RebootPersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceOperationMetadata)>` |   
  
### rebootPersistentResourceAsync(String name)
    
    
    public final OperationFuture<PersistentResource,RebootPersistentResourceOperationMetadata> rebootPersistentResourceAsync(String name)

Reboots a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       String name =
           PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]").toString();
       PersistentResource response =
           persistentResourceServiceClient.rebootPersistentResourceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[RebootPersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceOperationMetadata)>` |   
  
### rebootPersistentResourceCallable()
    
    
    public final UnaryCallable<RebootPersistentResourceRequest,Operation> rebootPersistentResourceCallable()

Reboots a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       RebootPersistentResourceRequest request =
           RebootPersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           persistentResourceServiceClient.rebootPersistentResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RebootPersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rebootPersistentResourceOperationCallable()
    
    
    public final OperationCallable<RebootPersistentResourceRequest,PersistentResource,RebootPersistentResourceOperationMetadata> rebootPersistentResourceOperationCallable()

Reboots a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       RebootPersistentResourceRequest request =
           RebootPersistentResourceRequest.newBuilder()
               .setName(
                   PersistentResourceName.of("[PROJECT]", "[LOCATION]", "[PERSISTENT_RESOURCE]")
                       .toString())
               .build();
       OperationFuture<PersistentResource, RebootPersistentResourceOperationMetadata> future =
           persistentResourceServiceClient
               .rebootPersistentResourceOperationCallable()
               .futureCall(request);
       // Do something.
       PersistentResource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RebootPersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceRequest),[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[RebootPersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RebootPersistentResourceOperationMetadata)>` |   
  
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = persistentResourceServiceClient.setIamPolicy(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
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
           persistentResourceServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           persistentResourceServiceClient.testIamPermissions(request);
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
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           persistentResourceServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updatePersistentResourceAsync(PersistentResource persistentResource, FieldMask updateMask)
    
    
    public final OperationFuture<PersistentResource,UpdatePersistentResourceOperationMetadata> updatePersistentResourceAsync(PersistentResource persistentResource, FieldMask updateMask)

Updates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       PersistentResource persistentResource = PersistentResource.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       PersistentResource response =
           persistentResourceServiceClient
               .updatePersistentResourceAsync(persistentResource, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`persistentResource` | `[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource)`  
Required. The PersistentResource to update. The PersistentResource's `name` field is used to identify the PersistentResource to update. Format: `projects/{project}/locations/{location}/persistentResources/{persistent_resource}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Specify the fields to be overwritten in the PersistentResource by the update method.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[UpdatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceOperationMetadata)>` |   
  
### updatePersistentResourceAsync(UpdatePersistentResourceRequest request)
    
    
    public final OperationFuture<PersistentResource,UpdatePersistentResourceOperationMetadata> updatePersistentResourceAsync(UpdatePersistentResourceRequest request)

Updates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       UpdatePersistentResourceRequest request =
           UpdatePersistentResourceRequest.newBuilder()
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       PersistentResource response =
           persistentResourceServiceClient.updatePersistentResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[UpdatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceOperationMetadata)>` |   
  
### updatePersistentResourceCallable()
    
    
    public final UnaryCallable<UpdatePersistentResourceRequest,Operation> updatePersistentResourceCallable()

Updates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       UpdatePersistentResourceRequest request =
           UpdatePersistentResourceRequest.newBuilder()
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           persistentResourceServiceClient.updatePersistentResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePersistentResourceOperationCallable()
    
    
    public final OperationCallable<UpdatePersistentResourceRequest,PersistentResource,UpdatePersistentResourceOperationMetadata> updatePersistentResourceOperationCallable()

Updates a PersistentResource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PersistentResourceServiceClient persistentResourceServiceClient =
         PersistentResourceServiceClient.create()) {
       UpdatePersistentResourceRequest request =
           UpdatePersistentResourceRequest.newBuilder()
               .setPersistentResource(PersistentResource.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<PersistentResource, UpdatePersistentResourceOperationMetadata> future =
           persistentResourceServiceClient
               .updatePersistentResourceOperationCallable()
               .futureCall(request);
       // Do something.
       PersistentResource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePersistentResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceRequest),[PersistentResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PersistentResource),[UpdatePersistentResourceOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdatePersistentResourceOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
