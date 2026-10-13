---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient
title: Class BackendServicesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:09.301680+00:00
---

# Class BackendServicesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackendServicesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/BackendServicesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The BackendServices API.

This client uses BackendServices version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       BackendService response = backendServicesClient.get(project, backendService);
     }
     

Note: close() needs to be called on the BackendServicesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddSignedUrlKey |  Adds a key for validating requests with signed URLs for this backend service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addSignedUrlKeyAsync(AddSignedUrlKeyBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addSignedUrlKeyAsync(String project, String backendService, SignedUrlKey signedUrlKeyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addSignedUrlKeyOperationCallable() 
  * addSignedUrlKeyCallable() 

  
AggregatedList |  Retrieves the list of all BackendService resources, regional and global, available to the specified project.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListBackendServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified BackendService resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String backendService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteSignedUrlKey |  Deletes a key for validating requests with signed URLs for this backend service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSignedUrlKeyAsync(String project, String backendService, String keyName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSignedUrlKeyOperationCallable() 
  * deleteSignedUrlKeyCallable() 

  
Get |  Returns the specified BackendService resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String backendService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetEffectiveSecurityPolicies |  Returns effective security policies applied to this backend service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEffectiveSecurityPolicies(GetEffectiveSecurityPoliciesBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEffectiveSecurityPolicies(String project, String backendService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEffectiveSecurityPoliciesCallable() 

  
GetHealth |  Gets the most recent health check results for this BackendService.  Example request body:  { "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" } |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHealth(GetHealthBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHealth(String project, String backendService, ResourceGroupReference resourceGroupReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHealthCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, BackendService backendServiceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of BackendService resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListBackendServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListUsable |  Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUsable(ListUsableBackendServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUsable(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUsablePagedCallable() 
  * listUsableCallable() 

  
Patch |  Patches the specified BackendService resource with the data included in the request. For more information, see Backend services overview. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String backendService, BackendService backendServiceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetEdgeSecurityPolicy |  Sets the edge security policy for the specified backend service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setEdgeSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setEdgeSecurityPolicyOperationCallable() 
  * setEdgeSecurityPolicyCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetSecurityPolicy |  Sets the Google Cloud Armor security policy for the specified backend service. For more information, seeGoogle Cloud Armor Overview |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSecurityPolicyAsync(SetSecurityPolicyBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSecurityPolicyOperationCallable() 
  * setSecurityPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsBackendServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates the specified BackendService resource with the data included in the request. For more information, seeBackend services overview. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateBackendServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String backendService, BackendService backendServiceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BackendServicesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackendServicesSettings backendServicesSettings =
         BackendServicesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BackendServicesClient backendServicesClient =
         BackendServicesClient.create(backendServicesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackendServicesSettings backendServicesSettings =
         BackendServicesSettings.newBuilder().setEndpoint(myEndpoint).build();
     BackendServicesClient backendServicesClient =
         BackendServicesClient.create(backendServicesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BackendServicesClient

## Static Methods 

### create()
    
    
    public static final BackendServicesClient create()

Constructs an instance of BackendServicesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackendServicesSettings settings)
    
    
    public static final BackendServicesClient create(BackendServicesSettings settings)

Constructs an instance of BackendServicesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackendServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BackendServicesStub stub)
    
    
    public static final BackendServicesClient create(BackendServicesStub stub)

Constructs an instance of BackendServicesClient, using the given stub for making calls. This is for advanced usage - prefer using create(BackendServicesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackendServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendServicesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient)` |   
  
## Constructors 

### BackendServicesClient(BackendServicesSettings settings)
    
    
    protected BackendServicesClient(BackendServicesSettings settings)

Constructs an instance of BackendServicesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BackendServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesSettings)`  
  
  
### BackendServicesClient(BackendServicesStub stub)
    
    
    protected BackendServicesClient(BackendServicesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BackendServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendServicesStub)`  
  
  
## Methods 

### addSignedUrlKeyAsync(AddSignedUrlKeyBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> addSignedUrlKeyAsync(AddSignedUrlKeyBackendServiceRequest request)

Adds a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AddSignedUrlKeyBackendServiceRequest request =
           AddSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       Operation response = backendServicesClient.addSignedUrlKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyAsync(String project, String backendService, SignedUrlKey signedUrlKeyResource)
    
    
    public final OperationFuture<Operation,Operation> addSignedUrlKeyAsync(String project, String backendService, SignedUrlKey signedUrlKeyResource)

Adds a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       SignedUrlKey signedUrlKeyResource = SignedUrlKey.newBuilder().build();
       Operation response =
           backendServicesClient
               .addSignedUrlKeyAsync(project, backendService, signedUrlKeyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to which the Signed URL Key should be added. The name should conform to RFC1035.  
`signedUrlKeyResource` | `[SignedUrlKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SignedUrlKey)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyCallable()
    
    
    public final UnaryCallable<AddSignedUrlKeyBackendServiceRequest,Operation> addSignedUrlKeyCallable()

Adds a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AddSignedUrlKeyBackendServiceRequest request =
           AddSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           backendServicesClient.addSignedUrlKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addSignedUrlKeyOperationCallable()
    
    
    public final OperationCallable<AddSignedUrlKeyBackendServiceRequest,Operation,Operation> addSignedUrlKeyOperationCallable()

Adds a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AddSignedUrlKeyBackendServiceRequest request =
           AddSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSignedUrlKeyResource(SignedUrlKey.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.addSignedUrlKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddSignedUrlKeyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListBackendServicesRequest request)
    
    
    public final BackendServicesClient.AggregatedListPagedResponse aggregatedList(AggregatedListBackendServicesRequest request)

Retrieves the list of all BackendService resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AggregatedListBackendServicesRequest request =
           AggregatedListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, BackendServicesScopedList> element :
           backendServicesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final BackendServicesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all BackendService resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, BackendServicesScopedList> element :
           backendServicesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListBackendServicesRequest,BackendServiceAggregatedList> aggregatedListCallable()

Retrieves the list of all BackendService resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AggregatedListBackendServicesRequest request =
           AggregatedListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         BackendServiceAggregatedList response =
             backendServicesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, BackendServicesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendServicesRequest),[BackendServiceAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListBackendServicesRequest,BackendServicesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all BackendService resources, regional and global, available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       AggregatedListBackendServicesRequest request =
           AggregatedListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, BackendServicesScopedList>> future =
           backendServicesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, BackendServicesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListBackendServicesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteBackendServiceRequest request)

Deletes the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteBackendServiceRequest request =
           DeleteBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendServicesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String backendService)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String backendService)

Deletes the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       Operation response = backendServicesClient.deleteAsync(project, backendService).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteBackendServiceRequest,Operation> deleteCallable()

Deletes the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteBackendServiceRequest request =
           DeleteBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendServicesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteBackendServiceRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteBackendServiceRequest request =
           DeleteBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteSignedUrlKeyAsync(DeleteSignedUrlKeyBackendServiceRequest request)

Deletes a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteSignedUrlKeyBackendServiceRequest request =
           DeleteSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendServicesClient.deleteSignedUrlKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyAsync(String project, String backendService, String keyName)
    
    
    public final OperationFuture<Operation,Operation> deleteSignedUrlKeyAsync(String project, String backendService, String keyName)

Deletes a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       String keyName = "keyName-815643254";
       Operation response =
           backendServicesClient.deleteSignedUrlKeyAsync(project, backendService, keyName).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to which the Signed URL Key should be added. The name should conform to RFC1035.  
`keyName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the Signed URL Key to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyCallable()
    
    
    public final UnaryCallable<DeleteSignedUrlKeyBackendServiceRequest,Operation> deleteSignedUrlKeyCallable()

Deletes a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteSignedUrlKeyBackendServiceRequest request =
           DeleteSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           backendServicesClient.deleteSignedUrlKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSignedUrlKeyOperationCallable()
    
    
    public final OperationCallable<DeleteSignedUrlKeyBackendServiceRequest,Operation,Operation> deleteSignedUrlKeyOperationCallable()

Deletes a key for validating requests with signed URLs for this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       DeleteSignedUrlKeyBackendServiceRequest request =
           DeleteSignedUrlKeyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setKeyName("keyName-815643254")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.deleteSignedUrlKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSignedUrlKeyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSignedUrlKeyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetBackendServiceRequest request)
    
    
    public final BackendService get(GetBackendServiceRequest request)

Returns the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetBackendServiceRequest request =
           GetBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .build();
       BackendService response = backendServicesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)` |   
  
### get(String project, String backendService)
    
    
    public final BackendService get(String project, String backendService)

Returns the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       BackendService response = backendServicesClient.get(project, backendService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetBackendServiceRequest,BackendService> getCallable()

Returns the specified BackendService resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetBackendServiceRequest request =
           GetBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendService> future = backendServicesClient.getCallable().futureCall(request);
       // Do something.
       BackendService response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetBackendServiceRequest),[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)>` |   
  
### getEffectiveSecurityPolicies(GetEffectiveSecurityPoliciesBackendServiceRequest request)
    
    
    public final GetEffectiveSecurityPoliciesBackendServiceResponse getEffectiveSecurityPolicies(GetEffectiveSecurityPoliciesBackendServiceRequest request)

Returns effective security policies applied to this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetEffectiveSecurityPoliciesBackendServiceRequest request =
           GetEffectiveSecurityPoliciesBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .build();
       GetEffectiveSecurityPoliciesBackendServiceResponse response =
           backendServicesClient.getEffectiveSecurityPolicies(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEffectiveSecurityPoliciesBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveSecurityPoliciesBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GetEffectiveSecurityPoliciesBackendServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveSecurityPoliciesBackendServiceResponse)` |   
  
### getEffectiveSecurityPolicies(String project, String backendService)
    
    
    public final GetEffectiveSecurityPoliciesBackendServiceResponse getEffectiveSecurityPolicies(String project, String backendService)

Returns effective security policies applied to this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       GetEffectiveSecurityPoliciesBackendServiceResponse response =
           backendServicesClient.getEffectiveSecurityPolicies(project, backendService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Backend Service for this request.  
**Returns**  
---  
**Type** | **Description**  
`[GetEffectiveSecurityPoliciesBackendServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveSecurityPoliciesBackendServiceResponse)` |   
  
### getEffectiveSecurityPoliciesCallable()
    
    
    public final UnaryCallable<GetEffectiveSecurityPoliciesBackendServiceRequest,GetEffectiveSecurityPoliciesBackendServiceResponse> getEffectiveSecurityPoliciesCallable()

Returns effective security policies applied to this backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetEffectiveSecurityPoliciesBackendServiceRequest request =
           GetEffectiveSecurityPoliciesBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .build();
       ApiFuture<GetEffectiveSecurityPoliciesBackendServiceResponse> future =
           backendServicesClient.getEffectiveSecurityPoliciesCallable().futureCall(request);
       // Do something.
       GetEffectiveSecurityPoliciesBackendServiceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEffectiveSecurityPoliciesBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveSecurityPoliciesBackendServiceRequest),[GetEffectiveSecurityPoliciesBackendServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveSecurityPoliciesBackendServiceResponse)>` |   
  
### getHealth(GetHealthBackendServiceRequest request)
    
    
    public final BackendServiceGroupHealth getHealth(GetHealthBackendServiceRequest request)

Gets the most recent health check results for this BackendService.

Example request body:

{ "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" }

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetHealthBackendServiceRequest request =
           GetHealthBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setResourceGroupReferenceResource(ResourceGroupReference.newBuilder().build())
               .build();
       BackendServiceGroupHealth response = backendServicesClient.getHealth(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHealthBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServiceGroupHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceGroupHealth)` |   
  
### getHealth(String project, String backendService, ResourceGroupReference resourceGroupReferenceResource)
    
    
    public final BackendServiceGroupHealth getHealth(String project, String backendService, ResourceGroupReference resourceGroupReferenceResource)

Gets the most recent health check results for this BackendService.

Example request body:

{ "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" }

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       ResourceGroupReference resourceGroupReferenceResource =
           ResourceGroupReference.newBuilder().build();
       BackendServiceGroupHealth response =
           backendServicesClient.getHealth(project, backendService, resourceGroupReferenceResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to which the queried instance belongs.  
`resourceGroupReferenceResource` | `[ResourceGroupReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourceGroupReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[BackendServiceGroupHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceGroupHealth)` |   
  
### getHealthCallable()
    
    
    public final UnaryCallable<GetHealthBackendServiceRequest,BackendServiceGroupHealth> getHealthCallable()

Gets the most recent health check results for this BackendService.

Example request body:

{ "group": "/zones/us-east1-b/instanceGroups/lb-backend-example" }

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetHealthBackendServiceRequest request =
           GetHealthBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setResourceGroupReferenceResource(ResourceGroupReference.newBuilder().build())
               .build();
       ApiFuture<BackendServiceGroupHealth> future =
           backendServicesClient.getHealthCallable().futureCall(request);
       // Do something.
       BackendServiceGroupHealth response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHealthBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthBackendServiceRequest),[BackendServiceGroupHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceGroupHealth)>` |   
  
### getIamPolicy(GetIamPolicyBackendServiceRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyBackendServiceRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetIamPolicyBackendServiceRequest request =
           GetIamPolicyBackendServiceRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = backendServicesClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = backendServicesClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyBackendServiceRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       GetIamPolicyBackendServiceRequest request =
           GetIamPolicyBackendServiceRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = backendServicesClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyBackendServiceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable BackendServicesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.BackendServicesSettings` |   
  
### getStub()
    
    
    public BackendServicesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BackendServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.BackendServicesStub)` |   
  
### insertAsync(InsertBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertBackendServiceRequest request)

Creates a BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       InsertBackendServiceRequest request =
           InsertBackendServiceRequest.newBuilder()
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendServicesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, BackendService backendServiceResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, BackendService backendServiceResource)

Creates a BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       BackendService backendServiceResource = BackendService.newBuilder().build();
       Operation response = backendServicesClient.insertAsync(project, backendServiceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendServiceResource` | `[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertBackendServiceRequest,Operation> insertCallable()

Creates a BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       InsertBackendServiceRequest request =
           InsertBackendServiceRequest.newBuilder()
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendServicesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertBackendServiceRequest,Operation,Operation> insertOperationCallable()

Creates a BackendService resource in the specified project using the data included in the request. For more information, see Backend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       InsertBackendServiceRequest request =
           InsertBackendServiceRequest.newBuilder()
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListBackendServicesRequest request)
    
    
    public final BackendServicesClient.ListPagedResponse list(ListBackendServicesRequest request)

Retrieves the list of BackendService resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListBackendServicesRequest request =
           ListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (BackendService element : backendServicesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final BackendServicesClient.ListPagedResponse list(String project)

Retrieves the list of BackendService resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       for (BackendService element : backendServicesClient.list(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListBackendServicesRequest,BackendServiceList> listCallable()

Retrieves the list of BackendService resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListBackendServicesRequest request =
           ListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         BackendServiceList response = backendServicesClient.listCallable().call(request);
         for (BackendService element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendServicesRequest),[BackendServiceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListBackendServicesRequest,BackendServicesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of BackendService resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListBackendServicesRequest request =
           ListBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendService> future =
           backendServicesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (BackendService element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBackendServicesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListPagedResponse)>` |   
  
### listUsable(ListUsableBackendServicesRequest request)
    
    
    public final BackendServicesClient.ListUsablePagedResponse listUsable(ListUsableBackendServicesRequest request)

Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListUsableBackendServicesRequest request =
           ListUsableBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (BackendService element : backendServicesClient.listUsable(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUsableBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListUsablePagedResponse)` |   
  
### listUsable(String project)
    
    
    public final BackendServicesClient.ListUsablePagedResponse listUsable(String project)

Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       for (BackendService element : backendServicesClient.listUsable(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[BackendServicesClient.ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListUsablePagedResponse)` |   
  
### listUsableCallable()
    
    
    public final UnaryCallable<ListUsableBackendServicesRequest,BackendServiceListUsable> listUsableCallable()

Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListUsableBackendServicesRequest request =
           ListUsableBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         BackendServiceListUsable response =
             backendServicesClient.listUsableCallable().call(request);
         for (BackendService element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendServicesRequest),[BackendServiceListUsable](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServiceListUsable)>` |   
  
### listUsablePagedCallable()
    
    
    public final UnaryCallable<ListUsableBackendServicesRequest,BackendServicesClient.ListUsablePagedResponse> listUsablePagedCallable()

Retrieves a list of all usable backend services for Application Load Balancers and Proxy Network Load Balancers in the specified project. Backend services for external and internal passthrough Network Load Balancers are not included in the response.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       ListUsableBackendServicesRequest request =
           ListUsableBackendServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackendService> future =
           backendServicesClient.listUsablePagedCallable().futureCall(request);
       // Do something.
       for (BackendService element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUsableBackendServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUsableBackendServicesRequest),[ListUsablePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendServicesClient.ListUsablePagedResponse)>` |   
  
### patchAsync(PatchBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchBackendServiceRequest request)

Patches the specified BackendService resource with the data included in the request. For more information, see Backend services overview. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       PatchBackendServiceRequest request =
           PatchBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendServicesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String backendService, BackendService backendServiceResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String backendService, BackendService backendServiceResource)

Patches the specified BackendService resource with the data included in the request. For more information, see Backend services overview. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       BackendService backendServiceResource = BackendService.newBuilder().build();
       Operation response =
           backendServicesClient.patchAsync(project, backendService, backendServiceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to patch.  
`backendServiceResource` | `[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchBackendServiceRequest,Operation> patchCallable()

Patches the specified BackendService resource with the data included in the request. For more information, see Backend services overview. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       PatchBackendServiceRequest request =
           PatchBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendServicesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchBackendServiceRequest,Operation,Operation> patchOperationCallable()

Patches the specified BackendService resource with the data included in the request. For more information, see Backend services overview. This method supports PATCH semantics and uses the JSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       PatchBackendServiceRequest request =
           PatchBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setEdgeSecurityPolicyAsync(SetEdgeSecurityPolicyBackendServiceRequest request)

Sets the edge security policy for the specified backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetEdgeSecurityPolicyBackendServiceRequest request =
           SetEdgeSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       Operation response = backendServicesClient.setEdgeSecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetEdgeSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setEdgeSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource)

Sets the edge security policy for the specified backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       SecurityPolicyReference securityPolicyReferenceResource =
           SecurityPolicyReference.newBuilder().build();
       Operation response =
           backendServicesClient
               .setEdgeSecurityPolicyAsync(project, backendService, securityPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to which the edge security policy should be set. The name should conform to RFC1035.  
`securityPolicyReferenceResource` | `[SecurityPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyCallable()
    
    
    public final UnaryCallable<SetEdgeSecurityPolicyBackendServiceRequest,Operation> setEdgeSecurityPolicyCallable()

Sets the edge security policy for the specified backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetEdgeSecurityPolicyBackendServiceRequest request =
           SetEdgeSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           backendServicesClient.setEdgeSecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetEdgeSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setEdgeSecurityPolicyOperationCallable()
    
    
    public final OperationCallable<SetEdgeSecurityPolicyBackendServiceRequest,Operation,Operation> setEdgeSecurityPolicyOperationCallable()

Sets the edge security policy for the specified backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetEdgeSecurityPolicyBackendServiceRequest request =
           SetEdgeSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.setEdgeSecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetEdgeSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetEdgeSecurityPolicyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyBackendServiceRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyBackendServiceRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetIamPolicyBackendServiceRequest request =
           SetIamPolicyBackendServiceRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = backendServicesClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           backendServicesClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyBackendServiceRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetIamPolicyBackendServiceRequest request =
           SetIamPolicyBackendServiceRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = backendServicesClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyBackendServiceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setSecurityPolicyAsync(SetSecurityPolicyBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(SetSecurityPolicyBackendServiceRequest request)

Sets the Google Cloud Armor security policy for the specified backend service. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetSecurityPolicyBackendServiceRequest request =
           SetSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       Operation response = backendServicesClient.setSecurityPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setSecurityPolicyAsync(String project, String backendService, SecurityPolicyReference securityPolicyReferenceResource)

Sets the Google Cloud Armor security policy for the specified backend service. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       SecurityPolicyReference securityPolicyReferenceResource =
           SecurityPolicyReference.newBuilder().build();
       Operation response =
           backendServicesClient
               .setSecurityPolicyAsync(project, backendService, securityPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to which the security policy should be set. The name should conform to RFC1035.  
`securityPolicyReferenceResource` | `[SecurityPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyCallable()
    
    
    public final UnaryCallable<SetSecurityPolicyBackendServiceRequest,Operation> setSecurityPolicyCallable()

Sets the Google Cloud Armor security policy for the specified backend service. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetSecurityPolicyBackendServiceRequest request =
           SetSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           backendServicesClient.setSecurityPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyOperationCallable()
    
    
    public final OperationCallable<SetSecurityPolicyBackendServiceRequest,Operation,Operation> setSecurityPolicyOperationCallable()

Sets the Google Cloud Armor security policy for the specified backend service. For more information, seeGoogle Cloud Armor Overview

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       SetSecurityPolicyBackendServiceRequest request =
           SetSecurityPolicyBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSecurityPolicyReferenceResource(SecurityPolicyReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.setSecurityPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSecurityPolicyBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsBackendServiceRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsBackendServiceRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       TestIamPermissionsBackendServiceRequest request =
           TestIamPermissionsBackendServiceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = backendServicesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           backendServicesClient.testIamPermissions(
               project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsBackendServiceRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       TestIamPermissionsBackendServiceRequest request =
           TestIamPermissionsBackendServiceRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           backendServicesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsBackendServiceRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateBackendServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateBackendServiceRequest request)

Updates the specified BackendService resource with the data included in the request. For more information, seeBackend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       UpdateBackendServiceRequest request =
           UpdateBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = backendServicesClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String backendService, BackendService backendServiceResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String backendService, BackendService backendServiceResource)

Updates the specified BackendService resource with the data included in the request. For more information, seeBackend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       String project = "project-309310695";
       String backendService = "backendService-1884714623";
       BackendService backendServiceResource = BackendService.newBuilder().build();
       Operation response =
           backendServicesClient.updateAsync(project, backendService, backendServiceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`backendService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the BackendService resource to update.  
`backendServiceResource` | `[BackendService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendService)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateBackendServiceRequest,Operation> updateCallable()

Updates the specified BackendService resource with the data included in the request. For more information, seeBackend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       UpdateBackendServiceRequest request =
           UpdateBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = backendServicesClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateBackendServiceRequest,Operation,Operation> updateOperationCallable()

Updates the specified BackendService resource with the data included in the request. For more information, seeBackend services overview.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BackendServicesClient backendServicesClient = BackendServicesClient.create()) {
       UpdateBackendServiceRequest request =
           UpdateBackendServiceRequest.newBuilder()
               .setBackendService("backendService-1884714623")
               .setBackendServiceResource(BackendService.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           backendServicesClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateBackendServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
