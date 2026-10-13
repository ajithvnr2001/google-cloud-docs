---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient
title: Class PolicyBasedRoutingServiceClient (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:05.705605+00:00
---

# Class PolicyBasedRoutingServiceClient (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PolicyBasedRoutingServiceClient (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-networkconnectivity/google-cloud-networkconnectivity/src/main/java/com/google/cloud/networkconnectivity/v1/PolicyBasedRoutingServiceClient.java)| [Product Reference](https://cloud.google.com/network-connectivity/docs)  
---|---  
  
Service Description: Policy-Based Routing allows GCP customers to specify flexibile routing policies for Layer 4 traffic traversing through the connected service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       PolicyBasedRouteName name = PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]");
       PolicyBasedRoute response = policyBasedRoutingServiceClient.getPolicyBasedRoute(name);
     }
     

Note: close() needs to be called on the PolicyBasedRoutingServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListPolicyBasedRoutes |  Lists policy-based routes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPolicyBasedRoutes(ListPolicyBasedRoutesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPolicyBasedRoutes(LocationName parent) 
  * listPolicyBasedRoutes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPolicyBasedRoutesPagedCallable() 
  * listPolicyBasedRoutesCallable() 

  
GetPolicyBasedRoute |  Gets details of a single policy-based route. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPolicyBasedRoute(GetPolicyBasedRouteRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPolicyBasedRoute(PolicyBasedRouteName name) 
  * getPolicyBasedRoute(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPolicyBasedRouteCallable() 

  
CreatePolicyBasedRoute |  Creates a new policy-based route in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPolicyBasedRouteAsync(CreatePolicyBasedRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createPolicyBasedRouteAsync(LocationName parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId) 
  * createPolicyBasedRouteAsync(String parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPolicyBasedRouteOperationCallable() 
  * createPolicyBasedRouteCallable() 

  
DeletePolicyBasedRoute |  Deletes a single policy-based route. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePolicyBasedRouteAsync(DeletePolicyBasedRouteRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePolicyBasedRouteAsync(PolicyBasedRouteName name) 
  * deletePolicyBasedRouteAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePolicyBasedRouteOperationCallable() 
  * deletePolicyBasedRouteCallable() 

  
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

This class can be customized by passing in a custom instance of PolicyBasedRoutingServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PolicyBasedRoutingServiceSettings policyBasedRoutingServiceSettings =
         PolicyBasedRoutingServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create(policyBasedRoutingServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PolicyBasedRoutingServiceSettings policyBasedRoutingServiceSettings =
         PolicyBasedRoutingServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create(policyBasedRoutingServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PolicyBasedRoutingServiceClient

## Static Methods 

### create()
    
    
    public static final PolicyBasedRoutingServiceClient create()

Constructs an instance of PolicyBasedRoutingServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PolicyBasedRoutingServiceSettings settings)
    
    
    public static final PolicyBasedRoutingServiceClient create(PolicyBasedRoutingServiceSettings settings)

Constructs an instance of PolicyBasedRoutingServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PolicyBasedRoutingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PolicyBasedRoutingServiceStub stub)
    
    
    public static final PolicyBasedRoutingServiceClient create(PolicyBasedRoutingServiceStub stub)

Constructs an instance of PolicyBasedRoutingServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PolicyBasedRoutingServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PolicyBasedRoutingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.PolicyBasedRoutingServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient)` |   
  
## Constructors 

### PolicyBasedRoutingServiceClient(PolicyBasedRoutingServiceSettings settings)
    
    
    protected PolicyBasedRoutingServiceClient(PolicyBasedRoutingServiceSettings settings)

Constructs an instance of PolicyBasedRoutingServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PolicyBasedRoutingServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceSettings)`  
  
  
### PolicyBasedRoutingServiceClient(PolicyBasedRoutingServiceStub stub)
    
    
    protected PolicyBasedRoutingServiceClient(PolicyBasedRoutingServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PolicyBasedRoutingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.PolicyBasedRoutingServiceStub)`  
  
  
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

### createPolicyBasedRouteAsync(@Nullable LocationName parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId)
    
    
    public final OperationFuture<PolicyBasedRoute,OperationMetadata> createPolicyBasedRouteAsync(@Nullable LocationName parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId)

Creates a new policy-based route in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PolicyBasedRoute policyBasedRoute = PolicyBasedRoute.newBuilder().build();
       String policyBasedRouteId = "policyBasedRouteId-18034589";
       PolicyBasedRoute response =
           policyBasedRoutingServiceClient
               .createPolicyBasedRouteAsync(parent, policyBasedRoute, policyBasedRouteId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name of the PolicyBasedRoute.  
`policyBasedRoute` | `[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)`  
Required. Initial values for a new policy-based route.  
`policyBasedRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique id for the policy-based route to create. Provided by the client when the resource is created. The name must comply with <https://google.aip.dev/122#resource-id-segments>. Specifically, the name must be 1-63 characters long and match the regular expression [a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/\[a-z0-9-\]*\[a-z0-9\])?. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createPolicyBasedRouteAsync(CreatePolicyBasedRouteRequest request)
    
    
    public final OperationFuture<PolicyBasedRoute,OperationMetadata> createPolicyBasedRouteAsync(CreatePolicyBasedRouteRequest request)

Creates a new policy-based route in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       CreatePolicyBasedRouteRequest request =
           CreatePolicyBasedRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPolicyBasedRouteId("policyBasedRouteId-18034589")
               .setPolicyBasedRoute(PolicyBasedRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       PolicyBasedRoute response =
           policyBasedRoutingServiceClient.createPolicyBasedRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreatePolicyBasedRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createPolicyBasedRouteAsync(String parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId)
    
    
    public final OperationFuture<PolicyBasedRoute,OperationMetadata> createPolicyBasedRouteAsync(String parent, PolicyBasedRoute policyBasedRoute, String policyBasedRouteId)

Creates a new policy-based route in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PolicyBasedRoute policyBasedRoute = PolicyBasedRoute.newBuilder().build();
       String policyBasedRouteId = "policyBasedRouteId-18034589";
       PolicyBasedRoute response =
           policyBasedRoutingServiceClient
               .createPolicyBasedRouteAsync(parent, policyBasedRoute, policyBasedRouteId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name of the PolicyBasedRoute.  
`policyBasedRoute` | `[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)`  
Required. Initial values for a new policy-based route.  
`policyBasedRouteId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Unique id for the policy-based route to create. Provided by the client when the resource is created. The name must comply with <https://google.aip.dev/122#resource-id-segments>. Specifically, the name must be 1-63 characters long and match the regular expression [a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/\[a-z0-9-\]*\[a-z0-9\])?. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createPolicyBasedRouteCallable()
    
    
    public final UnaryCallable<CreatePolicyBasedRouteRequest,Operation> createPolicyBasedRouteCallable()

Creates a new policy-based route in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       CreatePolicyBasedRouteRequest request =
           CreatePolicyBasedRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPolicyBasedRouteId("policyBasedRouteId-18034589")
               .setPolicyBasedRoute(PolicyBasedRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           policyBasedRoutingServiceClient.createPolicyBasedRouteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreatePolicyBasedRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPolicyBasedRouteOperationCallable()
    
    
    public final OperationCallable<CreatePolicyBasedRouteRequest,PolicyBasedRoute,OperationMetadata> createPolicyBasedRouteOperationCallable()

Creates a new policy-based route in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       CreatePolicyBasedRouteRequest request =
           CreatePolicyBasedRouteRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPolicyBasedRouteId("policyBasedRouteId-18034589")
               .setPolicyBasedRoute(PolicyBasedRoute.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<PolicyBasedRoute, OperationMetadata> future =
           policyBasedRoutingServiceClient
               .createPolicyBasedRouteOperationCallable()
               .futureCall(request);
       // Do something.
       PolicyBasedRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreatePolicyBasedRouteRequest),[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deletePolicyBasedRouteAsync(@Nullable PolicyBasedRouteName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePolicyBasedRouteAsync(@Nullable PolicyBasedRouteName name)

Deletes a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       PolicyBasedRouteName name = PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]");
       policyBasedRoutingServiceClient.deletePolicyBasedRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.PolicyBasedRouteName`  
Required. Name of the policy-based route resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deletePolicyBasedRouteAsync(DeletePolicyBasedRouteRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePolicyBasedRouteAsync(DeletePolicyBasedRouteRequest request)

Deletes a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       DeletePolicyBasedRouteRequest request =
           DeletePolicyBasedRouteRequest.newBuilder()
               .setName(PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString())
               .setRequestId("requestId693933066")
               .build();
       policyBasedRoutingServiceClient.deletePolicyBasedRouteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeletePolicyBasedRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deletePolicyBasedRouteAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deletePolicyBasedRouteAsync(String name)

Deletes a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       String name = PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString();
       policyBasedRoutingServiceClient.deletePolicyBasedRouteAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the policy-based route resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deletePolicyBasedRouteCallable()
    
    
    public final UnaryCallable<DeletePolicyBasedRouteRequest,Operation> deletePolicyBasedRouteCallable()

Deletes a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       DeletePolicyBasedRouteRequest request =
           DeletePolicyBasedRouteRequest.newBuilder()
               .setName(PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           policyBasedRoutingServiceClient.deletePolicyBasedRouteCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeletePolicyBasedRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePolicyBasedRouteOperationCallable()
    
    
    public final OperationCallable<DeletePolicyBasedRouteRequest,Empty,OperationMetadata> deletePolicyBasedRouteOperationCallable()

Deletes a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       DeletePolicyBasedRouteRequest request =
           DeletePolicyBasedRouteRequest.newBuilder()
               .setName(PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           policyBasedRoutingServiceClient
               .deletePolicyBasedRouteOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeletePolicyBasedRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = policyBasedRoutingServiceClient.getIamPolicy(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           policyBasedRoutingServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = policyBasedRoutingServiceClient.getLocation(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           policyBasedRoutingServiceClient.getLocationCallable().futureCall(request);
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
  
### getPolicyBasedRoute(@Nullable PolicyBasedRouteName name)
    
    
    public final PolicyBasedRoute getPolicyBasedRoute(@Nullable PolicyBasedRouteName name)

Gets details of a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       PolicyBasedRouteName name = PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]");
       PolicyBasedRoute response = policyBasedRoutingServiceClient.getPolicyBasedRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.PolicyBasedRouteName`  
Required. Name of the PolicyBasedRoute resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)` |   
  
### getPolicyBasedRoute(GetPolicyBasedRouteRequest request)
    
    
    public final PolicyBasedRoute getPolicyBasedRoute(GetPolicyBasedRouteRequest request)

Gets details of a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetPolicyBasedRouteRequest request =
           GetPolicyBasedRouteRequest.newBuilder()
               .setName(PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString())
               .build();
       PolicyBasedRoute response = policyBasedRoutingServiceClient.getPolicyBasedRoute(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetPolicyBasedRouteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)` |   
  
### getPolicyBasedRoute(String name)
    
    
    public final PolicyBasedRoute getPolicyBasedRoute(String name)

Gets details of a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       String name = PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString();
       PolicyBasedRoute response = policyBasedRoutingServiceClient.getPolicyBasedRoute(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the PolicyBasedRoute resource to get.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)` |   
  
### getPolicyBasedRouteCallable()
    
    
    public final UnaryCallable<GetPolicyBasedRouteRequest,PolicyBasedRoute> getPolicyBasedRouteCallable()

Gets details of a single policy-based route.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       GetPolicyBasedRouteRequest request =
           GetPolicyBasedRouteRequest.newBuilder()
               .setName(PolicyBasedRouteName.of("[PROJECT]", "[POLICY_BASED_ROUTE]").toString())
               .build();
       ApiFuture<PolicyBasedRoute> future =
           policyBasedRoutingServiceClient.getPolicyBasedRouteCallable().futureCall(request);
       // Do something.
       PolicyBasedRoute response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPolicyBasedRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetPolicyBasedRouteRequest),[PolicyBasedRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoute)>` |   
  
### getSettings()
    
    
    public final @Nullable PolicyBasedRoutingServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceSettings` |   
  
### getStub()
    
    
    public PolicyBasedRoutingServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.PolicyBasedRoutingServiceStub)` |   
  
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
    
    
    public final PolicyBasedRoutingServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : policyBasedRoutingServiceClient.listLocations(request).iterateAll()) {
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
`[PolicyBasedRoutingServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             policyBasedRoutingServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,PolicyBasedRoutingServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           policyBasedRoutingServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListLocationsPagedResponse)>` |   
  
### listPolicyBasedRoutes(@Nullable LocationName parent)
    
    
    public final PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse listPolicyBasedRoutes(@Nullable LocationName parent)

Lists policy-based routes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PolicyBasedRoute element :
           policyBasedRoutingServiceClient.listPolicyBasedRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.networkconnectivity.v1.LocationName`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse)` |   
  
### listPolicyBasedRoutes(ListPolicyBasedRoutesRequest request)
    
    
    public final PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse listPolicyBasedRoutes(ListPolicyBasedRoutesRequest request)

Lists policy-based routes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListPolicyBasedRoutesRequest request =
           ListPolicyBasedRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (PolicyBasedRoute element :
           policyBasedRoutingServiceClient.listPolicyBasedRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPolicyBasedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse)` |   
  
### listPolicyBasedRoutes(String parent)
    
    
    public final PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse listPolicyBasedRoutes(String parent)

Lists policy-based routes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PolicyBasedRoute element :
           policyBasedRoutingServiceClient.listPolicyBasedRoutes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource's name.  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse)` |   
  
### listPolicyBasedRoutesCallable()
    
    
    public final UnaryCallable<ListPolicyBasedRoutesRequest,ListPolicyBasedRoutesResponse> listPolicyBasedRoutesCallable()

Lists policy-based routes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListPolicyBasedRoutesRequest request =
           ListPolicyBasedRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListPolicyBasedRoutesResponse response =
             policyBasedRoutingServiceClient.listPolicyBasedRoutesCallable().call(request);
         for (PolicyBasedRoute element : response.getPolicyBasedRoutesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPolicyBasedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesRequest),[ListPolicyBasedRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesResponse)>` |   
  
### listPolicyBasedRoutesPagedCallable()
    
    
    public final UnaryCallable<ListPolicyBasedRoutesRequest,PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse> listPolicyBasedRoutesPagedCallable()

Lists policy-based routes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       ListPolicyBasedRoutesRequest request =
           ListPolicyBasedRoutesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<PolicyBasedRoute> future =
           policyBasedRoutingServiceClient.listPolicyBasedRoutesPagedCallable().futureCall(request);
       // Do something.
       for (PolicyBasedRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPolicyBasedRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListPolicyBasedRoutesRequest),[ListPolicyBasedRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.PolicyBasedRoutingServiceClient.ListPolicyBasedRoutesPagedResponse)>` |   
  
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = policyBasedRoutingServiceClient.setIamPolicy(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           policyBasedRoutingServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           policyBasedRoutingServiceClient.testIamPermissions(request);
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
     try (PolicyBasedRoutingServiceClient policyBasedRoutingServiceClient =
         PolicyBasedRoutingServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(GroupName.of("[PROJECT]", "[HUB]", "[GROUP]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           policyBasedRoutingServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
