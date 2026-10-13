---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient
title: Class AuthProviderServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:02.093277+00:00
---

# Class AuthProviderServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthProviderServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-agentidentity/google-cloud-agentidentity/src/main/java/com/google/cloud/agentidentity/v1beta/AuthProviderServiceClient.java)| [Product Reference](https://cloud.google.com/agentidentity/)  
---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       AuthProvider response = authProviderServiceClient.getAuthProvider(name);
     }
     

Note: close() needs to be called on the AuthProviderServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListAuthProviders |  Lists AuthProviders in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthProviders(ListAuthProvidersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthProviders(LocationName parent) 
  * listAuthProviders(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthProvidersPagedCallable() 
  * listAuthProvidersCallable() 

  
GetAuthProvider |  Gets details of a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthProvider(GetAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthProvider(AuthProviderName name) 
  * getAuthProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthProviderCallable() 

  
CreateAuthProvider |  Creates a new AuthProvider in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAuthProvider(CreateAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAuthProvider(LocationName parent, AuthProvider authProvider, String authProviderId) 
  * createAuthProvider(String parent, AuthProvider authProvider, String authProviderId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAuthProviderCallable() 

  
UpdateAuthProvider |  Updates the parameters of a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAuthProvider(UpdateAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAuthProvider(AuthProvider authProvider, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAuthProviderCallable() 

  
DeleteAuthProvider |  Deletes a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthProvider(DeleteAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAuthProvider(AuthProviderName name) 
  * deleteAuthProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthProviderCallable() 

  
UndeleteAuthProvider |  Undeletes a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeleteAuthProvider(UndeleteAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * undeleteAuthProvider(AuthProviderName name) 
  * undeleteAuthProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeleteAuthProviderCallable() 

  
QueryAuthProviders |  Queries what all auth_providers are used by a given workload_id. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryAuthProviders(QueryAuthProvidersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryAuthProviders(LocationName parent, String workloadId) 
  * queryAuthProviders(String parent, String workloadId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryAuthProvidersPagedCallable() 
  * queryAuthProvidersCallable() 

  
QueryWorkloads |  Queries what all workloads are using a given auth_provider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryWorkloads(QueryWorkloadsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * queryWorkloads(AuthProviderName name) 
  * queryWorkloads(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryWorkloadsPagedCallable() 
  * queryWorkloadsCallable() 

  
ListAuthorizations |  Lists Authorizations in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthorizations(ListAuthorizationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthorizations(AuthProviderName parent) 
  * listAuthorizations(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthorizationsPagedCallable() 
  * listAuthorizationsCallable() 

  
GetAuthorization |  Gets details of a single Authorization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthorization(GetAuthorizationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthorization(AuthorizationName name) 
  * getAuthorization(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthorizationCallable() 

  
DeleteAuthorization |  Deletes a single Authorization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthorization(DeleteAuthorizationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAuthorization(AuthorizationName name) 
  * deleteAuthorization(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthorizationCallable() 

  
ListAccessSummaries |  Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAccessSummaries(ListAccessSummariesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAccessSummaries(LocationName parent) 
  * listAccessSummaries(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAccessSummariesPagedCallable() 
  * listAccessSummariesCallable() 

  
GetAccessSummary |  Gets details of a single AccessSummary. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAccessSummary(GetAccessSummaryRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAccessSummary(AccessSummaryName name) 
  * getAccessSummary(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAccessSummaryCallable() 

  
RevokeAuthorization |  Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * revokeAuthorization(RevokeAuthorizationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * revokeAuthorization(AuthProviderName name, String userId) 
  * revokeAuthorization(String name, String userId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * revokeAuthorizationCallable() 

  
EnableAuthProvider |  Enables a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableAuthProvider(EnableAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * enableAuthProvider(AuthProviderName name) 
  * enableAuthProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableAuthProviderCallable() 

  
DisableAuthProvider |  Disables a single AuthProvider. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableAuthProvider(DisableAuthProviderRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * disableAuthProvider(AuthProviderName name) 
  * disableAuthProvider(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableAuthProviderCallable() 

  
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

This class can be customized by passing in a custom instance of AuthProviderServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuthProviderServiceSettings authProviderServiceSettings =
         AuthProviderServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AuthProviderServiceClient authProviderServiceClient =
         AuthProviderServiceClient.create(authProviderServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuthProviderServiceSettings authProviderServiceSettings =
         AuthProviderServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AuthProviderServiceClient authProviderServiceClient =
         AuthProviderServiceClient.create(authProviderServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AuthProviderServiceSettings authProviderServiceSettings =
         AuthProviderServiceSettings.newHttpJsonBuilder().build();
     AuthProviderServiceClient authProviderServiceClient =
         AuthProviderServiceClient.create(authProviderServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AuthProviderServiceClient

## Static Methods 

### create()
    
    
    public static final AuthProviderServiceClient create()

Constructs an instance of AuthProviderServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AuthProviderServiceSettings settings)
    
    
    public static final AuthProviderServiceClient create(AuthProviderServiceSettings settings)

Constructs an instance of AuthProviderServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AuthProviderServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AuthProviderServiceStub stub)
    
    
    public static final AuthProviderServiceClient create(AuthProviderServiceStub stub)

Constructs an instance of AuthProviderServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AuthProviderServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AuthProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.stub.AuthProviderServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient)` |   
  
## Constructors 

### AuthProviderServiceClient(AuthProviderServiceSettings settings)
    
    
    protected AuthProviderServiceClient(AuthProviderServiceSettings settings)

Constructs an instance of AuthProviderServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AuthProviderServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceSettings)`  
  
  
### AuthProviderServiceClient(AuthProviderServiceStub stub)
    
    
    protected AuthProviderServiceClient(AuthProviderServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AuthProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.stub.AuthProviderServiceStub)`  
  
  
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

### createAuthProvider(@Nullable LocationName parent, AuthProvider authProvider, String authProviderId)
    
    
    public final AuthProvider createAuthProvider(@Nullable LocationName parent, AuthProvider authProvider, String authProviderId)

Creates a new AuthProvider in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       AuthProvider authProvider = AuthProvider.newBuilder().build();
       String authProviderId = "authProviderId325000884";
       AuthProvider response =
           authProviderServiceClient.createAuthProvider(parent, authProvider, authProviderId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.LocationName`  
Required. The parent resource where the AuthProvider is created. Format: projects/{project}/locations/{location}  
`authProvider` | `[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)`  
Required. The AuthProvider to create.  
`authProviderId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the AuthProvider, which will become the final segment of the AuthProvider's resource name. This value should be 1-63 characters, and valid characters are /a-z-/. The first character must be a lowercase letter, and the last character must be a lowercase letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### createAuthProvider(CreateAuthProviderRequest request)
    
    
    public final AuthProvider createAuthProvider(CreateAuthProviderRequest request)

Creates a new AuthProvider in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       CreateAuthProviderRequest request =
           CreateAuthProviderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthProviderId("authProviderId325000884")
               .setAuthProvider(AuthProvider.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthProvider response = authProviderServiceClient.createAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.CreateAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### createAuthProvider(String parent, AuthProvider authProvider, String authProviderId)
    
    
    public final AuthProvider createAuthProvider(String parent, AuthProvider authProvider, String authProviderId)

Creates a new AuthProvider in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       AuthProvider authProvider = AuthProvider.newBuilder().build();
       String authProviderId = "authProviderId325000884";
       AuthProvider response =
           authProviderServiceClient.createAuthProvider(parent, authProvider, authProviderId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the AuthProvider is created. Format: projects/{project}/locations/{location}  
`authProvider` | `[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)`  
Required. The AuthProvider to create.  
`authProviderId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the AuthProvider, which will become the final segment of the AuthProvider's resource name. This value should be 1-63 characters, and valid characters are /a-z-/. The first character must be a lowercase letter, and the last character must be a lowercase letter or a number.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### createAuthProviderCallable()
    
    
    public final UnaryCallable<CreateAuthProviderRequest,AuthProvider> createAuthProviderCallable()

Creates a new AuthProvider in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       CreateAuthProviderRequest request =
           CreateAuthProviderRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setAuthProviderId("authProviderId325000884")
               .setAuthProvider(AuthProvider.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.createAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.CreateAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
### deleteAuthProvider(@Nullable AuthProviderName name)
    
    
    public final void deleteAuthProvider(@Nullable AuthProviderName name)

Deletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       authProviderServiceClient.deleteAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. Name of the resource  
  
### deleteAuthProvider(DeleteAuthProviderRequest request)
    
    
    public final void deleteAuthProvider(DeleteAuthProviderRequest request)

Deletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DeleteAuthProviderRequest request =
           DeleteAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       authProviderServiceClient.deleteAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DeleteAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAuthProvider(String name)
    
    
    public final void deleteAuthProvider(String name)

Deletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       authProviderServiceClient.deleteAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
  
### deleteAuthProviderCallable()
    
    
    public final UnaryCallable<DeleteAuthProviderRequest,Empty> deleteAuthProviderCallable()

Deletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DeleteAuthProviderRequest request =
           DeleteAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future =
           authProviderServiceClient.deleteAuthProviderCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DeleteAuthProviderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteAuthorization(@Nullable AuthorizationName name)
    
    
    public final void deleteAuthorization(@Nullable AuthorizationName name)

Deletes a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthorizationName name =
           AuthorizationName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]");
       authProviderServiceClient.deleteAuthorization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthorizationName`  
Required. The name of the Authorization to delete. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}/authorizations/{authorization}  
  
### deleteAuthorization(DeleteAuthorizationRequest request)
    
    
    public final void deleteAuthorization(DeleteAuthorizationRequest request)

Deletes a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DeleteAuthorizationRequest request =
           DeleteAuthorizationRequest.newBuilder()
               .setName(
                   AuthorizationName.of(
                           "[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       authProviderServiceClient.deleteAuthorization(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DeleteAuthorizationRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAuthorization(String name)
    
    
    public final void deleteAuthorization(String name)

Deletes a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name =
           AuthorizationName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
               .toString();
       authProviderServiceClient.deleteAuthorization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Authorization to delete. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}/authorizations/{authorization}  
  
### deleteAuthorizationCallable()
    
    
    public final UnaryCallable<DeleteAuthorizationRequest,Empty> deleteAuthorizationCallable()

Deletes a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DeleteAuthorizationRequest request =
           DeleteAuthorizationRequest.newBuilder()
               .setName(
                   AuthorizationName.of(
                           "[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Empty> future =
           authProviderServiceClient.deleteAuthorizationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DeleteAuthorizationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### disableAuthProvider(@Nullable AuthProviderName name)
    
    
    public final AuthProvider disableAuthProvider(@Nullable AuthProviderName name)

Disables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       AuthProvider response = authProviderServiceClient.disableAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### disableAuthProvider(DisableAuthProviderRequest request)
    
    
    public final AuthProvider disableAuthProvider(DisableAuthProviderRequest request)

Disables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DisableAuthProviderRequest request =
           DisableAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       AuthProvider response = authProviderServiceClient.disableAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DisableAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### disableAuthProvider(String name)
    
    
    public final AuthProvider disableAuthProvider(String name)

Disables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       AuthProvider response = authProviderServiceClient.disableAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### disableAuthProviderCallable()
    
    
    public final UnaryCallable<DisableAuthProviderRequest,AuthProvider> disableAuthProviderCallable()

Disables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       DisableAuthProviderRequest request =
           DisableAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.disableAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.DisableAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
### enableAuthProvider(@Nullable AuthProviderName name)
    
    
    public final AuthProvider enableAuthProvider(@Nullable AuthProviderName name)

Enables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       AuthProvider response = authProviderServiceClient.enableAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### enableAuthProvider(EnableAuthProviderRequest request)
    
    
    public final AuthProvider enableAuthProvider(EnableAuthProviderRequest request)

Enables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       EnableAuthProviderRequest request =
           EnableAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       AuthProvider response = authProviderServiceClient.enableAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.EnableAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### enableAuthProvider(String name)
    
    
    public final AuthProvider enableAuthProvider(String name)

Enables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       AuthProvider response = authProviderServiceClient.enableAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### enableAuthProviderCallable()
    
    
    public final UnaryCallable<EnableAuthProviderRequest,AuthProvider> enableAuthProviderCallable()

Enables a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       EnableAuthProviderRequest request =
           EnableAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.enableAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.EnableAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
### getAccessSummary(@Nullable AccessSummaryName name)
    
    
    public final AccessSummary getAccessSummary(@Nullable AccessSummaryName name)

Gets details of a single AccessSummary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AccessSummaryName name = AccessSummaryName.of("[PROJECT]", "[LOCATION]", "[ACCESS_SUMMARY]");
       AccessSummary response = authProviderServiceClient.getAccessSummary(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AccessSummaryName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AccessSummary)` |   
  
### getAccessSummary(GetAccessSummaryRequest request)
    
    
    public final AccessSummary getAccessSummary(GetAccessSummaryRequest request)

Gets details of a single AccessSummary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAccessSummaryRequest request =
           GetAccessSummaryRequest.newBuilder()
               .setName(
                   AccessSummaryName.of("[PROJECT]", "[LOCATION]", "[ACCESS_SUMMARY]").toString())
               .build();
       AccessSummary response = authProviderServiceClient.getAccessSummary(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAccessSummaryRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AccessSummary)` |   
  
### getAccessSummary(String name)
    
    
    public final AccessSummary getAccessSummary(String name)

Gets details of a single AccessSummary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AccessSummaryName.of("[PROJECT]", "[LOCATION]", "[ACCESS_SUMMARY]").toString();
       AccessSummary response = authProviderServiceClient.getAccessSummary(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AccessSummary)` |   
  
### getAccessSummaryCallable()
    
    
    public final UnaryCallable<GetAccessSummaryRequest,AccessSummary> getAccessSummaryCallable()

Gets details of a single AccessSummary.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAccessSummaryRequest request =
           GetAccessSummaryRequest.newBuilder()
               .setName(
                   AccessSummaryName.of("[PROJECT]", "[LOCATION]", "[ACCESS_SUMMARY]").toString())
               .build();
       ApiFuture<AccessSummary> future =
           authProviderServiceClient.getAccessSummaryCallable().futureCall(request);
       // Do something.
       AccessSummary response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAccessSummaryRequest),[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AccessSummary)>` |   
  
### getAuthProvider(@Nullable AuthProviderName name)
    
    
    public final AuthProvider getAuthProvider(@Nullable AuthProviderName name)

Gets details of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       AuthProvider response = authProviderServiceClient.getAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### getAuthProvider(GetAuthProviderRequest request)
    
    
    public final AuthProvider getAuthProvider(GetAuthProviderRequest request)

Gets details of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAuthProviderRequest request =
           GetAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .build();
       AuthProvider response = authProviderServiceClient.getAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### getAuthProvider(String name)
    
    
    public final AuthProvider getAuthProvider(String name)

Gets details of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       AuthProvider response = authProviderServiceClient.getAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### getAuthProviderCallable()
    
    
    public final UnaryCallable<GetAuthProviderRequest,AuthProvider> getAuthProviderCallable()

Gets details of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAuthProviderRequest request =
           GetAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.getAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
### getAuthorization(@Nullable AuthorizationName name)
    
    
    public final Authorization getAuthorization(@Nullable AuthorizationName name)

Gets details of a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthorizationName name =
           AuthorizationName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]");
       Authorization response = authProviderServiceClient.getAuthorization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthorizationName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.Authorization)` |   
  
### getAuthorization(GetAuthorizationRequest request)
    
    
    public final Authorization getAuthorization(GetAuthorizationRequest request)

Gets details of a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAuthorizationRequest request =
           GetAuthorizationRequest.newBuilder()
               .setName(
                   AuthorizationName.of(
                           "[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
                       .toString())
               .build();
       Authorization response = authProviderServiceClient.getAuthorization(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAuthorizationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.Authorization)` |   
  
### getAuthorization(String name)
    
    
    public final Authorization getAuthorization(String name)

Gets details of a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name =
           AuthorizationName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
               .toString();
       Authorization response = authProviderServiceClient.getAuthorization(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.Authorization)` |   
  
### getAuthorizationCallable()
    
    
    public final UnaryCallable<GetAuthorizationRequest,Authorization> getAuthorizationCallable()

Gets details of a single Authorization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetAuthorizationRequest request =
           GetAuthorizationRequest.newBuilder()
               .setName(
                   AuthorizationName.of(
                           "[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]", "[AUTHORIZATION]")
                       .toString())
               .build();
       ApiFuture<Authorization> future =
           authProviderServiceClient.getAuthorizationCallable().futureCall(request);
       // Do something.
       Authorization response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.GetAuthorizationRequest),[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.Authorization)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = authProviderServiceClient.getIamPolicy(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           authProviderServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = authProviderServiceClient.getLocation(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           authProviderServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable AuthProviderServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderServiceSettings` |   
  
### getStub()
    
    
    public AuthProviderServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.stub.AuthProviderServiceStub)` |   
  
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
  
### listAccessSummaries(@Nullable LocationName parent)
    
    
    public final AuthProviderServiceClient.ListAccessSummariesPagedResponse listAccessSummaries(@Nullable LocationName parent)

Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AccessSummary element :
           authProviderServiceClient.listAccessSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.LocationName`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAccessSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAccessSummariesPagedResponse)` |   
  
### listAccessSummaries(ListAccessSummariesRequest request)
    
    
    public final AuthProviderServiceClient.ListAccessSummariesPagedResponse listAccessSummaries(ListAccessSummariesRequest request)

Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAccessSummariesRequest request =
           ListAccessSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AccessSummary element :
           authProviderServiceClient.listAccessSummaries(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAccessSummariesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAccessSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAccessSummariesPagedResponse)` |   
  
### listAccessSummaries(String parent)
    
    
    public final AuthProviderServiceClient.ListAccessSummariesPagedResponse listAccessSummaries(String parent)

Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AccessSummary element :
           authProviderServiceClient.listAccessSummaries(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAccessSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAccessSummariesPagedResponse)` |   
  
### listAccessSummariesCallable()
    
    
    public final UnaryCallable<ListAccessSummariesRequest,ListAccessSummariesResponse> listAccessSummariesCallable()

Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAccessSummariesRequest request =
           ListAccessSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAccessSummariesResponse response =
             authProviderServiceClient.listAccessSummariesCallable().call(request);
         for (AccessSummary element : response.getAccessSummariesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAccessSummariesRequest),[ListAccessSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAccessSummariesResponse)>` |   
  
### listAccessSummariesPagedCallable()
    
    
    public final UnaryCallable<ListAccessSummariesRequest,AuthProviderServiceClient.ListAccessSummariesPagedResponse> listAccessSummariesPagedCallable()

Lists AccessSummaries in a given project and location. Supported Filters: - `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAccessSummariesRequest request =
           ListAccessSummariesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AccessSummary> future =
           authProviderServiceClient.listAccessSummariesPagedCallable().futureCall(request);
       // Do something.
       for (AccessSummary element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAccessSummariesRequest),[ListAccessSummariesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAccessSummariesPagedResponse)>` |   
  
### listAuthProviders(@Nullable LocationName parent)
    
    
    public final AuthProviderServiceClient.ListAuthProvidersPagedResponse listAuthProviders(@Nullable LocationName parent)

Lists AuthProviders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (AuthProvider element :
           authProviderServiceClient.listAuthProviders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.LocationName`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthProvidersPagedResponse)` |   
  
### listAuthProviders(ListAuthProvidersRequest request)
    
    
    public final AuthProviderServiceClient.ListAuthProvidersPagedResponse listAuthProviders(ListAuthProvidersRequest request)

Lists AuthProviders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthProvidersRequest request =
           ListAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .build();
       for (AuthProvider element :
           authProviderServiceClient.listAuthProviders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthProvidersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthProvidersPagedResponse)` |   
  
### listAuthProviders(String parent)
    
    
    public final AuthProviderServiceClient.ListAuthProvidersPagedResponse listAuthProviders(String parent)

Lists AuthProviders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (AuthProvider element :
           authProviderServiceClient.listAuthProviders(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthProvidersPagedResponse)` |   
  
### listAuthProvidersCallable()
    
    
    public final UnaryCallable<ListAuthProvidersRequest,ListAuthProvidersResponse> listAuthProvidersCallable()

Lists AuthProviders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthProvidersRequest request =
           ListAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .build();
       while (true) {
         ListAuthProvidersResponse response =
             authProviderServiceClient.listAuthProvidersCallable().call(request);
         for (AuthProvider element : response.getAuthProvidersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthProvidersRequest),[ListAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthProvidersResponse)>` |   
  
### listAuthProvidersPagedCallable()
    
    
    public final UnaryCallable<ListAuthProvidersRequest,AuthProviderServiceClient.ListAuthProvidersPagedResponse> listAuthProvidersPagedCallable()

Lists AuthProviders in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthProvidersRequest request =
           ListAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.listAuthProvidersPagedCallable().futureCall(request);
       // Do something.
       for (AuthProvider element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthProvidersRequest),[ListAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthProvidersPagedResponse)>` |   
  
### listAuthorizations(@Nullable AuthProviderName parent)
    
    
    public final AuthProviderServiceClient.ListAuthorizationsPagedResponse listAuthorizations(@Nullable AuthProviderName parent)

Lists Authorizations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName parent = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       for (Authorization element :
           authProviderServiceClient.listAuthorizations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthorizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthorizationsPagedResponse)` |   
  
### listAuthorizations(ListAuthorizationsRequest request)
    
    
    public final AuthProviderServiceClient.ListAuthorizationsPagedResponse listAuthorizations(ListAuthorizationsRequest request)

Lists Authorizations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthorizationsRequest request =
           ListAuthorizationsRequest.newBuilder()
               .setParent(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Authorization element :
           authProviderServiceClient.listAuthorizations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthorizationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthorizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthorizationsPagedResponse)` |   
  
### listAuthorizations(String parent)
    
    
    public final AuthProviderServiceClient.ListAuthorizationsPagedResponse listAuthorizations(String parent)

Lists Authorizations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String parent = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       for (Authorization element :
           authProviderServiceClient.listAuthorizations(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.ListAuthorizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthorizationsPagedResponse)` |   
  
### listAuthorizationsCallable()
    
    
    public final UnaryCallable<ListAuthorizationsRequest,ListAuthorizationsResponse> listAuthorizationsCallable()

Lists Authorizations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthorizationsRequest request =
           ListAuthorizationsRequest.newBuilder()
               .setParent(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAuthorizationsResponse response =
             authProviderServiceClient.listAuthorizationsCallable().call(request);
         for (Authorization element : response.getAuthorizationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthorizationsRequest),[ListAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthorizationsResponse)>` |   
  
### listAuthorizationsPagedCallable()
    
    
    public final UnaryCallable<ListAuthorizationsRequest,AuthProviderServiceClient.ListAuthorizationsPagedResponse> listAuthorizationsPagedCallable()

Lists Authorizations in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListAuthorizationsRequest request =
           ListAuthorizationsRequest.newBuilder()
               .setParent(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Authorization> future =
           authProviderServiceClient.listAuthorizationsPagedCallable().futureCall(request);
       // Do something.
       for (Authorization element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.ListAuthorizationsRequest),[ListAuthorizationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListAuthorizationsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final AuthProviderServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : authProviderServiceClient.listLocations(request).iterateAll()) {
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
`[AuthProviderServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             authProviderServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AuthProviderServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           authProviderServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.ListLocationsPagedResponse)>` |   
  
### queryAuthProviders(@Nullable LocationName parent, String workloadId)
    
    
    public final AuthProviderServiceClient.QueryAuthProvidersPagedResponse queryAuthProviders(@Nullable LocationName parent, String workloadId)

Queries what all auth_providers are used by a given workload_id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       String workloadId = "workloadId-186277134";
       for (String element :
           authProviderServiceClient.queryAuthProviders(parent, workloadId).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.LocationName`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
`workloadId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workload identifier to filter by.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryAuthProvidersPagedResponse)` |   
  
### queryAuthProviders(QueryAuthProvidersRequest request)
    
    
    public final AuthProviderServiceClient.QueryAuthProvidersPagedResponse queryAuthProviders(QueryAuthProvidersRequest request)

Queries what all auth_providers are used by a given workload_id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryAuthProvidersRequest request =
           QueryAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkloadId("workloadId-186277134")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : authProviderServiceClient.queryAuthProviders(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryAuthProvidersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryAuthProvidersPagedResponse)` |   
  
### queryAuthProviders(String parent, String workloadId)
    
    
    public final AuthProviderServiceClient.QueryAuthProvidersPagedResponse queryAuthProviders(String parent, String workloadId)

Queries what all auth_providers are used by a given workload_id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       String workloadId = "workloadId-186277134";
       for (String element :
           authProviderServiceClient.queryAuthProviders(parent, workloadId).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
`workloadId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The workload identifier to filter by.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryAuthProvidersPagedResponse)` |   
  
### queryAuthProvidersCallable()
    
    
    public final UnaryCallable<QueryAuthProvidersRequest,QueryAuthProvidersResponse> queryAuthProvidersCallable()

Queries what all auth_providers are used by a given workload_id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryAuthProvidersRequest request =
           QueryAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkloadId("workloadId-186277134")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryAuthProvidersResponse response =
             authProviderServiceClient.queryAuthProvidersCallable().call(request);
         for (String element : response.getAuthProviderNamesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryAuthProvidersRequest),[QueryAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryAuthProvidersResponse)>` |   
  
### queryAuthProvidersPagedCallable()
    
    
    public final UnaryCallable<QueryAuthProvidersRequest,AuthProviderServiceClient.QueryAuthProvidersPagedResponse> queryAuthProvidersPagedCallable()

Queries what all auth_providers are used by a given workload_id.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryAuthProvidersRequest request =
           QueryAuthProvidersRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkloadId("workloadId-186277134")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future =
           authProviderServiceClient.queryAuthProvidersPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryAuthProvidersRequest),[QueryAuthProvidersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryAuthProvidersPagedResponse)>` |   
  
### queryWorkloads(@Nullable AuthProviderName name)
    
    
    public final AuthProviderServiceClient.QueryWorkloadsPagedResponse queryWorkloads(@Nullable AuthProviderName name)

Queries what all workloads are using a given auth_provider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       for (String element : authProviderServiceClient.queryWorkloads(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. The name of the auth_provider to query. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryWorkloadsPagedResponse)` |   
  
### queryWorkloads(QueryWorkloadsRequest request)
    
    
    public final AuthProviderServiceClient.QueryWorkloadsPagedResponse queryWorkloads(QueryWorkloadsRequest request)

Queries what all workloads are using a given auth_provider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryWorkloadsRequest request =
           QueryWorkloadsRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (String element : authProviderServiceClient.queryWorkloads(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryWorkloadsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryWorkloadsPagedResponse)` |   
  
### queryWorkloads(String name)
    
    
    public final AuthProviderServiceClient.QueryWorkloadsPagedResponse queryWorkloads(String name)

Queries what all workloads are using a given auth_provider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       for (String element : authProviderServiceClient.queryWorkloads(name).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the auth_provider to query. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceClient.QueryWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryWorkloadsPagedResponse)` |   
  
### queryWorkloadsCallable()
    
    
    public final UnaryCallable<QueryWorkloadsRequest,QueryWorkloadsResponse> queryWorkloadsCallable()

Queries what all workloads are using a given auth_provider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryWorkloadsRequest request =
           QueryWorkloadsRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryWorkloadsResponse response =
             authProviderServiceClient.queryWorkloadsCallable().call(request);
         for (String element : response.getWorkloadIdsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryWorkloadsRequest),[QueryWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryWorkloadsResponse)>` |   
  
### queryWorkloadsPagedCallable()
    
    
    public final UnaryCallable<QueryWorkloadsRequest,AuthProviderServiceClient.QueryWorkloadsPagedResponse> queryWorkloadsPagedCallable()

Queries what all workloads are using a given auth_provider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       QueryWorkloadsRequest request =
           QueryWorkloadsRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<String> future =
           authProviderServiceClient.queryWorkloadsPagedCallable().futureCall(request);
       // Do something.
       for (String element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.QueryWorkloadsRequest),[QueryWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProviderServiceClient.QueryWorkloadsPagedResponse)>` |   
  
### revokeAuthorization(@Nullable AuthProviderName name, String userId)
    
    
    public final RevokeAuthorizationResponse revokeAuthorization(@Nullable AuthProviderName name, String userId)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       String userId = "userId-836030906";
       RevokeAuthorizationResponse response =
           authProviderServiceClient.revokeAuthorization(name, userId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. The resource name of the AuthProvider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
`userId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identity of the user to revoke authorization for.  
**Returns**  
---  
**Type** | **Description**  
`[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationResponse)` |   
  
### revokeAuthorization(RevokeAuthorizationRequest request)
    
    
    public final RevokeAuthorizationResponse revokeAuthorization(RevokeAuthorizationRequest request)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       RevokeAuthorizationRequest request =
           RevokeAuthorizationRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setUserId("userId-836030906")
               .build();
       RevokeAuthorizationResponse response = authProviderServiceClient.revokeAuthorization(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationResponse)` |   
  
### revokeAuthorization(String name, String userId)
    
    
    public final RevokeAuthorizationResponse revokeAuthorization(String name, String userId)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       String userId = "userId-836030906";
       RevokeAuthorizationResponse response =
           authProviderServiceClient.revokeAuthorization(name, userId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AuthProvider. Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
`userId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The identity of the user to revoke authorization for.  
**Returns**  
---  
**Type** | **Description**  
`[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationResponse)` |   
  
### revokeAuthorizationCallable()
    
    
    public final UnaryCallable<RevokeAuthorizationRequest,RevokeAuthorizationResponse> revokeAuthorizationCallable()

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       RevokeAuthorizationRequest request =
           RevokeAuthorizationRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setUserId("userId-836030906")
               .build();
       ApiFuture<RevokeAuthorizationResponse> future =
           authProviderServiceClient.revokeAuthorizationCallable().futureCall(request);
       // Do something.
       RevokeAuthorizationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationRequest),[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.RevokeAuthorizationResponse)>` |   
  
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = authProviderServiceClient.setIamPolicy(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           authProviderServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = authProviderServiceClient.testIamPermissions(request);
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
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           authProviderServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### undeleteAuthProvider(@Nullable AuthProviderName name)
    
    
    public final AuthProvider undeleteAuthProvider(@Nullable AuthProviderName name)

Undeletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProviderName name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]");
       AuthProvider response = authProviderServiceClient.undeleteAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.agentidentity.v1beta.AuthProviderName`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### undeleteAuthProvider(UndeleteAuthProviderRequest request)
    
    
    public final AuthProvider undeleteAuthProvider(UndeleteAuthProviderRequest request)

Undeletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       UndeleteAuthProviderRequest request =
           UndeleteAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       AuthProvider response = authProviderServiceClient.undeleteAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.UndeleteAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### undeleteAuthProvider(String name)
    
    
    public final AuthProvider undeleteAuthProvider(String name)

Undeletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       String name = AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString();
       AuthProvider response = authProviderServiceClient.undeleteAuthProvider(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource Format: projects/{project}/locations/{location}/authProviders/{auth_provider}  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### undeleteAuthProviderCallable()
    
    
    public final UnaryCallable<UndeleteAuthProviderRequest,AuthProvider> undeleteAuthProviderCallable()

Undeletes a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       UndeleteAuthProviderRequest request =
           UndeleteAuthProviderRequest.newBuilder()
               .setName(AuthProviderName.of("[PROJECT]", "[LOCATION]", "[AUTH_PROVIDER]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.undeleteAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.UndeleteAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
### updateAuthProvider(AuthProvider authProvider, FieldMask updateMask)
    
    
    public final AuthProvider updateAuthProvider(AuthProvider authProvider, FieldMask updateMask)

Updates the parameters of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       AuthProvider authProvider = AuthProvider.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AuthProvider response =
           authProviderServiceClient.updateAuthProvider(authProvider, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`authProvider` | `[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)`  
Required. The AuthProvider resource which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the AuthProvider resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### updateAuthProvider(UpdateAuthProviderRequest request)
    
    
    public final AuthProvider updateAuthProvider(UpdateAuthProviderRequest request)

Updates the parameters of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       UpdateAuthProviderRequest request =
           UpdateAuthProviderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthProvider(AuthProvider.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       AuthProvider response = authProviderServiceClient.updateAuthProvider(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.UpdateAuthProviderRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)` |   
  
### updateAuthProviderCallable()
    
    
    public final UnaryCallable<UpdateAuthProviderRequest,AuthProvider> updateAuthProviderCallable()

Updates the parameters of a single AuthProvider.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AuthProviderServiceClient authProviderServiceClient = AuthProviderServiceClient.create()) {
       UpdateAuthProviderRequest request =
           UpdateAuthProviderRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAuthProvider(AuthProvider.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<AuthProvider> future =
           authProviderServiceClient.updateAuthProviderCallable().futureCall(request);
       // Do something.
       AuthProvider response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.UpdateAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1beta.AuthProvider)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
