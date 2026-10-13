---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient
title: Class CrossNetworkAutomationServiceClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:03.588932+00:00
---

# Class CrossNetworkAutomationServiceClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CrossNetworkAutomationServiceClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkconnectivity/google-cloud-networkconnectivity/src/main/java/com/google/cloud/networkconnectivity/v1/CrossNetworkAutomationServiceClient.java)| [Product Reference](https://cloud.google.com/network-connectivity/docs)  
---|---  
  
Service Description: The service for CrossNetworkAutomation resources.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionMapName name =
           ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]");
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.getServiceConnectionMap(name);
     }
     

Note: close() needs to be called on the CrossNetworkAutomationServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListServiceConnectionMaps |  Lists ServiceConnectionMaps in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceConnectionMaps(ListServiceConnectionMapsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceConnectionMaps(LocationName parent) 
  * listServiceConnectionMaps(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceConnectionMapsPagedCallable() 
  * listServiceConnectionMapsCallable() 

  
GetServiceConnectionMap |  Gets details of a single ServiceConnectionMap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceConnectionMap(GetServiceConnectionMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceConnectionMap(ServiceConnectionMapName name) 
  * getServiceConnectionMap(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceConnectionMapCallable() 

  
CreateServiceConnectionMap |  Creates a new ServiceConnectionMap in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceConnectionMapAsync(CreateServiceConnectionMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceConnectionMapAsync(LocationName parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId) 
  * createServiceConnectionMapAsync(String parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceConnectionMapOperationCallable() 
  * createServiceConnectionMapCallable() 

  
UpdateServiceConnectionMap |  Updates the parameters of a single ServiceConnectionMap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceConnectionMapAsync(UpdateServiceConnectionMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceConnectionMapAsync(ServiceConnectionMap serviceConnectionMap, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceConnectionMapOperationCallable() 
  * updateServiceConnectionMapCallable() 

  
DeleteServiceConnectionMap |  Deletes a single ServiceConnectionMap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceConnectionMapAsync(DeleteServiceConnectionMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceConnectionMapAsync(ServiceConnectionMapName name) 
  * deleteServiceConnectionMapAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceConnectionMapOperationCallable() 
  * deleteServiceConnectionMapCallable() 

  
ListServiceConnectionPolicies |  Lists ServiceConnectionPolicies in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceConnectionPolicies(ListServiceConnectionPoliciesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceConnectionPolicies(LocationName parent) 
  * listServiceConnectionPolicies(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceConnectionPoliciesPagedCallable() 
  * listServiceConnectionPoliciesCallable() 

  
GetServiceConnectionPolicy |  Gets details of a single ServiceConnectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceConnectionPolicy(GetServiceConnectionPolicyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceConnectionPolicy(ServiceConnectionPolicyName name) 
  * getServiceConnectionPolicy(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceConnectionPolicyCallable() 

  
CreateServiceConnectionPolicy |  Creates a new ServiceConnectionPolicy in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceConnectionPolicyAsync(CreateServiceConnectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceConnectionPolicyAsync(LocationName parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId) 
  * createServiceConnectionPolicyAsync(String parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceConnectionPolicyOperationCallable() 
  * createServiceConnectionPolicyCallable() 

  
UpdateServiceConnectionPolicy |  Updates the parameters of a single ServiceConnectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceConnectionPolicyAsync(UpdateServiceConnectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceConnectionPolicyAsync(ServiceConnectionPolicy serviceConnectionPolicy, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceConnectionPolicyOperationCallable() 
  * updateServiceConnectionPolicyCallable() 

  
DeleteServiceConnectionPolicy |  Deletes a single ServiceConnectionPolicy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceConnectionPolicyAsync(DeleteServiceConnectionPolicyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceConnectionPolicyAsync(ServiceConnectionPolicyName name) 
  * deleteServiceConnectionPolicyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceConnectionPolicyOperationCallable() 
  * deleteServiceConnectionPolicyCallable() 

  
ListServiceClasses |  Lists ServiceClasses in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceClasses(ListServiceClassesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceClasses(LocationName parent) 
  * listServiceClasses(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceClassesPagedCallable() 
  * listServiceClassesCallable() 

  
GetServiceClass |  Gets details of a single ServiceClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceClass(GetServiceClassRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceClass(ServiceClassName name) 
  * getServiceClass(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceClassCallable() 

  
UpdateServiceClass |  Updates the parameters of a single ServiceClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateServiceClassAsync(UpdateServiceClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateServiceClassAsync(ServiceClass serviceClass, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateServiceClassOperationCallable() 
  * updateServiceClassCallable() 

  
DeleteServiceClass |  Deletes a single ServiceClass. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceClassAsync(DeleteServiceClassRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceClassAsync(ServiceClassName name) 
  * deleteServiceClassAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceClassOperationCallable() 
  * deleteServiceClassCallable() 

  
GetServiceConnectionToken |  Gets details of a single ServiceConnectionToken. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getServiceConnectionToken(GetServiceConnectionTokenRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getServiceConnectionToken(ServiceConnectionTokenName name) 
  * getServiceConnectionToken(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getServiceConnectionTokenCallable() 

  
ListServiceConnectionTokens |  Lists ServiceConnectionTokens in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listServiceConnectionTokens(ListServiceConnectionTokensRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listServiceConnectionTokens(LocationName parent) 
  * listServiceConnectionTokens(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listServiceConnectionTokensPagedCallable() 
  * listServiceConnectionTokensCallable() 

  
CreateServiceConnectionToken |  Creates a new ServiceConnectionToken in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createServiceConnectionTokenAsync(CreateServiceConnectionTokenRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createServiceConnectionTokenAsync(LocationName parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId) 
  * createServiceConnectionTokenAsync(String parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createServiceConnectionTokenOperationCallable() 
  * createServiceConnectionTokenCallable() 

  
DeleteServiceConnectionToken |  Deletes a single ServiceConnectionToken. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteServiceConnectionTokenAsync(DeleteServiceConnectionTokenRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteServiceConnectionTokenAsync(ServiceConnectionTokenName name) 
  * deleteServiceConnectionTokenAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteServiceConnectionTokenOperationCallable() 
  * deleteServiceConnectionTokenCallable() 

  
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

This class can be customized by passing in a custom instance of CrossNetworkAutomationServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CrossNetworkAutomationServiceSettings crossNetworkAutomationServiceSettings =
         CrossNetworkAutomationServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create(crossNetworkAutomationServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CrossNetworkAutomationServiceSettings crossNetworkAutomationServiceSettings =
         CrossNetworkAutomationServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create(crossNetworkAutomationServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CrossNetworkAutomationServiceClient

## Static Methods 

### create()
    
    
    public static final CrossNetworkAutomationServiceClient create()

Constructs an instance of CrossNetworkAutomationServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CrossNetworkAutomationServiceSettings settings)
    
    
    public static final CrossNetworkAutomationServiceClient create(CrossNetworkAutomationServiceSettings settings)

Constructs an instance of CrossNetworkAutomationServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CrossNetworkAutomationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CrossNetworkAutomationServiceStub stub)
    
    
    public static final CrossNetworkAutomationServiceClient create(CrossNetworkAutomationServiceStub stub)

Constructs an instance of CrossNetworkAutomationServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CrossNetworkAutomationServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CrossNetworkAutomationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.CrossNetworkAutomationServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient)` |   
  
## Constructors 

### CrossNetworkAutomationServiceClient(CrossNetworkAutomationServiceSettings settings)
    
    
    protected CrossNetworkAutomationServiceClient(CrossNetworkAutomationServiceSettings settings)

Constructs an instance of CrossNetworkAutomationServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CrossNetworkAutomationServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceSettings)`  
  
  
### CrossNetworkAutomationServiceClient(CrossNetworkAutomationServiceStub stub)
    
    
    protected CrossNetworkAutomationServiceClient(CrossNetworkAutomationServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CrossNetworkAutomationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.CrossNetworkAutomationServiceStub)`  
  
  
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

### createServiceConnectionMapAsync(@Nullable LocationName parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId)
    
    
    public final OperationFuture<ServiceConnectionMap,OperationMetadata> createServiceConnectionMapAsync(@Nullable LocationName parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId)

Creates a new ServiceConnectionMap in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServiceConnectionMap serviceConnectionMap = ServiceConnectionMap.newBuilder().build();
       String serviceConnectionMapId = "serviceConnectionMapId407176164";
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionMapAsync(parent, serviceConnectionMap, serviceConnectionMapId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name of the ServiceConnectionMap. ex. projects/123/locations/us-east1  
`serviceConnectionMap` | `[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)`  
Required. Initial values for a new ServiceConnectionMaps  
`serviceConnectionMapId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/serviceConnectionMaps/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location. If one is not provided, one will be generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionMapAsync(CreateServiceConnectionMapRequest request)
    
    
    public final OperationFuture<ServiceConnectionMap,OperationMetadata> createServiceConnectionMapAsync(CreateServiceConnectionMapRequest request)

Creates a new ServiceConnectionMap in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionMapRequest request =
           CreateServiceConnectionMapRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionMapId("serviceConnectionMapId407176164")
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.createServiceConnectionMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionMapAsync(String parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId)
    
    
    public final OperationFuture<ServiceConnectionMap,OperationMetadata> createServiceConnectionMapAsync(String parent, ServiceConnectionMap serviceConnectionMap, String serviceConnectionMapId)

Creates a new ServiceConnectionMap in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServiceConnectionMap serviceConnectionMap = ServiceConnectionMap.newBuilder().build();
       String serviceConnectionMapId = "serviceConnectionMapId407176164";
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionMapAsync(parent, serviceConnectionMap, serviceConnectionMapId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name of the ServiceConnectionMap. ex. projects/123/locations/us-east1  
`serviceConnectionMap` | `[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)`  
Required. Initial values for a new ServiceConnectionMaps  
`serviceConnectionMapId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/serviceConnectionMaps/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location. If one is not provided, one will be generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionMapCallable()
    
    
    public final UnaryCallable<CreateServiceConnectionMapRequest,Operation> createServiceConnectionMapCallable()

Creates a new ServiceConnectionMap in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionMapRequest request =
           CreateServiceConnectionMapRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionMapId("serviceConnectionMapId407176164")
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionMapCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceConnectionMapOperationCallable()
    
    
    public final OperationCallable<CreateServiceConnectionMapRequest,ServiceConnectionMap,OperationMetadata> createServiceConnectionMapOperationCallable()

Creates a new ServiceConnectionMap in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionMapRequest request =
           CreateServiceConnectionMapRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionMapId("serviceConnectionMapId407176164")
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceConnectionMap, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionMapOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionMapRequest),[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionPolicyAsync(@Nullable LocationName parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId)
    
    
    public final OperationFuture<ServiceConnectionPolicy,OperationMetadata> createServiceConnectionPolicyAsync(@Nullable LocationName parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId)

Creates a new ServiceConnectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServiceConnectionPolicy serviceConnectionPolicy =
           ServiceConnectionPolicy.newBuilder().build();
       String serviceConnectionPolicyId = "serviceConnectionPolicyId1586196096";
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionPolicyAsync(
                   parent, serviceConnectionPolicy, serviceConnectionPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name of the ServiceConnectionPolicy. ex. projects/123/locations/us-east1  
`serviceConnectionPolicy` | `[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)`  
Required. Initial values for a new ServiceConnectionPolicies  
`serviceConnectionPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/serviceConnectionPolicies/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionPolicyAsync(CreateServiceConnectionPolicyRequest request)
    
    
    public final OperationFuture<ServiceConnectionPolicy,OperationMetadata> createServiceConnectionPolicyAsync(CreateServiceConnectionPolicyRequest request)

Creates a new ServiceConnectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionPolicyRequest request =
           CreateServiceConnectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionPolicyId("serviceConnectionPolicyId1586196096")
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient.createServiceConnectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionPolicyAsync(String parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId)
    
    
    public final OperationFuture<ServiceConnectionPolicy,OperationMetadata> createServiceConnectionPolicyAsync(String parent, ServiceConnectionPolicy serviceConnectionPolicy, String serviceConnectionPolicyId)

Creates a new ServiceConnectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServiceConnectionPolicy serviceConnectionPolicy =
           ServiceConnectionPolicy.newBuilder().build();
       String serviceConnectionPolicyId = "serviceConnectionPolicyId1586196096";
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionPolicyAsync(
                   parent, serviceConnectionPolicy, serviceConnectionPolicyId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name of the ServiceConnectionPolicy. ex. projects/123/locations/us-east1  
`serviceConnectionPolicy` | `[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)`  
Required. Initial values for a new ServiceConnectionPolicies  
`serviceConnectionPolicyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/serviceConnectionPolicies/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionPolicyCallable()
    
    
    public final UnaryCallable<CreateServiceConnectionPolicyRequest,Operation> createServiceConnectionPolicyCallable()

Creates a new ServiceConnectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionPolicyRequest request =
           CreateServiceConnectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionPolicyId("serviceConnectionPolicyId1586196096")
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionPolicyCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceConnectionPolicyOperationCallable()
    
    
    public final OperationCallable<CreateServiceConnectionPolicyRequest,ServiceConnectionPolicy,OperationMetadata> createServiceConnectionPolicyOperationCallable()

Creates a new ServiceConnectionPolicy in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionPolicyRequest request =
           CreateServiceConnectionPolicyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionPolicyId("serviceConnectionPolicyId1586196096")
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceConnectionPolicy, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionPolicyOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionPolicyRequest),[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionTokenAsync(@Nullable LocationName parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId)
    
    
    public final OperationFuture<ServiceConnectionToken,OperationMetadata> createServiceConnectionTokenAsync(@Nullable LocationName parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId)

Creates a new ServiceConnectionToken in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ServiceConnectionToken serviceConnectionToken = ServiceConnectionToken.newBuilder().build();
       String serviceConnectionTokenId = "serviceConnectionTokenId-1526102527";
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionTokenAsync(
                   parent, serviceConnectionToken, serviceConnectionTokenId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name of the ServiceConnectionToken. ex. projects/123/locations/us-east1  
`serviceConnectionToken` | `[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)`  
Required. Initial values for a new ServiceConnectionTokens  
`serviceConnectionTokenId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/ServiceConnectionTokens/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location. If one is not provided, one will be generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionTokenAsync(CreateServiceConnectionTokenRequest request)
    
    
    public final OperationFuture<ServiceConnectionToken,OperationMetadata> createServiceConnectionTokenAsync(CreateServiceConnectionTokenRequest request)

Creates a new ServiceConnectionToken in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionTokenRequest request =
           CreateServiceConnectionTokenRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionTokenId("serviceConnectionTokenId-1526102527")
               .setServiceConnectionToken(ServiceConnectionToken.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient.createServiceConnectionTokenAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionTokenAsync(String parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId)
    
    
    public final OperationFuture<ServiceConnectionToken,OperationMetadata> createServiceConnectionTokenAsync(String parent, ServiceConnectionToken serviceConnectionToken, String serviceConnectionTokenId)

Creates a new ServiceConnectionToken in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ServiceConnectionToken serviceConnectionToken = ServiceConnectionToken.newBuilder().build();
       String serviceConnectionTokenId = "serviceConnectionTokenId-1526102527";
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient
               .createServiceConnectionTokenAsync(
                   parent, serviceConnectionToken, serviceConnectionTokenId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name of the ServiceConnectionToken. ex. projects/123/locations/us-east1  
`serviceConnectionToken` | `[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)`  
Required. Initial values for a new ServiceConnectionTokens  
`serviceConnectionTokenId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. Resource ID (i.e. 'foo' in '[...]/projects/p/locations/l/ServiceConnectionTokens/foo') See <https://google.aip.dev/122#resource-id-segments> Unique per location. If one is not provided, one will be generated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createServiceConnectionTokenCallable()
    
    
    public final UnaryCallable<CreateServiceConnectionTokenRequest,Operation> createServiceConnectionTokenCallable()

Creates a new ServiceConnectionToken in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionTokenRequest request =
           CreateServiceConnectionTokenRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionTokenId("serviceConnectionTokenId-1526102527")
               .setServiceConnectionToken(ServiceConnectionToken.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionTokenCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionTokenRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceConnectionTokenOperationCallable()
    
    
    public final OperationCallable<CreateServiceConnectionTokenRequest,ServiceConnectionToken,OperationMetadata> createServiceConnectionTokenOperationCallable()

Creates a new ServiceConnectionToken in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       CreateServiceConnectionTokenRequest request =
           CreateServiceConnectionTokenRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setServiceConnectionTokenId("serviceConnectionTokenId-1526102527")
               .setServiceConnectionToken(ServiceConnectionToken.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceConnectionToken, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .createServiceConnectionTokenOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionToken response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateServiceConnectionTokenRequest),[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceClassAsync(@Nullable ServiceClassName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceClassAsync(@Nullable ServiceClassName name)

Deletes a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceClassName name = ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]");
       crossNetworkAutomationServiceClient.deleteServiceClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceClassName`  
Required. The name of the ServiceClass to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceClassAsync(DeleteServiceClassRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceClassAsync(DeleteServiceClassRequest request)

Deletes a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceClassRequest request =
           DeleteServiceClassRequest.newBuilder()
               .setName(ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       crossNetworkAutomationServiceClient.deleteServiceClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceClassAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceClassAsync(String name)

Deletes a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name = ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString();
       crossNetworkAutomationServiceClient.deleteServiceClassAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ServiceClass to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceClassCallable()
    
    
    public final UnaryCallable<DeleteServiceClassRequest,Operation> deleteServiceClassCallable()

Deletes a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceClassRequest request =
           DeleteServiceClassRequest.newBuilder()
               .setName(ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient.deleteServiceClassCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceClassOperationCallable()
    
    
    public final OperationCallable<DeleteServiceClassRequest,Empty,OperationMetadata> deleteServiceClassOperationCallable()

Deletes a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceClassRequest request =
           DeleteServiceClassRequest.newBuilder()
               .setName(ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .deleteServiceClassOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceClassRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionMapAsync(@Nullable ServiceConnectionMapName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionMapAsync(@Nullable ServiceConnectionMapName name)

Deletes a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionMapName name =
           ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]");
       crossNetworkAutomationServiceClient.deleteServiceConnectionMapAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionMapName`  
Required. The name of the ServiceConnectionMap to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionMapAsync(DeleteServiceConnectionMapRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionMapAsync(DeleteServiceConnectionMapRequest request)

Deletes a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionMapRequest request =
           DeleteServiceConnectionMapRequest.newBuilder()
               .setName(
                   ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       crossNetworkAutomationServiceClient.deleteServiceConnectionMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionMapAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionMapAsync(String name)

Deletes a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
               .toString();
       crossNetworkAutomationServiceClient.deleteServiceConnectionMapAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ServiceConnectionMap to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionMapCallable()
    
    
    public final UnaryCallable<DeleteServiceConnectionMapRequest,Operation> deleteServiceConnectionMapCallable()

Deletes a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionMapRequest request =
           DeleteServiceConnectionMapRequest.newBuilder()
               .setName(
                   ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionMapCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceConnectionMapOperationCallable()
    
    
    public final OperationCallable<DeleteServiceConnectionMapRequest,Empty,OperationMetadata> deleteServiceConnectionMapOperationCallable()

Deletes a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionMapRequest request =
           DeleteServiceConnectionMapRequest.newBuilder()
               .setName(
                   ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionMapOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionMapRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionPolicyAsync(@Nullable ServiceConnectionPolicyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionPolicyAsync(@Nullable ServiceConnectionPolicyName name)

Deletes a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionPolicyName name =
           ServiceConnectionPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]");
       crossNetworkAutomationServiceClient.deleteServiceConnectionPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicyName`  
Required. The name of the ServiceConnectionPolicy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionPolicyAsync(DeleteServiceConnectionPolicyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionPolicyAsync(DeleteServiceConnectionPolicyRequest request)

Deletes a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionPolicyRequest request =
           DeleteServiceConnectionPolicyRequest.newBuilder()
               .setName(
                   ServiceConnectionPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       crossNetworkAutomationServiceClient.deleteServiceConnectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionPolicyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionPolicyAsync(String name)

Deletes a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
               .toString();
       crossNetworkAutomationServiceClient.deleteServiceConnectionPolicyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ServiceConnectionPolicy to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionPolicyCallable()
    
    
    public final UnaryCallable<DeleteServiceConnectionPolicyRequest,Operation> deleteServiceConnectionPolicyCallable()

Deletes a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionPolicyRequest request =
           DeleteServiceConnectionPolicyRequest.newBuilder()
               .setName(
                   ServiceConnectionPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionPolicyCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceConnectionPolicyOperationCallable()
    
    
    public final OperationCallable<DeleteServiceConnectionPolicyRequest,Empty,OperationMetadata> deleteServiceConnectionPolicyOperationCallable()

Deletes a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionPolicyRequest request =
           DeleteServiceConnectionPolicyRequest.newBuilder()
               .setName(
                   ServiceConnectionPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionPolicyOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionTokenAsync(@Nullable ServiceConnectionTokenName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionTokenAsync(@Nullable ServiceConnectionTokenName name)

Deletes a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionTokenName name =
           ServiceConnectionTokenName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]");
       crossNetworkAutomationServiceClient.deleteServiceConnectionTokenAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionTokenName`  
Required. The name of the ServiceConnectionToken to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionTokenAsync(DeleteServiceConnectionTokenRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionTokenAsync(DeleteServiceConnectionTokenRequest request)

Deletes a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionTokenRequest request =
           DeleteServiceConnectionTokenRequest.newBuilder()
               .setName(
                   ServiceConnectionTokenName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       crossNetworkAutomationServiceClient.deleteServiceConnectionTokenAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionTokenAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteServiceConnectionTokenAsync(String name)

Deletes a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionTokenName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
               .toString();
       crossNetworkAutomationServiceClient.deleteServiceConnectionTokenAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ServiceConnectionToken to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteServiceConnectionTokenCallable()
    
    
    public final UnaryCallable<DeleteServiceConnectionTokenRequest,Operation> deleteServiceConnectionTokenCallable()

Deletes a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionTokenRequest request =
           DeleteServiceConnectionTokenRequest.newBuilder()
               .setName(
                   ServiceConnectionTokenName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionTokenCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionTokenRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceConnectionTokenOperationCallable()
    
    
    public final OperationCallable<DeleteServiceConnectionTokenRequest,Empty,OperationMetadata> deleteServiceConnectionTokenOperationCallable()

Deletes a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       DeleteServiceConnectionTokenRequest request =
           DeleteServiceConnectionTokenRequest.newBuilder()
               .setName(
                   ServiceConnectionTokenName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
                       .toString())
               .setRequestId("requestId693933066")
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .deleteServiceConnectionTokenOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteServiceConnectionTokenRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = crossNetworkAutomationServiceClient.getIamPolicy(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           crossNetworkAutomationServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = crossNetworkAutomationServiceClient.getLocation(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           crossNetworkAutomationServiceClient.getLocationCallable().futureCall(request);
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
  
### getServiceClass(@Nullable ServiceClassName name)
    
    
    public final ServiceClass getServiceClass(@Nullable ServiceClassName name)

Gets details of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceClassName name = ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]");
       ServiceClass response = crossNetworkAutomationServiceClient.getServiceClass(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceClassName`  
Required. Name of the ServiceClass to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass)` |   
  
### getServiceClass(GetServiceClassRequest request)
    
    
    public final ServiceClass getServiceClass(GetServiceClassRequest request)

Gets details of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceClassRequest request =
           GetServiceClassRequest.newBuilder()
               .setName(ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString())
               .build();
       ServiceClass response = crossNetworkAutomationServiceClient.getServiceClass(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass)` |   
  
### getServiceClass(String name)
    
    
    public final ServiceClass getServiceClass(String name)

Gets details of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name = ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString();
       ServiceClass response = crossNetworkAutomationServiceClient.getServiceClass(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the ServiceClass to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass)` |   
  
### getServiceClassCallable()
    
    
    public final UnaryCallable<GetServiceClassRequest,ServiceClass> getServiceClassCallable()

Gets details of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceClassRequest request =
           GetServiceClassRequest.newBuilder()
               .setName(ServiceClassName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CLASS]").toString())
               .build();
       ApiFuture<ServiceClass> future =
           crossNetworkAutomationServiceClient.getServiceClassCallable().futureCall(request);
       // Do something.
       ServiceClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceClassRequest),[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass)>` |   
  
### getServiceConnectionMap(@Nullable ServiceConnectionMapName name)
    
    
    public final ServiceConnectionMap getServiceConnectionMap(@Nullable ServiceConnectionMapName name)

Gets details of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionMapName name =
           ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]");
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.getServiceConnectionMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionMapName`  
Required. Name of the ServiceConnectionMap to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)` |   
  
### getServiceConnectionMap(GetServiceConnectionMapRequest request)
    
    
    public final ServiceConnectionMap getServiceConnectionMap(GetServiceConnectionMapRequest request)

Gets details of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionMapRequest request =
           GetServiceConnectionMapRequest.newBuilder()
               .setName(
                   ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
                       .toString())
               .build();
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.getServiceConnectionMap(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)` |   
  
### getServiceConnectionMap(String name)
    
    
    public final ServiceConnectionMap getServiceConnectionMap(String name)

Gets details of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
               .toString();
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.getServiceConnectionMap(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the ServiceConnectionMap to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)` |   
  
### getServiceConnectionMapCallable()
    
    
    public final UnaryCallable<GetServiceConnectionMapRequest,ServiceConnectionMap> getServiceConnectionMapCallable()

Gets details of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionMapRequest request =
           GetServiceConnectionMapRequest.newBuilder()
               .setName(
                   ServiceConnectionMapName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_MAP]")
                       .toString())
               .build();
       ApiFuture<ServiceConnectionMap> future =
           crossNetworkAutomationServiceClient.getServiceConnectionMapCallable().futureCall(request);
       // Do something.
       ServiceConnectionMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionMapRequest),[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)>` |   
  
### getServiceConnectionPolicy(@Nullable ServiceConnectionPolicyName name)
    
    
    public final ServiceConnectionPolicy getServiceConnectionPolicy(@Nullable ServiceConnectionPolicyName name)

Gets details of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionPolicyName name =
           ServiceConnectionPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]");
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient.getServiceConnectionPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicyName`  
Required. Name of the ServiceConnectionPolicy to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)` |   
  
### getServiceConnectionPolicy(GetServiceConnectionPolicyRequest request)
    
    
    public final ServiceConnectionPolicy getServiceConnectionPolicy(GetServiceConnectionPolicyRequest request)

Gets details of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionPolicyRequest request =
           GetServiceConnectionPolicyRequest.newBuilder()
               .setName(
                   ServiceConnectionPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
                       .toString())
               .build();
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient.getServiceConnectionPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)` |   
  
### getServiceConnectionPolicy(String name)
    
    
    public final ServiceConnectionPolicy getServiceConnectionPolicy(String name)

Gets details of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionPolicyName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
               .toString();
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient.getServiceConnectionPolicy(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the ServiceConnectionPolicy to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)` |   
  
### getServiceConnectionPolicyCallable()
    
    
    public final UnaryCallable<GetServiceConnectionPolicyRequest,ServiceConnectionPolicy> getServiceConnectionPolicyCallable()

Gets details of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionPolicyRequest request =
           GetServiceConnectionPolicyRequest.newBuilder()
               .setName(
                   ServiceConnectionPolicyName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_POLICY]")
                       .toString())
               .build();
       ApiFuture<ServiceConnectionPolicy> future =
           crossNetworkAutomationServiceClient
               .getServiceConnectionPolicyCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionPolicyRequest),[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)>` |   
  
### getServiceConnectionToken(@Nullable ServiceConnectionTokenName name)
    
    
    public final ServiceConnectionToken getServiceConnectionToken(@Nullable ServiceConnectionTokenName name)

Gets details of a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionTokenName name =
           ServiceConnectionTokenName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]");
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient.getServiceConnectionToken(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.ServiceConnectionTokenName`  
Required. Name of the ServiceConnectionToken to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)` |   
  
### getServiceConnectionToken(GetServiceConnectionTokenRequest request)
    
    
    public final ServiceConnectionToken getServiceConnectionToken(GetServiceConnectionTokenRequest request)

Gets details of a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionTokenRequest request =
           GetServiceConnectionTokenRequest.newBuilder()
               .setName(
                   ServiceConnectionTokenName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
                       .toString())
               .build();
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient.getServiceConnectionToken(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)` |   
  
### getServiceConnectionToken(String name)
    
    
    public final ServiceConnectionToken getServiceConnectionToken(String name)

Gets details of a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String name =
           ServiceConnectionTokenName.of("[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
               .toString();
       ServiceConnectionToken response =
           crossNetworkAutomationServiceClient.getServiceConnectionToken(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the ServiceConnectionToken to get.  
**Returns**  
---  
**Type** | **Description**  
`[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)` |   
  
### getServiceConnectionTokenCallable()
    
    
    public final UnaryCallable<GetServiceConnectionTokenRequest,ServiceConnectionToken> getServiceConnectionTokenCallable()

Gets details of a single ServiceConnectionToken.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       GetServiceConnectionTokenRequest request =
           GetServiceConnectionTokenRequest.newBuilder()
               .setName(
                   ServiceConnectionTokenName.of(
                           "[PROJECT]", "[LOCATION]", "[SERVICE_CONNECTION_TOKEN]")
                       .toString())
               .build();
       ApiFuture<ServiceConnectionToken> future =
           crossNetworkAutomationServiceClient
               .getServiceConnectionTokenCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionToken response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetServiceConnectionTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetServiceConnectionTokenRequest),[ServiceConnectionToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionToken)>` |   
  
### getSettings()
    
    
    public final @Nullable CrossNetworkAutomationServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceSettings` |   
  
### getStub()
    
    
    public CrossNetworkAutomationServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.CrossNetworkAutomationServiceStub)` |   
  
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
    
    
    public final CrossNetworkAutomationServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           crossNetworkAutomationServiceClient.listLocations(request).iterateAll()) {
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
`[CrossNetworkAutomationServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             crossNetworkAutomationServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CrossNetworkAutomationServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           crossNetworkAutomationServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListLocationsPagedResponse)>` |   
  
### listServiceClasses(@Nullable LocationName parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse listServiceClasses(@Nullable LocationName parent)

Lists ServiceClasses in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceClass element :
           crossNetworkAutomationServiceClient.listServiceClasses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse)` |   
  
### listServiceClasses(ListServiceClassesRequest request)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse listServiceClasses(ListServiceClassesRequest request)

Lists ServiceClasses in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceClassesRequest request =
           ListServiceClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ServiceClass element :
           crossNetworkAutomationServiceClient.listServiceClasses(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceClassesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse)` |   
  
### listServiceClasses(String parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse listServiceClasses(String parent)

Lists ServiceClasses in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceClass element :
           crossNetworkAutomationServiceClient.listServiceClasses(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse)` |   
  
### listServiceClassesCallable()
    
    
    public final UnaryCallable<ListServiceClassesRequest,ListServiceClassesResponse> listServiceClassesCallable()

Lists ServiceClasses in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceClassesRequest request =
           ListServiceClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServiceClassesResponse response =
             crossNetworkAutomationServiceClient.listServiceClassesCallable().call(request);
         for (ServiceClass element : response.getServiceClassesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceClassesRequest),[ListServiceClassesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceClassesResponse)>` |   
  
### listServiceClassesPagedCallable()
    
    
    public final UnaryCallable<ListServiceClassesRequest,CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse> listServiceClassesPagedCallable()

Lists ServiceClasses in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceClassesRequest request =
           ListServiceClassesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ServiceClass> future =
           crossNetworkAutomationServiceClient.listServiceClassesPagedCallable().futureCall(request);
       // Do something.
       for (ServiceClass element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceClassesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceClassesRequest),[ListServiceClassesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceClassesPagedResponse)>` |   
  
### listServiceConnectionMaps(@Nullable LocationName parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse listServiceConnectionMaps(@Nullable LocationName parent)

Lists ServiceConnectionMaps in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceConnectionMap element :
           crossNetworkAutomationServiceClient.listServiceConnectionMaps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse)` |   
  
### listServiceConnectionMaps(ListServiceConnectionMapsRequest request)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse listServiceConnectionMaps(ListServiceConnectionMapsRequest request)

Lists ServiceConnectionMaps in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionMapsRequest request =
           ListServiceConnectionMapsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ServiceConnectionMap element :
           crossNetworkAutomationServiceClient.listServiceConnectionMaps(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceConnectionMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionMapsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse)` |   
  
### listServiceConnectionMaps(String parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse listServiceConnectionMaps(String parent)

Lists ServiceConnectionMaps in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceConnectionMap element :
           crossNetworkAutomationServiceClient.listServiceConnectionMaps(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse)` |   
  
### listServiceConnectionMapsCallable()
    
    
    public final UnaryCallable<ListServiceConnectionMapsRequest,ListServiceConnectionMapsResponse> listServiceConnectionMapsCallable()

Lists ServiceConnectionMaps in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionMapsRequest request =
           ListServiceConnectionMapsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServiceConnectionMapsResponse response =
             crossNetworkAutomationServiceClient.listServiceConnectionMapsCallable().call(request);
         for (ServiceConnectionMap element : response.getServiceConnectionMapsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionMapsRequest),[ListServiceConnectionMapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionMapsResponse)>` |   
  
### listServiceConnectionMapsPagedCallable()
    
    
    public final UnaryCallable<ListServiceConnectionMapsRequest,CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse> listServiceConnectionMapsPagedCallable()

Lists ServiceConnectionMaps in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionMapsRequest request =
           ListServiceConnectionMapsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ServiceConnectionMap> future =
           crossNetworkAutomationServiceClient
               .listServiceConnectionMapsPagedCallable()
               .futureCall(request);
       // Do something.
       for (ServiceConnectionMap element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionMapsRequest),[ListServiceConnectionMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionMapsPagedResponse)>` |   
  
### listServiceConnectionPolicies(@Nullable LocationName parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse listServiceConnectionPolicies(@Nullable LocationName parent)

Lists ServiceConnectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceConnectionPolicy element :
           crossNetworkAutomationServiceClient.listServiceConnectionPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse)` |   
  
### listServiceConnectionPolicies(ListServiceConnectionPoliciesRequest request)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse listServiceConnectionPolicies(ListServiceConnectionPoliciesRequest request)

Lists ServiceConnectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionPoliciesRequest request =
           ListServiceConnectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ServiceConnectionPolicy element :
           crossNetworkAutomationServiceClient.listServiceConnectionPolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceConnectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse)` |   
  
### listServiceConnectionPolicies(String parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse listServiceConnectionPolicies(String parent)

Lists ServiceConnectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceConnectionPolicy element :
           crossNetworkAutomationServiceClient.listServiceConnectionPolicies(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse)` |   
  
### listServiceConnectionPoliciesCallable()
    
    
    public final UnaryCallable<ListServiceConnectionPoliciesRequest,ListServiceConnectionPoliciesResponse> listServiceConnectionPoliciesCallable()

Lists ServiceConnectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionPoliciesRequest request =
           ListServiceConnectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServiceConnectionPoliciesResponse response =
             crossNetworkAutomationServiceClient
                 .listServiceConnectionPoliciesCallable()
                 .call(request);
         for (ServiceConnectionPolicy element : response.getServiceConnectionPoliciesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesRequest),[ListServiceConnectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesResponse)>` |   
  
### listServiceConnectionPoliciesPagedCallable()
    
    
    public final UnaryCallable<ListServiceConnectionPoliciesRequest,CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse> listServiceConnectionPoliciesPagedCallable()

Lists ServiceConnectionPolicies in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionPoliciesRequest request =
           ListServiceConnectionPoliciesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ServiceConnectionPolicy> future =
           crossNetworkAutomationServiceClient
               .listServiceConnectionPoliciesPagedCallable()
               .futureCall(request);
       // Do something.
       for (ServiceConnectionPolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionPoliciesRequest),[ListServiceConnectionPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionPoliciesPagedResponse)>` |   
  
### listServiceConnectionTokens(@Nullable LocationName parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse listServiceConnectionTokens(@Nullable LocationName parent)

Lists ServiceConnectionTokens in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ServiceConnectionToken element :
           crossNetworkAutomationServiceClient.listServiceConnectionTokens(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse)` |   
  
### listServiceConnectionTokens(ListServiceConnectionTokensRequest request)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse listServiceConnectionTokens(ListServiceConnectionTokensRequest request)

Lists ServiceConnectionTokens in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionTokensRequest request =
           ListServiceConnectionTokensRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (ServiceConnectionToken element :
           crossNetworkAutomationServiceClient.listServiceConnectionTokens(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListServiceConnectionTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionTokensRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse)` |   
  
### listServiceConnectionTokens(String parent)
    
    
    public final CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse listServiceConnectionTokens(String parent)

Lists ServiceConnectionTokens in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ServiceConnectionToken element :
           crossNetworkAutomationServiceClient.listServiceConnectionTokens(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name. ex. projects/123/locations/us-east1  
**Returns**  
---  
**Type** | **Description**  
`[CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse)` |   
  
### listServiceConnectionTokensCallable()
    
    
    public final UnaryCallable<ListServiceConnectionTokensRequest,ListServiceConnectionTokensResponse> listServiceConnectionTokensCallable()

Lists ServiceConnectionTokens in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionTokensRequest request =
           ListServiceConnectionTokensRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListServiceConnectionTokensResponse response =
             crossNetworkAutomationServiceClient.listServiceConnectionTokensCallable().call(request);
         for (ServiceConnectionToken element : response.getServiceConnectionTokensList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionTokensRequest),[ListServiceConnectionTokensResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionTokensResponse)>` |   
  
### listServiceConnectionTokensPagedCallable()
    
    
    public final UnaryCallable<ListServiceConnectionTokensRequest,CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse> listServiceConnectionTokensPagedCallable()

Lists ServiceConnectionTokens in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ListServiceConnectionTokensRequest request =
           ListServiceConnectionTokensRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<ServiceConnectionToken> future =
           crossNetworkAutomationServiceClient
               .listServiceConnectionTokensPagedCallable()
               .futureCall(request);
       // Do something.
       for (ServiceConnectionToken element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListServiceConnectionTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListServiceConnectionTokensRequest),[ListServiceConnectionTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CrossNetworkAutomationServiceClient.ListServiceConnectionTokensPagedResponse)>` |   
  
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = crossNetworkAutomationServiceClient.setIamPolicy(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           crossNetworkAutomationServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           crossNetworkAutomationServiceClient.testIamPermissions(request);
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
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           crossNetworkAutomationServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateServiceClassAsync(ServiceClass serviceClass, FieldMask updateMask)
    
    
    public final OperationFuture<ServiceClass,OperationMetadata> updateServiceClassAsync(ServiceClass serviceClass, FieldMask updateMask)

Updates the parameters of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceClass serviceClass = ServiceClass.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServiceClass response =
           crossNetworkAutomationServiceClient
               .updateServiceClassAsync(serviceClass, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serviceClass` | `[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass)`  
Required. New values to be patched into the resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServiceClass resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceClassAsync(UpdateServiceClassRequest request)
    
    
    public final OperationFuture<ServiceClass,OperationMetadata> updateServiceClassAsync(UpdateServiceClassRequest request)

Updates the parameters of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceClassRequest request =
           UpdateServiceClassRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceClass(ServiceClass.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceClass response =
           crossNetworkAutomationServiceClient.updateServiceClassAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceClassRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceClassCallable()
    
    
    public final UnaryCallable<UpdateServiceClassRequest,Operation> updateServiceClassCallable()

Updates the parameters of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceClassRequest request =
           UpdateServiceClassRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceClass(ServiceClass.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient.updateServiceClassCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceClassRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceClassOperationCallable()
    
    
    public final OperationCallable<UpdateServiceClassRequest,ServiceClass,OperationMetadata> updateServiceClassOperationCallable()

Updates the parameters of a single ServiceClass.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceClassRequest request =
           UpdateServiceClassRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceClass(ServiceClass.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceClass, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .updateServiceClassOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceClass response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceClassRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceClassRequest),[ServiceClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceClass),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionMapAsync(ServiceConnectionMap serviceConnectionMap, FieldMask updateMask)
    
    
    public final OperationFuture<ServiceConnectionMap,OperationMetadata> updateServiceConnectionMapAsync(ServiceConnectionMap serviceConnectionMap, FieldMask updateMask)

Updates the parameters of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionMap serviceConnectionMap = ServiceConnectionMap.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionMapAsync(serviceConnectionMap, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serviceConnectionMap` | `[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap)`  
Required. New values to be patched into the resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServiceConnectionMap resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionMapAsync(UpdateServiceConnectionMapRequest request)
    
    
    public final OperationFuture<ServiceConnectionMap,OperationMetadata> updateServiceConnectionMapAsync(UpdateServiceConnectionMapRequest request)

Updates the parameters of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionMapRequest request =
           UpdateServiceConnectionMapRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceConnectionMap response =
           crossNetworkAutomationServiceClient.updateServiceConnectionMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionMapCallable()
    
    
    public final UnaryCallable<UpdateServiceConnectionMapRequest,Operation> updateServiceConnectionMapCallable()

Updates the parameters of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionMapRequest request =
           UpdateServiceConnectionMapRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionMapCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceConnectionMapOperationCallable()
    
    
    public final OperationCallable<UpdateServiceConnectionMapRequest,ServiceConnectionMap,OperationMetadata> updateServiceConnectionMapOperationCallable()

Updates the parameters of a single ServiceConnectionMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionMapRequest request =
           UpdateServiceConnectionMapRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionMap(ServiceConnectionMap.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceConnectionMap, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionMapOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceConnectionMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionMapRequest),[ServiceConnectionMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionMap),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionPolicyAsync(ServiceConnectionPolicy serviceConnectionPolicy, FieldMask updateMask)
    
    
    public final OperationFuture<ServiceConnectionPolicy,OperationMetadata> updateServiceConnectionPolicyAsync(ServiceConnectionPolicy serviceConnectionPolicy, FieldMask updateMask)

Updates the parameters of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       ServiceConnectionPolicy serviceConnectionPolicy =
           ServiceConnectionPolicy.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionPolicyAsync(serviceConnectionPolicy, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`serviceConnectionPolicy` | `[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy)`  
Required. New values to be patched into the resource.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the ServiceConnectionPolicy resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionPolicyAsync(UpdateServiceConnectionPolicyRequest request)
    
    
    public final OperationFuture<ServiceConnectionPolicy,OperationMetadata> updateServiceConnectionPolicyAsync(UpdateServiceConnectionPolicyRequest request)

Updates the parameters of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionPolicyRequest request =
           UpdateServiceConnectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ServiceConnectionPolicy response =
           crossNetworkAutomationServiceClient.updateServiceConnectionPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionPolicyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateServiceConnectionPolicyCallable()
    
    
    public final UnaryCallable<UpdateServiceConnectionPolicyRequest,Operation> updateServiceConnectionPolicyCallable()

Updates the parameters of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionPolicyRequest request =
           UpdateServiceConnectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionPolicyCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceConnectionPolicyOperationCallable()
    
    
    public final OperationCallable<UpdateServiceConnectionPolicyRequest,ServiceConnectionPolicy,OperationMetadata> updateServiceConnectionPolicyOperationCallable()

Updates the parameters of a single ServiceConnectionPolicy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossNetworkAutomationServiceClient crossNetworkAutomationServiceClient =
         CrossNetworkAutomationServiceClient.create()) {
       UpdateServiceConnectionPolicyRequest request =
           UpdateServiceConnectionPolicyRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setServiceConnectionPolicy(ServiceConnectionPolicy.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<ServiceConnectionPolicy, OperationMetadata> future =
           crossNetworkAutomationServiceClient
               .updateServiceConnectionPolicyOperationCallable()
               .futureCall(request);
       // Do something.
       ServiceConnectionPolicy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateServiceConnectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateServiceConnectionPolicyRequest),[ServiceConnectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ServiceConnectionPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
