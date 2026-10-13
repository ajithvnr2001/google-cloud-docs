---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient
title: Class DepServiceClient (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:04.178178+00:00
---

# Class DepServiceClient (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DepServiceClient (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkservices/google-cloud-networkservices/src/main/java/com/google/cloud/networkservices/v1/DepServiceClient.java)| [Product Reference](https://cloud.google.com/products/networking)  
---|---  
  
Service Description: Service describing handlers for resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbTrafficExtensionName name =
           LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]");
       LbTrafficExtension response = depServiceClient.getLbTrafficExtension(name);
     }
     

Note: close() needs to be called on the DepServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListLbTrafficExtensions |  Lists `LbTrafficExtension` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLbTrafficExtensions(ListLbTrafficExtensionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLbTrafficExtensions(LocationName parent) 
  * listLbTrafficExtensions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLbTrafficExtensionsPagedCallable() 
  * listLbTrafficExtensionsCallable() 

  
GetLbTrafficExtension |  Gets details of the specified `LbTrafficExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLbTrafficExtension(GetLbTrafficExtensionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLbTrafficExtension(LbTrafficExtensionName name) 
  * getLbTrafficExtension(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLbTrafficExtensionCallable() 

  
CreateLbTrafficExtension |  Creates a new `LbTrafficExtension` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLbTrafficExtensionAsync(CreateLbTrafficExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLbTrafficExtensionAsync(LocationName parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId) 
  * createLbTrafficExtensionAsync(String parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLbTrafficExtensionOperationCallable() 
  * createLbTrafficExtensionCallable() 

  
UpdateLbTrafficExtension |  Updates the parameters of the specified `LbTrafficExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLbTrafficExtensionAsync(UpdateLbTrafficExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLbTrafficExtensionAsync(LbTrafficExtension lbTrafficExtension, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLbTrafficExtensionOperationCallable() 
  * updateLbTrafficExtensionCallable() 

  
DeleteLbTrafficExtension |  Deletes the specified `LbTrafficExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLbTrafficExtensionAsync(DeleteLbTrafficExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLbTrafficExtensionAsync(LbTrafficExtensionName name) 
  * deleteLbTrafficExtensionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLbTrafficExtensionOperationCallable() 
  * deleteLbTrafficExtensionCallable() 

  
ListLbRouteExtensions |  Lists `LbRouteExtension` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLbRouteExtensions(ListLbRouteExtensionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLbRouteExtensions(LocationName parent) 
  * listLbRouteExtensions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLbRouteExtensionsPagedCallable() 
  * listLbRouteExtensionsCallable() 

  
GetLbRouteExtension |  Gets details of the specified `LbRouteExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLbRouteExtension(GetLbRouteExtensionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLbRouteExtension(LbRouteExtensionName name) 
  * getLbRouteExtension(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLbRouteExtensionCallable() 

  
CreateLbRouteExtension |  Creates a new `LbRouteExtension` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLbRouteExtensionAsync(CreateLbRouteExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLbRouteExtensionAsync(LocationName parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId) 
  * createLbRouteExtensionAsync(String parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLbRouteExtensionOperationCallable() 
  * createLbRouteExtensionCallable() 

  
UpdateLbRouteExtension |  Updates the parameters of the specified `LbRouteExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLbRouteExtensionAsync(UpdateLbRouteExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLbRouteExtensionAsync(LbRouteExtension lbRouteExtension, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLbRouteExtensionOperationCallable() 
  * updateLbRouteExtensionCallable() 

  
DeleteLbRouteExtension |  Deletes the specified `LbRouteExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLbRouteExtensionAsync(DeleteLbRouteExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLbRouteExtensionAsync(LbRouteExtensionName name) 
  * deleteLbRouteExtensionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLbRouteExtensionOperationCallable() 
  * deleteLbRouteExtensionCallable() 

  
ListLbEdgeExtensions |  Lists `LbEdgeExtension` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLbEdgeExtensions(ListLbEdgeExtensionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLbEdgeExtensions(LocationName parent) 
  * listLbEdgeExtensions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLbEdgeExtensionsPagedCallable() 
  * listLbEdgeExtensionsCallable() 

  
GetLbEdgeExtension |  Gets details of the specified `LbEdgeExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLbEdgeExtension(GetLbEdgeExtensionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLbEdgeExtension(LbEdgeExtensionName name) 
  * getLbEdgeExtension(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLbEdgeExtensionCallable() 

  
CreateLbEdgeExtension |  Creates a new `LbEdgeExtension` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLbEdgeExtensionAsync(CreateLbEdgeExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLbEdgeExtensionAsync(LocationName parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId) 
  * createLbEdgeExtensionAsync(String parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLbEdgeExtensionOperationCallable() 
  * createLbEdgeExtensionCallable() 

  
UpdateLbEdgeExtension |  Updates the parameters of the specified `LbEdgeExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLbEdgeExtensionAsync(UpdateLbEdgeExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLbEdgeExtensionAsync(LbEdgeExtension lbEdgeExtension, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLbEdgeExtensionOperationCallable() 
  * updateLbEdgeExtensionCallable() 

  
DeleteLbEdgeExtension |  Deletes the specified `LbEdgeExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLbEdgeExtensionAsync(DeleteLbEdgeExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLbEdgeExtensionAsync(LbEdgeExtensionName name) 
  * deleteLbEdgeExtensionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLbEdgeExtensionOperationCallable() 
  * deleteLbEdgeExtensionCallable() 

  
ListAuthzExtensions |  Lists `AuthzExtension` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthzExtensions(ListAuthzExtensionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthzExtensions(LocationName parent) 
  * listAuthzExtensions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthzExtensionsPagedCallable() 
  * listAuthzExtensionsCallable() 

  
GetAuthzExtension |  Gets details of the specified `AuthzExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthzExtension(GetAuthzExtensionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthzExtension(AuthzExtensionName name) 
  * getAuthzExtension(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthzExtensionCallable() 

  
CreateAuthzExtension |  Creates a new `AuthzExtension` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAuthzExtensionAsync(CreateAuthzExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAuthzExtensionAsync(LocationName parent, AuthzExtension authzExtension, String authzExtensionId) 
  * createAuthzExtensionAsync(String parent, AuthzExtension authzExtension, String authzExtensionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAuthzExtensionOperationCallable() 
  * createAuthzExtensionCallable() 

  
UpdateAuthzExtension |  Updates the parameters of the specified `AuthzExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAuthzExtensionAsync(UpdateAuthzExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAuthzExtensionAsync(AuthzExtension authzExtension, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAuthzExtensionOperationCallable() 
  * updateAuthzExtensionCallable() 

  
DeleteAuthzExtension |  Deletes the specified `AuthzExtension` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthzExtensionAsync(DeleteAuthzExtensionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAuthzExtensionAsync(AuthzExtensionName name) 
  * deleteAuthzExtensionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthzExtensionOperationCallable() 
  * deleteAuthzExtensionCallable() 

  
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

This class can be customized by passing in a custom instance of DepServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DepServiceSettings depServiceSettings =
         DepServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DepServiceClient depServiceClient = DepServiceClient.create(depServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DepServiceSettings depServiceSettings =
         DepServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DepServiceClient depServiceClient = DepServiceClient.create(depServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DepServiceSettings depServiceSettings = DepServiceSettings.newHttpJsonBuilder().build();
     DepServiceClient depServiceClient = DepServiceClient.create(depServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DepServiceClient

## Static Methods 

### create()
    
    
    public static final DepServiceClient create()

Constructs an instance of DepServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DepServiceSettings settings)
    
    
    public static final DepServiceClient create(DepServiceSettings settings)

Constructs an instance of DepServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DepServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DepServiceStub stub)
    
    
    public static final DepServiceClient create(DepServiceStub stub)

Constructs an instance of DepServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DepServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.DepServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient)` |   
  
## Constructors 

### DepServiceClient(DepServiceSettings settings)
    
    
    protected DepServiceClient(DepServiceSettings settings)

Constructs an instance of DepServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DepServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceSettings)`  
  
  
### DepServiceClient(DepServiceStub stub)
    
    
    protected DepServiceClient(DepServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.DepServiceStub)`  
  
  
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

### createAuthzExtensionAsync(@Nullable LocationName parent, AuthzExtension authzExtension, String authzExtensionId)
    
    
    public final OperationFuture<AuthzExtension,OperationMetadata> createAuthzExtensionAsync(@Nullable LocationName parent, AuthzExtension authzExtension, String authzExtensionId)

Creates a new `AuthzExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AuthzExtension authzExtension = AuthzExtension.newBuilder().build();
       String authzExtensionId = "authzExtensionId-973067640";
       AuthzExtension response =
           depServiceClient
               .createAuthzExtensionAsync(parent, authzExtension, authzExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the `AuthzExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`authzExtension` | `[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)`  
Required. `AuthzExtension` resource to be created.  
`authzExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `AuthzExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAuthzExtensionAsync(CreateAuthzExtensionRequest request)
    
    
    public final OperationFuture<AuthzExtension,OperationMetadata> createAuthzExtensionAsync(CreateAuthzExtensionRequest request)

Creates a new `AuthzExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateAuthzExtensionRequest request =
           CreateAuthzExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzExtensionId("authzExtensionId-973067640")
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthzExtension response = depServiceClient.createAuthzExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAuthzExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAuthzExtensionAsync(String parent, AuthzExtension authzExtension, String authzExtensionId)
    
    
    public final OperationFuture<AuthzExtension,OperationMetadata> createAuthzExtensionAsync(String parent, AuthzExtension authzExtension, String authzExtensionId)

Creates a new `AuthzExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AuthzExtension authzExtension = AuthzExtension.newBuilder().build();
       String authzExtensionId = "authzExtensionId-973067640";
       AuthzExtension response =
           depServiceClient
               .createAuthzExtensionAsync(parent, authzExtension, authzExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `AuthzExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`authzExtension` | `[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)`  
Required. `AuthzExtension` resource to be created.  
`authzExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `AuthzExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAuthzExtensionCallable()
    
    
    public final UnaryCallable<CreateAuthzExtensionRequest,Operation> createAuthzExtensionCallable()

Creates a new `AuthzExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateAuthzExtensionRequest request =
           CreateAuthzExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzExtensionId("authzExtensionId-973067640")
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.createAuthzExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAuthzExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAuthzExtensionOperationCallable()
    
    
    public final OperationCallable<CreateAuthzExtensionRequest,AuthzExtension,OperationMetadata> createAuthzExtensionOperationCallable()

Creates a new `AuthzExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateAuthzExtensionRequest request =
           CreateAuthzExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthzExtensionId("authzExtensionId-973067640")
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AuthzExtension, OperationMetadata> future =
           depServiceClient.createAuthzExtensionOperationCallable().futureCall(request);
       // Do something.
       AuthzExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAuthzExtensionRequest),[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbEdgeExtensionAsync(@Nullable LocationName parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId)
    
    
    public final OperationFuture<LbEdgeExtension,OperationMetadata> createLbEdgeExtensionAsync(@Nullable LocationName parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId)

Creates a new `LbEdgeExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       LbEdgeExtension lbEdgeExtension = LbEdgeExtension.newBuilder().build();
       String lbEdgeExtensionId = "lbEdgeExtensionId673551207";
       LbEdgeExtension response =
           depServiceClient
               .createLbEdgeExtensionAsync(parent, lbEdgeExtension, lbEdgeExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the `LbEdgeExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbEdgeExtension` | `[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)`  
Required. `LbEdgeExtension` resource to be created.  
`lbEdgeExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbEdgeExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbEdgeExtensionAsync(CreateLbEdgeExtensionRequest request)
    
    
    public final OperationFuture<LbEdgeExtension,OperationMetadata> createLbEdgeExtensionAsync(CreateLbEdgeExtensionRequest request)

Creates a new `LbEdgeExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbEdgeExtensionRequest request =
           CreateLbEdgeExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbEdgeExtensionId("lbEdgeExtensionId673551207")
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbEdgeExtension response = depServiceClient.createLbEdgeExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbEdgeExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbEdgeExtensionAsync(String parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId)
    
    
    public final OperationFuture<LbEdgeExtension,OperationMetadata> createLbEdgeExtensionAsync(String parent, LbEdgeExtension lbEdgeExtension, String lbEdgeExtensionId)

Creates a new `LbEdgeExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       LbEdgeExtension lbEdgeExtension = LbEdgeExtension.newBuilder().build();
       String lbEdgeExtensionId = "lbEdgeExtensionId673551207";
       LbEdgeExtension response =
           depServiceClient
               .createLbEdgeExtensionAsync(parent, lbEdgeExtension, lbEdgeExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `LbEdgeExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbEdgeExtension` | `[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)`  
Required. `LbEdgeExtension` resource to be created.  
`lbEdgeExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbEdgeExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbEdgeExtensionCallable()
    
    
    public final UnaryCallable<CreateLbEdgeExtensionRequest,Operation> createLbEdgeExtensionCallable()

Creates a new `LbEdgeExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbEdgeExtensionRequest request =
           CreateLbEdgeExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbEdgeExtensionId("lbEdgeExtensionId673551207")
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.createLbEdgeExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbEdgeExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLbEdgeExtensionOperationCallable()
    
    
    public final OperationCallable<CreateLbEdgeExtensionRequest,LbEdgeExtension,OperationMetadata> createLbEdgeExtensionOperationCallable()

Creates a new `LbEdgeExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbEdgeExtensionRequest request =
           CreateLbEdgeExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbEdgeExtensionId("lbEdgeExtensionId673551207")
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbEdgeExtension, OperationMetadata> future =
           depServiceClient.createLbEdgeExtensionOperationCallable().futureCall(request);
       // Do something.
       LbEdgeExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbEdgeExtensionRequest),[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbRouteExtensionAsync(@Nullable LocationName parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId)
    
    
    public final OperationFuture<LbRouteExtension,OperationMetadata> createLbRouteExtensionAsync(@Nullable LocationName parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId)

Creates a new `LbRouteExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       LbRouteExtension lbRouteExtension = LbRouteExtension.newBuilder().build();
       String lbRouteExtensionId = "lbRouteExtensionId-1336830649";
       LbRouteExtension response =
           depServiceClient
               .createLbRouteExtensionAsync(parent, lbRouteExtension, lbRouteExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the `LbRouteExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)`  
Required. `LbRouteExtension` resource to be created.  
`lbRouteExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbRouteExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbRouteExtensionAsync(CreateLbRouteExtensionRequest request)
    
    
    public final OperationFuture<LbRouteExtension,OperationMetadata> createLbRouteExtensionAsync(CreateLbRouteExtensionRequest request)

Creates a new `LbRouteExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbRouteExtensionRequest request =
           CreateLbRouteExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbRouteExtensionId("lbRouteExtensionId-1336830649")
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbRouteExtension response = depServiceClient.createLbRouteExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbRouteExtensionAsync(String parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId)
    
    
    public final OperationFuture<LbRouteExtension,OperationMetadata> createLbRouteExtensionAsync(String parent, LbRouteExtension lbRouteExtension, String lbRouteExtensionId)

Creates a new `LbRouteExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       LbRouteExtension lbRouteExtension = LbRouteExtension.newBuilder().build();
       String lbRouteExtensionId = "lbRouteExtensionId-1336830649";
       LbRouteExtension response =
           depServiceClient
               .createLbRouteExtensionAsync(parent, lbRouteExtension, lbRouteExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `LbRouteExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)`  
Required. `LbRouteExtension` resource to be created.  
`lbRouteExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbRouteExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbRouteExtensionCallable()
    
    
    public final UnaryCallable<CreateLbRouteExtensionRequest,Operation> createLbRouteExtensionCallable()

Creates a new `LbRouteExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbRouteExtensionRequest request =
           CreateLbRouteExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbRouteExtensionId("lbRouteExtensionId-1336830649")
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.createLbRouteExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLbRouteExtensionOperationCallable()
    
    
    public final OperationCallable<CreateLbRouteExtensionRequest,LbRouteExtension,OperationMetadata> createLbRouteExtensionOperationCallable()

Creates a new `LbRouteExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbRouteExtensionRequest request =
           CreateLbRouteExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbRouteExtensionId("lbRouteExtensionId-1336830649")
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbRouteExtension, OperationMetadata> future =
           depServiceClient.createLbRouteExtensionOperationCallable().futureCall(request);
       // Do something.
       LbRouteExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbTrafficExtensionAsync(@Nullable LocationName parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId)
    
    
    public final OperationFuture<LbTrafficExtension,OperationMetadata> createLbTrafficExtensionAsync(@Nullable LocationName parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId)

Creates a new `LbTrafficExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       LbTrafficExtension lbTrafficExtension = LbTrafficExtension.newBuilder().build();
       String lbTrafficExtensionId = "lbTrafficExtensionId1150549907";
       LbTrafficExtension response =
           depServiceClient
               .createLbTrafficExtensionAsync(parent, lbTrafficExtension, lbTrafficExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The parent resource of the `LbTrafficExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource to be created.  
`lbTrafficExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbTrafficExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbTrafficExtensionAsync(CreateLbTrafficExtensionRequest request)
    
    
    public final OperationFuture<LbTrafficExtension,OperationMetadata> createLbTrafficExtensionAsync(CreateLbTrafficExtensionRequest request)

Creates a new `LbTrafficExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbTrafficExtensionRequest request =
           CreateLbTrafficExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbTrafficExtensionId("lbTrafficExtensionId1150549907")
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbTrafficExtension response = depServiceClient.createLbTrafficExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbTrafficExtensionAsync(String parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId)
    
    
    public final OperationFuture<LbTrafficExtension,OperationMetadata> createLbTrafficExtensionAsync(String parent, LbTrafficExtension lbTrafficExtension, String lbTrafficExtensionId)

Creates a new `LbTrafficExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       LbTrafficExtension lbTrafficExtension = LbTrafficExtension.newBuilder().build();
       String lbTrafficExtensionId = "lbTrafficExtensionId1150549907";
       LbTrafficExtension response =
           depServiceClient
               .createLbTrafficExtensionAsync(parent, lbTrafficExtension, lbTrafficExtensionId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `LbTrafficExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource to be created.  
`lbTrafficExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbTrafficExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createLbTrafficExtensionCallable()
    
    
    public final UnaryCallable<CreateLbTrafficExtensionRequest,Operation> createLbTrafficExtensionCallable()

Creates a new `LbTrafficExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbTrafficExtensionRequest request =
           CreateLbTrafficExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbTrafficExtensionId("lbTrafficExtensionId1150549907")
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.createLbTrafficExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLbTrafficExtensionOperationCallable()
    
    
    public final OperationCallable<CreateLbTrafficExtensionRequest,LbTrafficExtension,OperationMetadata> createLbTrafficExtensionOperationCallable()

Creates a new `LbTrafficExtension` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateLbTrafficExtensionRequest request =
           CreateLbTrafficExtensionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLbTrafficExtensionId("lbTrafficExtensionId1150549907")
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbTrafficExtension, OperationMetadata> future =
           depServiceClient.createLbTrafficExtensionOperationCallable().futureCall(request);
       // Do something.
       LbTrafficExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAuthzExtensionAsync(@Nullable AuthzExtensionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzExtensionAsync(@Nullable AuthzExtensionName name)

Deletes the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       AuthzExtensionName name =
           AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]");
       depServiceClient.deleteAuthzExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.AuthzExtensionName`  
Required. The name of the `AuthzExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAuthzExtensionAsync(DeleteAuthzExtensionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzExtensionAsync(DeleteAuthzExtensionRequest request)

Deletes the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteAuthzExtensionRequest request =
           DeleteAuthzExtensionRequest.newBuilder()
               .setName(
                   AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString())
               .setRequestId("requestId693933066")
               .build();
       depServiceClient.deleteAuthzExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAuthzExtensionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthzExtensionAsync(String name)

Deletes the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString();
       depServiceClient.deleteAuthzExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `AuthzExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAuthzExtensionCallable()
    
    
    public final UnaryCallable<DeleteAuthzExtensionRequest,Operation> deleteAuthzExtensionCallable()

Deletes the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteAuthzExtensionRequest request =
           DeleteAuthzExtensionRequest.newBuilder()
               .setName(
                   AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.deleteAuthzExtensionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAuthzExtensionOperationCallable()
    
    
    public final OperationCallable<DeleteAuthzExtensionRequest,Empty,OperationMetadata> deleteAuthzExtensionOperationCallable()

Deletes the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteAuthzExtensionRequest request =
           DeleteAuthzExtensionRequest.newBuilder()
               .setName(
                   AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           depServiceClient.deleteAuthzExtensionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbEdgeExtensionAsync(@Nullable LbEdgeExtensionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbEdgeExtensionAsync(@Nullable LbEdgeExtensionName name)

Deletes the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbEdgeExtensionName name =
           LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]");
       depServiceClient.deleteLbEdgeExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbEdgeExtensionName`  
Required. The name of the `LbEdgeExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbEdgeExtensionAsync(DeleteLbEdgeExtensionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbEdgeExtensionAsync(DeleteLbEdgeExtensionRequest request)

Deletes the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbEdgeExtensionRequest request =
           DeleteLbEdgeExtensionRequest.newBuilder()
               .setName(
                   LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       depServiceClient.deleteLbEdgeExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbEdgeExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbEdgeExtensionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbEdgeExtensionAsync(String name)

Deletes the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]").toString();
       depServiceClient.deleteLbEdgeExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `LbEdgeExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbEdgeExtensionCallable()
    
    
    public final UnaryCallable<DeleteLbEdgeExtensionRequest,Operation> deleteLbEdgeExtensionCallable()

Deletes the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbEdgeExtensionRequest request =
           DeleteLbEdgeExtensionRequest.newBuilder()
               .setName(
                   LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.deleteLbEdgeExtensionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbEdgeExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLbEdgeExtensionOperationCallable()
    
    
    public final OperationCallable<DeleteLbEdgeExtensionRequest,Empty,OperationMetadata> deleteLbEdgeExtensionOperationCallable()

Deletes the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbEdgeExtensionRequest request =
           DeleteLbEdgeExtensionRequest.newBuilder()
               .setName(
                   LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           depServiceClient.deleteLbEdgeExtensionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbEdgeExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbRouteExtensionAsync(@Nullable LbRouteExtensionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbRouteExtensionAsync(@Nullable LbRouteExtensionName name)

Deletes the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbRouteExtensionName name =
           LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]");
       depServiceClient.deleteLbRouteExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbRouteExtensionName`  
Required. The name of the `LbRouteExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbRouteExtensionAsync(DeleteLbRouteExtensionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbRouteExtensionAsync(DeleteLbRouteExtensionRequest request)

Deletes the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbRouteExtensionRequest request =
           DeleteLbRouteExtensionRequest.newBuilder()
               .setName(
                   LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       depServiceClient.deleteLbRouteExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbRouteExtensionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbRouteExtensionAsync(String name)

Deletes the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]").toString();
       depServiceClient.deleteLbRouteExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `LbRouteExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbRouteExtensionCallable()
    
    
    public final UnaryCallable<DeleteLbRouteExtensionRequest,Operation> deleteLbRouteExtensionCallable()

Deletes the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbRouteExtensionRequest request =
           DeleteLbRouteExtensionRequest.newBuilder()
               .setName(
                   LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.deleteLbRouteExtensionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLbRouteExtensionOperationCallable()
    
    
    public final OperationCallable<DeleteLbRouteExtensionRequest,Empty,OperationMetadata> deleteLbRouteExtensionOperationCallable()

Deletes the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbRouteExtensionRequest request =
           DeleteLbRouteExtensionRequest.newBuilder()
               .setName(
                   LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           depServiceClient.deleteLbRouteExtensionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbRouteExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbTrafficExtensionAsync(@Nullable LbTrafficExtensionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbTrafficExtensionAsync(@Nullable LbTrafficExtensionName name)

Deletes the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbTrafficExtensionName name =
           LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]");
       depServiceClient.deleteLbTrafficExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbTrafficExtensionName`  
Required. The name of the `LbTrafficExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbTrafficExtensionAsync(DeleteLbTrafficExtensionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbTrafficExtensionAsync(DeleteLbTrafficExtensionRequest request)

Deletes the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbTrafficExtensionRequest request =
           DeleteLbTrafficExtensionRequest.newBuilder()
               .setName(
                   LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       depServiceClient.deleteLbTrafficExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbTrafficExtensionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLbTrafficExtensionAsync(String name)

Deletes the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]").toString();
       depServiceClient.deleteLbTrafficExtensionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `LbTrafficExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteLbTrafficExtensionCallable()
    
    
    public final UnaryCallable<DeleteLbTrafficExtensionRequest,Operation> deleteLbTrafficExtensionCallable()

Deletes the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbTrafficExtensionRequest request =
           DeleteLbTrafficExtensionRequest.newBuilder()
               .setName(
                   LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.deleteLbTrafficExtensionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLbTrafficExtensionOperationCallable()
    
    
    public final OperationCallable<DeleteLbTrafficExtensionRequest,Empty,OperationMetadata> deleteLbTrafficExtensionOperationCallable()

Deletes the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteLbTrafficExtensionRequest request =
           DeleteLbTrafficExtensionRequest.newBuilder()
               .setName(
                   LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           depServiceClient.deleteLbTrafficExtensionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteLbTrafficExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### getAuthzExtension(@Nullable AuthzExtensionName name)
    
    
    public final AuthzExtension getAuthzExtension(@Nullable AuthzExtensionName name)

Gets details of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       AuthzExtensionName name =
           AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]");
       AuthzExtension response = depServiceClient.getAuthzExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.AuthzExtensionName`  
Required. A name of the `AuthzExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)` |   
  
### getAuthzExtension(GetAuthzExtensionRequest request)
    
    
    public final AuthzExtension getAuthzExtension(GetAuthzExtensionRequest request)

Gets details of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetAuthzExtensionRequest request =
           GetAuthzExtensionRequest.newBuilder()
               .setName(
                   AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString())
               .build();
       AuthzExtension response = depServiceClient.getAuthzExtension(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAuthzExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)` |   
  
### getAuthzExtension(String name)
    
    
    public final AuthzExtension getAuthzExtension(String name)

Gets details of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString();
       AuthzExtension response = depServiceClient.getAuthzExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `AuthzExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/authzExtensions/{authz_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)` |   
  
### getAuthzExtensionCallable()
    
    
    public final UnaryCallable<GetAuthzExtensionRequest,AuthzExtension> getAuthzExtensionCallable()

Gets details of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetAuthzExtensionRequest request =
           GetAuthzExtensionRequest.newBuilder()
               .setName(
                   AuthzExtensionName.of("[PROJECT]", "[LOCATION]", "[AUTHZ_EXTENSION]").toString())
               .build();
       ApiFuture<AuthzExtension> future =
           depServiceClient.getAuthzExtensionCallable().futureCall(request);
       // Do something.
       AuthzExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAuthzExtensionRequest),[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = depServiceClient.getIamPolicy(request);
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = depServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLbEdgeExtension(@Nullable LbEdgeExtensionName name)
    
    
    public final LbEdgeExtension getLbEdgeExtension(@Nullable LbEdgeExtensionName name)

Gets details of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbEdgeExtensionName name =
           LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]");
       LbEdgeExtension response = depServiceClient.getLbEdgeExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbEdgeExtensionName`  
Required. A name of the `LbEdgeExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)` |   
  
### getLbEdgeExtension(GetLbEdgeExtensionRequest request)
    
    
    public final LbEdgeExtension getLbEdgeExtension(GetLbEdgeExtensionRequest request)

Gets details of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbEdgeExtensionRequest request =
           GetLbEdgeExtensionRequest.newBuilder()
               .setName(
                   LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]")
                       .toString())
               .build();
       LbEdgeExtension response = depServiceClient.getLbEdgeExtension(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbEdgeExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)` |   
  
### getLbEdgeExtension(String name)
    
    
    public final LbEdgeExtension getLbEdgeExtension(String name)

Gets details of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]").toString();
       LbEdgeExtension response = depServiceClient.getLbEdgeExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `LbEdgeExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)` |   
  
### getLbEdgeExtensionCallable()
    
    
    public final UnaryCallable<GetLbEdgeExtensionRequest,LbEdgeExtension> getLbEdgeExtensionCallable()

Gets details of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbEdgeExtensionRequest request =
           GetLbEdgeExtensionRequest.newBuilder()
               .setName(
                   LbEdgeExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_EDGE_EXTENSION]")
                       .toString())
               .build();
       ApiFuture<LbEdgeExtension> future =
           depServiceClient.getLbEdgeExtensionCallable().futureCall(request);
       // Do something.
       LbEdgeExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbEdgeExtensionRequest),[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)>` |   
  
### getLbRouteExtension(@Nullable LbRouteExtensionName name)
    
    
    public final LbRouteExtension getLbRouteExtension(@Nullable LbRouteExtensionName name)

Gets details of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbRouteExtensionName name =
           LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]");
       LbRouteExtension response = depServiceClient.getLbRouteExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbRouteExtensionName`  
Required. A name of the `LbRouteExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)` |   
  
### getLbRouteExtension(GetLbRouteExtensionRequest request)
    
    
    public final LbRouteExtension getLbRouteExtension(GetLbRouteExtensionRequest request)

Gets details of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbRouteExtensionRequest request =
           GetLbRouteExtensionRequest.newBuilder()
               .setName(
                   LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]")
                       .toString())
               .build();
       LbRouteExtension response = depServiceClient.getLbRouteExtension(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)` |   
  
### getLbRouteExtension(String name)
    
    
    public final LbRouteExtension getLbRouteExtension(String name)

Gets details of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]").toString();
       LbRouteExtension response = depServiceClient.getLbRouteExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `LbRouteExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)` |   
  
### getLbRouteExtensionCallable()
    
    
    public final UnaryCallable<GetLbRouteExtensionRequest,LbRouteExtension> getLbRouteExtensionCallable()

Gets details of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbRouteExtensionRequest request =
           GetLbRouteExtensionRequest.newBuilder()
               .setName(
                   LbRouteExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_ROUTE_EXTENSION]")
                       .toString())
               .build();
       ApiFuture<LbRouteExtension> future =
           depServiceClient.getLbRouteExtensionCallable().futureCall(request);
       // Do something.
       LbRouteExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)>` |   
  
### getLbTrafficExtension(@Nullable LbTrafficExtensionName name)
    
    
    public final LbTrafficExtension getLbTrafficExtension(@Nullable LbTrafficExtensionName name)

Gets details of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbTrafficExtensionName name =
           LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]");
       LbTrafficExtension response = depServiceClient.getLbTrafficExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LbTrafficExtensionName`  
Required. A name of the `LbTrafficExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)` |   
  
### getLbTrafficExtension(GetLbTrafficExtensionRequest request)
    
    
    public final LbTrafficExtension getLbTrafficExtension(GetLbTrafficExtensionRequest request)

Gets details of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbTrafficExtensionRequest request =
           GetLbTrafficExtensionRequest.newBuilder()
               .setName(
                   LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]")
                       .toString())
               .build();
       LbTrafficExtension response = depServiceClient.getLbTrafficExtension(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)` |   
  
### getLbTrafficExtension(String name)
    
    
    public final LbTrafficExtension getLbTrafficExtension(String name)

Gets details of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]").toString();
       LbTrafficExtension response = depServiceClient.getLbTrafficExtension(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `LbTrafficExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)` |   
  
### getLbTrafficExtensionCallable()
    
    
    public final UnaryCallable<GetLbTrafficExtensionRequest,LbTrafficExtension> getLbTrafficExtensionCallable()

Gets details of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLbTrafficExtensionRequest request =
           GetLbTrafficExtensionRequest.newBuilder()
               .setName(
                   LbTrafficExtensionName.of("[PROJECT]", "[LOCATION]", "[LB_TRAFFIC_EXTENSION]")
                       .toString())
               .build();
       ApiFuture<LbTrafficExtension> future =
           depServiceClient.getLbTrafficExtensionCallable().futureCall(request);
       // Do something.
       LbTrafficExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = depServiceClient.getLocation(request);
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = depServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable DepServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.DepServiceSettings` |   
  
### getStub()
    
    
    public DepServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.DepServiceStub)` |   
  
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
  
### listAuthzExtensions(@Nullable LocationName parent)
    
    
    public final DepServiceClient.ListAuthzExtensionsPagedResponse listAuthzExtensions(@Nullable LocationName parent)

Lists `AuthzExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AuthzExtension element : depServiceClient.listAuthzExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the `AuthzExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListAuthzExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListAuthzExtensionsPagedResponse)` |   
  
### listAuthzExtensions(ListAuthzExtensionsRequest request)
    
    
    public final DepServiceClient.ListAuthzExtensionsPagedResponse listAuthzExtensions(ListAuthzExtensionsRequest request)

Lists `AuthzExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListAuthzExtensionsRequest request =
           ListAuthzExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AuthzExtension element : depServiceClient.listAuthzExtensions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthzExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAuthzExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListAuthzExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListAuthzExtensionsPagedResponse)` |   
  
### listAuthzExtensions(String parent)
    
    
    public final DepServiceClient.ListAuthzExtensionsPagedResponse listAuthzExtensions(String parent)

Lists `AuthzExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AuthzExtension element : depServiceClient.listAuthzExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `AuthzExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListAuthzExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListAuthzExtensionsPagedResponse)` |   
  
### listAuthzExtensionsCallable()
    
    
    public final UnaryCallable<ListAuthzExtensionsRequest,ListAuthzExtensionsResponse> listAuthzExtensionsCallable()

Lists `AuthzExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListAuthzExtensionsRequest request =
           ListAuthzExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAuthzExtensionsResponse response =
             depServiceClient.listAuthzExtensionsCallable().call(request);
         for (AuthzExtension element : response.getAuthzExtensionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthzExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAuthzExtensionsRequest),[ListAuthzExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAuthzExtensionsResponse)>` |   
  
### listAuthzExtensionsPagedCallable()
    
    
    public final UnaryCallable<ListAuthzExtensionsRequest,DepServiceClient.ListAuthzExtensionsPagedResponse> listAuthzExtensionsPagedCallable()

Lists `AuthzExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListAuthzExtensionsRequest request =
           ListAuthzExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AuthzExtension> future =
           depServiceClient.listAuthzExtensionsPagedCallable().futureCall(request);
       // Do something.
       for (AuthzExtension element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthzExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAuthzExtensionsRequest),[ListAuthzExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListAuthzExtensionsPagedResponse)>` |   
  
### listLbEdgeExtensions(@Nullable LocationName parent)
    
    
    public final DepServiceClient.ListLbEdgeExtensionsPagedResponse listLbEdgeExtensions(@Nullable LocationName parent)

Lists `LbEdgeExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (LbEdgeExtension element : depServiceClient.listLbEdgeExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the `LbEdgeExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbEdgeExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbEdgeExtensionsPagedResponse)` |   
  
### listLbEdgeExtensions(ListLbEdgeExtensionsRequest request)
    
    
    public final DepServiceClient.ListLbEdgeExtensionsPagedResponse listLbEdgeExtensions(ListLbEdgeExtensionsRequest request)

Lists `LbEdgeExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbEdgeExtensionsRequest request =
           ListLbEdgeExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (LbEdgeExtension element : depServiceClient.listLbEdgeExtensions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLbEdgeExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbEdgeExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbEdgeExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbEdgeExtensionsPagedResponse)` |   
  
### listLbEdgeExtensions(String parent)
    
    
    public final DepServiceClient.ListLbEdgeExtensionsPagedResponse listLbEdgeExtensions(String parent)

Lists `LbEdgeExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (LbEdgeExtension element : depServiceClient.listLbEdgeExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `LbEdgeExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbEdgeExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbEdgeExtensionsPagedResponse)` |   
  
### listLbEdgeExtensionsCallable()
    
    
    public final UnaryCallable<ListLbEdgeExtensionsRequest,ListLbEdgeExtensionsResponse> listLbEdgeExtensionsCallable()

Lists `LbEdgeExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbEdgeExtensionsRequest request =
           ListLbEdgeExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLbEdgeExtensionsResponse response =
             depServiceClient.listLbEdgeExtensionsCallable().call(request);
         for (LbEdgeExtension element : response.getLbEdgeExtensionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbEdgeExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbEdgeExtensionsRequest),[ListLbEdgeExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbEdgeExtensionsResponse)>` |   
  
### listLbEdgeExtensionsPagedCallable()
    
    
    public final UnaryCallable<ListLbEdgeExtensionsRequest,DepServiceClient.ListLbEdgeExtensionsPagedResponse> listLbEdgeExtensionsPagedCallable()

Lists `LbEdgeExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbEdgeExtensionsRequest request =
           ListLbEdgeExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<LbEdgeExtension> future =
           depServiceClient.listLbEdgeExtensionsPagedCallable().futureCall(request);
       // Do something.
       for (LbEdgeExtension element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbEdgeExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbEdgeExtensionsRequest),[ListLbEdgeExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbEdgeExtensionsPagedResponse)>` |   
  
### listLbRouteExtensions(@Nullable LocationName parent)
    
    
    public final DepServiceClient.ListLbRouteExtensionsPagedResponse listLbRouteExtensions(@Nullable LocationName parent)

Lists `LbRouteExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (LbRouteExtension element : depServiceClient.listLbRouteExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the `LbRouteExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
### listLbRouteExtensions(ListLbRouteExtensionsRequest request)
    
    
    public final DepServiceClient.ListLbRouteExtensionsPagedResponse listLbRouteExtensions(ListLbRouteExtensionsRequest request)

Lists `LbRouteExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbRouteExtensionsRequest request =
           ListLbRouteExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (LbRouteExtension element :
           depServiceClient.listLbRouteExtensions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
### listLbRouteExtensions(String parent)
    
    
    public final DepServiceClient.ListLbRouteExtensionsPagedResponse listLbRouteExtensions(String parent)

Lists `LbRouteExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (LbRouteExtension element : depServiceClient.listLbRouteExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `LbRouteExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
### listLbRouteExtensionsCallable()
    
    
    public final UnaryCallable<ListLbRouteExtensionsRequest,ListLbRouteExtensionsResponse> listLbRouteExtensionsCallable()

Lists `LbRouteExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbRouteExtensionsRequest request =
           ListLbRouteExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLbRouteExtensionsResponse response =
             depServiceClient.listLbRouteExtensionsCallable().call(request);
         for (LbRouteExtension element : response.getLbRouteExtensionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest),[ListLbRouteExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbRouteExtensionsResponse)>` |   
  
### listLbRouteExtensionsPagedCallable()
    
    
    public final UnaryCallable<ListLbRouteExtensionsRequest,DepServiceClient.ListLbRouteExtensionsPagedResponse> listLbRouteExtensionsPagedCallable()

Lists `LbRouteExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbRouteExtensionsRequest request =
           ListLbRouteExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<LbRouteExtension> future =
           depServiceClient.listLbRouteExtensionsPagedCallable().futureCall(request);
       // Do something.
       for (LbRouteExtension element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbRouteExtensionsRequest),[ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbRouteExtensionsPagedResponse)>` |   
  
### listLbTrafficExtensions(@Nullable LocationName parent)
    
    
    public final DepServiceClient.ListLbTrafficExtensionsPagedResponse listLbTrafficExtensions(@Nullable LocationName parent)

Lists `LbTrafficExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (LbTrafficExtension element :
           depServiceClient.listLbTrafficExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1.LocationName`  
Required. The project and location from which the `LbTrafficExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
### listLbTrafficExtensions(ListLbTrafficExtensionsRequest request)
    
    
    public final DepServiceClient.ListLbTrafficExtensionsPagedResponse listLbTrafficExtensions(ListLbTrafficExtensionsRequest request)

Lists `LbTrafficExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbTrafficExtensionsRequest request =
           ListLbTrafficExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (LbTrafficExtension element :
           depServiceClient.listLbTrafficExtensions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
### listLbTrafficExtensions(String parent)
    
    
    public final DepServiceClient.ListLbTrafficExtensionsPagedResponse listLbTrafficExtensions(String parent)

Lists `LbTrafficExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (LbTrafficExtension element :
           depServiceClient.listLbTrafficExtensions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `LbTrafficExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
### listLbTrafficExtensionsCallable()
    
    
    public final UnaryCallable<ListLbTrafficExtensionsRequest,ListLbTrafficExtensionsResponse> listLbTrafficExtensionsCallable()

Lists `LbTrafficExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbTrafficExtensionsRequest request =
           ListLbTrafficExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLbTrafficExtensionsResponse response =
             depServiceClient.listLbTrafficExtensionsCallable().call(request);
         for (LbTrafficExtension element : response.getLbTrafficExtensionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest),[ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbTrafficExtensionsResponse)>` |   
  
### listLbTrafficExtensionsPagedCallable()
    
    
    public final UnaryCallable<ListLbTrafficExtensionsRequest,DepServiceClient.ListLbTrafficExtensionsPagedResponse> listLbTrafficExtensionsPagedCallable()

Lists `LbTrafficExtension` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLbTrafficExtensionsRequest request =
           ListLbTrafficExtensionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<LbTrafficExtension> future =
           depServiceClient.listLbTrafficExtensionsPagedCallable().futureCall(request);
       // Do something.
       for (LbTrafficExtension element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListLbTrafficExtensionsRequest),[ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DepServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : depServiceClient.listLocations(request).iterateAll()) {
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
`[DepServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = depServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DepServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           depServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DepServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = depServiceClient.setIamPolicy(request);
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = depServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = depServiceClient.testIamPermissions(request);
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
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointPolicyName.of("[PROJECT]", "[LOCATION]", "[ENDPOINT_POLICY]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           depServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAuthzExtensionAsync(AuthzExtension authzExtension, FieldMask updateMask)
    
    
    public final OperationFuture<AuthzExtension,OperationMetadata> updateAuthzExtensionAsync(AuthzExtension authzExtension, FieldMask updateMask)

Updates the parameters of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       AuthzExtension authzExtension = AuthzExtension.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AuthzExtension response =
           depServiceClient.updateAuthzExtensionAsync(authzExtension, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`authzExtension` | `[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension)`  
Required. `AuthzExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Used to specify the fields to be overwritten in the `AuthzExtension` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateAuthzExtensionAsync(UpdateAuthzExtensionRequest request)
    
    
    public final OperationFuture<AuthzExtension,OperationMetadata> updateAuthzExtensionAsync(UpdateAuthzExtensionRequest request)

Updates the parameters of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateAuthzExtensionRequest request =
           UpdateAuthzExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthzExtension response = depServiceClient.updateAuthzExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAuthzExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateAuthzExtensionCallable()
    
    
    public final UnaryCallable<UpdateAuthzExtensionRequest,Operation> updateAuthzExtensionCallable()

Updates the parameters of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateAuthzExtensionRequest request =
           UpdateAuthzExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.updateAuthzExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAuthzExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAuthzExtensionOperationCallable()
    
    
    public final OperationCallable<UpdateAuthzExtensionRequest,AuthzExtension,OperationMetadata> updateAuthzExtensionOperationCallable()

Updates the parameters of the specified `AuthzExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateAuthzExtensionRequest request =
           UpdateAuthzExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthzExtension(AuthzExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<AuthzExtension, OperationMetadata> future =
           depServiceClient.updateAuthzExtensionOperationCallable().futureCall(request);
       // Do something.
       AuthzExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAuthzExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAuthzExtensionRequest),[AuthzExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AuthzExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbEdgeExtensionAsync(LbEdgeExtension lbEdgeExtension, FieldMask updateMask)
    
    
    public final OperationFuture<LbEdgeExtension,OperationMetadata> updateLbEdgeExtensionAsync(LbEdgeExtension lbEdgeExtension, FieldMask updateMask)

Updates the parameters of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbEdgeExtension lbEdgeExtension = LbEdgeExtension.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LbEdgeExtension response =
           depServiceClient.updateLbEdgeExtensionAsync(lbEdgeExtension, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`lbEdgeExtension` | `[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension)`  
Required. `LbEdgeExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Used to specify the fields to be overwritten in the `LbEdgeExtension` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbEdgeExtensionAsync(UpdateLbEdgeExtensionRequest request)
    
    
    public final OperationFuture<LbEdgeExtension,OperationMetadata> updateLbEdgeExtensionAsync(UpdateLbEdgeExtensionRequest request)

Updates the parameters of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbEdgeExtensionRequest request =
           UpdateLbEdgeExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbEdgeExtension response = depServiceClient.updateLbEdgeExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbEdgeExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbEdgeExtensionCallable()
    
    
    public final UnaryCallable<UpdateLbEdgeExtensionRequest,Operation> updateLbEdgeExtensionCallable()

Updates the parameters of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbEdgeExtensionRequest request =
           UpdateLbEdgeExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.updateLbEdgeExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbEdgeExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLbEdgeExtensionOperationCallable()
    
    
    public final OperationCallable<UpdateLbEdgeExtensionRequest,LbEdgeExtension,OperationMetadata> updateLbEdgeExtensionOperationCallable()

Updates the parameters of the specified `LbEdgeExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbEdgeExtensionRequest request =
           UpdateLbEdgeExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbEdgeExtension(LbEdgeExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbEdgeExtension, OperationMetadata> future =
           depServiceClient.updateLbEdgeExtensionOperationCallable().futureCall(request);
       // Do something.
       LbEdgeExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLbEdgeExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbEdgeExtensionRequest),[LbEdgeExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbEdgeExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbRouteExtensionAsync(LbRouteExtension lbRouteExtension, FieldMask updateMask)
    
    
    public final OperationFuture<LbRouteExtension,OperationMetadata> updateLbRouteExtensionAsync(LbRouteExtension lbRouteExtension, FieldMask updateMask)

Updates the parameters of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbRouteExtension lbRouteExtension = LbRouteExtension.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LbRouteExtension response =
           depServiceClient.updateLbRouteExtensionAsync(lbRouteExtension, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension)`  
Required. `LbRouteExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Used to specify the fields to be overwritten in the `LbRouteExtension` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbRouteExtensionAsync(UpdateLbRouteExtensionRequest request)
    
    
    public final OperationFuture<LbRouteExtension,OperationMetadata> updateLbRouteExtensionAsync(UpdateLbRouteExtensionRequest request)

Updates the parameters of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbRouteExtensionRequest request =
           UpdateLbRouteExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbRouteExtension response = depServiceClient.updateLbRouteExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbRouteExtensionCallable()
    
    
    public final UnaryCallable<UpdateLbRouteExtensionRequest,Operation> updateLbRouteExtensionCallable()

Updates the parameters of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbRouteExtensionRequest request =
           UpdateLbRouteExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.updateLbRouteExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLbRouteExtensionOperationCallable()
    
    
    public final OperationCallable<UpdateLbRouteExtensionRequest,LbRouteExtension,OperationMetadata> updateLbRouteExtensionOperationCallable()

Updates the parameters of the specified `LbRouteExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbRouteExtensionRequest request =
           UpdateLbRouteExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbRouteExtension(LbRouteExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbRouteExtension, OperationMetadata> future =
           depServiceClient.updateLbRouteExtensionOperationCallable().futureCall(request);
       // Do something.
       LbRouteExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbTrafficExtensionAsync(LbTrafficExtension lbTrafficExtension, FieldMask updateMask)
    
    
    public final OperationFuture<LbTrafficExtension,OperationMetadata> updateLbTrafficExtensionAsync(LbTrafficExtension lbTrafficExtension, FieldMask updateMask)

Updates the parameters of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LbTrafficExtension lbTrafficExtension = LbTrafficExtension.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LbTrafficExtension response =
           depServiceClient.updateLbTrafficExtensionAsync(lbTrafficExtension, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Used to specify the fields to be overwritten in the `LbTrafficExtension` resource by the update. The fields specified in the `update_mask` are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbTrafficExtensionAsync(UpdateLbTrafficExtensionRequest request)
    
    
    public final OperationFuture<LbTrafficExtension,OperationMetadata> updateLbTrafficExtensionAsync(UpdateLbTrafficExtensionRequest request)

Updates the parameters of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbTrafficExtensionRequest request =
           UpdateLbTrafficExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LbTrafficExtension response = depServiceClient.updateLbTrafficExtensionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateLbTrafficExtensionCallable()
    
    
    public final UnaryCallable<UpdateLbTrafficExtensionRequest,Operation> updateLbTrafficExtensionCallable()

Updates the parameters of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbTrafficExtensionRequest request =
           UpdateLbTrafficExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.updateLbTrafficExtensionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLbTrafficExtensionOperationCallable()
    
    
    public final OperationCallable<UpdateLbTrafficExtensionRequest,LbTrafficExtension,OperationMetadata> updateLbTrafficExtensionOperationCallable()

Updates the parameters of the specified `LbTrafficExtension` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateLbTrafficExtensionRequest request =
           UpdateLbTrafficExtensionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLbTrafficExtension(LbTrafficExtension.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LbTrafficExtension, OperationMetadata> future =
           depServiceClient.updateLbTrafficExtensionOperationCallable().futureCall(request);
       // Do something.
       LbTrafficExtension response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
