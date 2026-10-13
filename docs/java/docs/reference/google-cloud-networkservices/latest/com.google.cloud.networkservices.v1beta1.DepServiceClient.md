---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient
title: Class DepServiceClient (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:06.632229+00:00
---

# Class DepServiceClient (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DepServiceClient (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkservices/google-cloud-networkservices/src/main/java/com/google/cloud/networkservices/v1beta1/DepServiceClient.java)| [Product Reference](https://cloud.google.com/products/networking)  
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

  
ListExtensionBindings |  Lists `ExtensionBinding` resources in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExtensionBindings(ListExtensionBindingsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExtensionBindings(LocationName parent) 
  * listExtensionBindings(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExtensionBindingsPagedCallable() 
  * listExtensionBindingsCallable() 

  
GetExtensionBinding |  Gets details of the specified `ExtensionBinding` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExtensionBinding(GetExtensionBindingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExtensionBinding(ExtensionBindingName name) 
  * getExtensionBinding(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExtensionBindingCallable() 

  
CreateExtensionBinding |  Creates a new `ExtensionBinding` resource in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createExtensionBindingAsync(CreateExtensionBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createExtensionBindingAsync(LocationName parent, ExtensionBinding extensionBinding, String extensionBindingId) 
  * createExtensionBindingAsync(String parent, ExtensionBinding extensionBinding, String extensionBindingId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createExtensionBindingOperationCallable() 
  * createExtensionBindingCallable() 

  
UpdateExtensionBinding |  Updates the parameters of the specified `ExtensionBinding` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateExtensionBindingAsync(UpdateExtensionBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateExtensionBindingAsync(ExtensionBinding extensionBinding, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateExtensionBindingOperationCallable() 
  * updateExtensionBindingCallable() 

  
DeleteExtensionBinding |  Deletes the specified `ExtensionBinding` resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExtensionBindingAsync(DeleteExtensionBindingRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExtensionBindingAsync(ExtensionBindingName name) 
  * deleteExtensionBindingAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExtensionBindingOperationCallable() 
  * deleteExtensionBindingCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient)` |   
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
`settings` | `[DepServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient)` |   
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
`stub` | `[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.stub.DepServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient)` |   
  
## Constructors 

### DepServiceClient(DepServiceSettings settings)
    
    
    protected DepServiceClient(DepServiceSettings settings)

Constructs an instance of DepServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DepServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceSettings)`  
  
  
### DepServiceClient(DepServiceStub stub)
    
    
    protected DepServiceClient(DepServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.stub.DepServiceStub)`  
  
  
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

### createExtensionBindingAsync(@Nullable LocationName parent, ExtensionBinding extensionBinding, String extensionBindingId)
    
    
    public final OperationFuture<ExtensionBinding,OperationMetadata> createExtensionBindingAsync(@Nullable LocationName parent, ExtensionBinding extensionBinding, String extensionBindingId)

Creates a new `ExtensionBinding` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ExtensionBinding extensionBinding = ExtensionBinding.newBuilder().build();
       String extensionBindingId = "extensionBindingId673350913";
       ExtensionBinding response =
           depServiceClient
               .createExtensionBindingAsync(parent, extensionBinding, extensionBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The parent resource of the `ExtensionBinding` resource. Must be in the format `projects/{project}/locations/{location}`.  
`extensionBinding` | `[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)`  
Required. `ExtensionBinding` resource to be created.  
`extensionBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the `ExtensionBinding` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### createExtensionBindingAsync(CreateExtensionBindingRequest request)
    
    
    public final OperationFuture<ExtensionBinding,OperationMetadata> createExtensionBindingAsync(CreateExtensionBindingRequest request)

Creates a new `ExtensionBinding` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateExtensionBindingRequest request =
           CreateExtensionBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExtensionBindingId("extensionBindingId673350913")
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       ExtensionBinding response = depServiceClient.createExtensionBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateExtensionBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### createExtensionBindingAsync(String parent, ExtensionBinding extensionBinding, String extensionBindingId)
    
    
    public final OperationFuture<ExtensionBinding,OperationMetadata> createExtensionBindingAsync(String parent, ExtensionBinding extensionBinding, String extensionBindingId)

Creates a new `ExtensionBinding` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ExtensionBinding extensionBinding = ExtensionBinding.newBuilder().build();
       String extensionBindingId = "extensionBindingId673350913";
       ExtensionBinding response =
           depServiceClient
               .createExtensionBindingAsync(parent, extensionBinding, extensionBindingId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource of the `ExtensionBinding` resource. Must be in the format `projects/{project}/locations/{location}`.  
`extensionBinding` | `[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)`  
Required. `ExtensionBinding` resource to be created.  
`extensionBindingId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Short name of the `ExtensionBinding` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### createExtensionBindingCallable()
    
    
    public final UnaryCallable<CreateExtensionBindingRequest,Operation> createExtensionBindingCallable()

Creates a new `ExtensionBinding` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateExtensionBindingRequest request =
           CreateExtensionBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExtensionBindingId("extensionBindingId673350913")
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           depServiceClient.createExtensionBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateExtensionBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExtensionBindingOperationCallable()
    
    
    public final OperationCallable<CreateExtensionBindingRequest,ExtensionBinding,OperationMetadata> createExtensionBindingOperationCallable()

Creates a new `ExtensionBinding` resource in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       CreateExtensionBindingRequest request =
           CreateExtensionBindingRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setExtensionBindingId("extensionBindingId673350913")
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       OperationFuture<ExtensionBinding, OperationMetadata> future =
           depServiceClient.createExtensionBindingOperationCallable().futureCall(request);
       // Do something.
       ExtensionBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateExtensionBindingRequest),[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The parent resource of the `LbRouteExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)`  
Required. `LbRouteExtension` resource to be created.  
`lbRouteExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbRouteExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)`  
Required. `LbRouteExtension` resource to be created.  
`lbRouteExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbRouteExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The parent resource of the `LbTrafficExtension` resource. Must be in the format `projects/{project}/locations/{location}`.  
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource to be created.  
`lbTrafficExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbTrafficExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource to be created.  
`lbTrafficExtensionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. User-provided ID of the `LbTrafficExtension` resource to be created.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.CreateLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### deleteExtensionBindingAsync(@Nullable ExtensionBindingName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExtensionBindingAsync(@Nullable ExtensionBindingName name)

Deletes the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ExtensionBindingName name =
           ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]");
       depServiceClient.deleteExtensionBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.ExtensionBindingName`  
Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### deleteExtensionBindingAsync(DeleteExtensionBindingRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExtensionBindingAsync(DeleteExtensionBindingRequest request)

Deletes the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteExtensionBindingRequest request =
           DeleteExtensionBindingRequest.newBuilder()
               .setName(
                   ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       depServiceClient.deleteExtensionBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### deleteExtensionBindingAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteExtensionBindingAsync(String name)

Deletes the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]").toString();
       depServiceClient.deleteExtensionBindingAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### deleteExtensionBindingCallable()
    
    
    public final UnaryCallable<DeleteExtensionBindingRequest,Operation> deleteExtensionBindingCallable()

Deletes the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteExtensionBindingRequest request =
           DeleteExtensionBindingRequest.newBuilder()
               .setName(
                   ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           depServiceClient.deleteExtensionBindingCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExtensionBindingOperationCallable()
    
    
    public final OperationCallable<DeleteExtensionBindingRequest,Empty,OperationMetadata> deleteExtensionBindingOperationCallable()

Deletes the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       DeleteExtensionBindingRequest request =
           DeleteExtensionBindingRequest.newBuilder()
               .setName(
                   ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           depServiceClient.deleteExtensionBindingOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteExtensionBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LbRouteExtensionName`  
Required. The name of the `LbRouteExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbRouteExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LbTrafficExtensionName`  
Required. The name of the `LbTrafficExtension` resource to delete. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DeleteLbTrafficExtensionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### getExtensionBinding(@Nullable ExtensionBindingName name)
    
    
    public final ExtensionBinding getExtensionBinding(@Nullable ExtensionBindingName name)

Gets details of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ExtensionBindingName name =
           ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]");
       ExtensionBinding response = depServiceClient.getExtensionBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.ExtensionBindingName`  
Required. A name of the `ExtensionBinding` resource to get. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)` |   
  
### getExtensionBinding(GetExtensionBindingRequest request)
    
    
    public final ExtensionBinding getExtensionBinding(GetExtensionBindingRequest request)

Gets details of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetExtensionBindingRequest request =
           GetExtensionBindingRequest.newBuilder()
               .setName(
                   ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]")
                       .toString())
               .build();
       ExtensionBinding response = depServiceClient.getExtensionBinding(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetExtensionBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)` |   
  
### getExtensionBinding(String name)
    
    
    public final ExtensionBinding getExtensionBinding(String name)

Gets details of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String name =
           ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]").toString();
       ExtensionBinding response = depServiceClient.getExtensionBinding(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the `ExtensionBinding` resource to get. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.  
**Returns**  
---  
**Type** | **Description**  
`[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)` |   
  
### getExtensionBindingCallable()
    
    
    public final UnaryCallable<GetExtensionBindingRequest,ExtensionBinding> getExtensionBindingCallable()

Gets details of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       GetExtensionBindingRequest request =
           GetExtensionBindingRequest.newBuilder()
               .setName(
                   ExtensionBindingName.of("[PROJECT]", "[LOCATION]", "[EXTENSION_BINDING]")
                       .toString())
               .build();
       ApiFuture<ExtensionBinding> future =
           depServiceClient.getExtensionBindingCallable().futureCall(request);
       // Do something.
       ExtensionBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetExtensionBindingRequest),[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)>` |   
  
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
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LbRouteExtensionName`  
Required. A name of the `LbRouteExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)` |   
  
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
`request` | `[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)` |   
  
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
`[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)>` |   
  
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
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LbTrafficExtensionName`  
Required. A name of the `LbTrafficExtension` resource to get. Must be in the format `projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}`.  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)` |   
  
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
`request` | `[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)` |   
  
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
`[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.GetLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)>` |   
  
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
`@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.DepServiceSettings` |   
  
### getStub()
    
    
    public DepServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DepServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.stub.DepServiceStub)` |   
  
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
  
### listExtensionBindings(@Nullable LocationName parent)
    
    
    public final DepServiceClient.ListExtensionBindingsPagedResponse listExtensionBindings(@Nullable LocationName parent)

Lists `ExtensionBinding` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ExtensionBinding element : depServiceClient.listExtensionBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The project and location from which the `ExtensionBinding` resources should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListExtensionBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListExtensionBindingsPagedResponse)` |   
  
### listExtensionBindings(ListExtensionBindingsRequest request)
    
    
    public final DepServiceClient.ListExtensionBindingsPagedResponse listExtensionBindings(ListExtensionBindingsRequest request)

Lists `ExtensionBinding` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListExtensionBindingsRequest request =
           ListExtensionBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ExtensionBinding element :
           depServiceClient.listExtensionBindings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExtensionBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListExtensionBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListExtensionBindingsPagedResponse)` |   
  
### listExtensionBindings(String parent)
    
    
    public final DepServiceClient.ListExtensionBindingsPagedResponse listExtensionBindings(String parent)

Lists `ExtensionBinding` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ExtensionBinding element : depServiceClient.listExtensionBindings(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location from which the `ExtensionBinding` resources should be listed, specified in the format `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListExtensionBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListExtensionBindingsPagedResponse)` |   
  
### listExtensionBindingsCallable()
    
    
    public final UnaryCallable<ListExtensionBindingsRequest,ListExtensionBindingsResponse> listExtensionBindingsCallable()

Lists `ExtensionBinding` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListExtensionBindingsRequest request =
           ListExtensionBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListExtensionBindingsResponse response =
             depServiceClient.listExtensionBindingsCallable().call(request);
         for (ExtensionBinding element : response.getExtensionBindingsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExtensionBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsRequest),[ListExtensionBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsResponse)>` |   
  
### listExtensionBindingsPagedCallable()
    
    
    public final UnaryCallable<ListExtensionBindingsRequest,DepServiceClient.ListExtensionBindingsPagedResponse> listExtensionBindingsPagedCallable()

Lists `ExtensionBinding` resources in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ListExtensionBindingsRequest request =
           ListExtensionBindingsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ExtensionBinding> future =
           depServiceClient.listExtensionBindingsPagedCallable().futureCall(request);
       // Do something.
       for (ExtensionBinding element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExtensionBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListExtensionBindingsRequest),[ListExtensionBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListExtensionBindingsPagedResponse)>` |   
  
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
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The project and location from which the `LbRouteExtension` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
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
`request` | `[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
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
Required. The project and location from which the `LbRouteExtension` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbRouteExtensionsPagedResponse)` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsRequest),[ListLbRouteExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsResponse)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbRouteExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbRouteExtensionsRequest),[ListLbRouteExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbRouteExtensionsPagedResponse)>` |   
  
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
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkservices.v1beta1.LocationName`  
Required. The project and location from which the `LbTrafficExtension` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
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
`request` | `[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
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
Required. The project and location from which the `LbTrafficExtension` resources are listed, specified in the following format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[DepServiceClient.ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsRequest),[ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsResponse)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLbTrafficExtensionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ListLbTrafficExtensionsRequest),[ListLbTrafficExtensionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLbTrafficExtensionsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DepServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

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
`[DepServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

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

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.DepServiceClient.ListLocationsPagedResponse)>` |   
  
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
  
### updateExtensionBindingAsync(ExtensionBinding extensionBinding, FieldMask updateMask)
    
    
    public final OperationFuture<ExtensionBinding,OperationMetadata> updateExtensionBindingAsync(ExtensionBinding extensionBinding, FieldMask updateMask)

Updates the parameters of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       ExtensionBinding extensionBinding = ExtensionBinding.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ExtensionBinding response =
           depServiceClient.updateExtensionBindingAsync(extensionBinding, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`extensionBinding` | `[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding)`  
Required. Updated `ExtensionBinding` resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the `ExtensionBinding` resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### updateExtensionBindingAsync(UpdateExtensionBindingRequest request)
    
    
    public final OperationFuture<ExtensionBinding,OperationMetadata> updateExtensionBindingAsync(UpdateExtensionBindingRequest request)

Updates the parameters of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateExtensionBindingRequest request =
           UpdateExtensionBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       ExtensionBinding response = depServiceClient.updateExtensionBindingAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateExtensionBindingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
### updateExtensionBindingCallable()
    
    
    public final UnaryCallable<UpdateExtensionBindingRequest,Operation> updateExtensionBindingCallable()

Updates the parameters of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateExtensionBindingRequest request =
           UpdateExtensionBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           depServiceClient.updateExtensionBindingCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateExtensionBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExtensionBindingOperationCallable()
    
    
    public final OperationCallable<UpdateExtensionBindingRequest,ExtensionBinding,OperationMetadata> updateExtensionBindingOperationCallable()

Updates the parameters of the specified `ExtensionBinding` resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DepServiceClient depServiceClient = DepServiceClient.create()) {
       UpdateExtensionBindingRequest request =
           UpdateExtensionBindingRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setExtensionBinding(ExtensionBinding.newBuilder().build())
               .build();
       OperationFuture<ExtensionBinding, OperationMetadata> future =
           depServiceClient.updateExtensionBindingOperationCallable().futureCall(request);
       // Do something.
       ExtensionBinding response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateExtensionBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateExtensionBindingRequest),[ExtensionBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.ExtensionBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`lbRouteExtension` | `[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension)`  
Required. `LbRouteExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Used to specify the fields to be overwritten in the `LbRouteExtension` resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbRouteExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbRouteExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLbRouteExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbRouteExtensionRequest),[LbRouteExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbRouteExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`lbTrafficExtension` | `[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension)`  
Required. `LbTrafficExtension` resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Used to specify the fields to be overwritten in the `LbTrafficExtension` resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not specify a mask, then all fields are overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`request` | `[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbTrafficExtensionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbTrafficExtensionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLbTrafficExtensionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.UpdateLbTrafficExtensionRequest),[LbTrafficExtension](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.LbTrafficExtension),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
