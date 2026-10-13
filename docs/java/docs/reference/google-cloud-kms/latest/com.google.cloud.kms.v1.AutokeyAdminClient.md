---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient
title: Class AutokeyAdminClient (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:36.006910+00:00
---

# Class AutokeyAdminClient (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AutokeyAdminClient (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.8  2.5.3  2.4.4  2.3.1 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-kms/google-cloud-kms/src/main/java/com/google/cloud/kms/v1/AutokeyAdminClient.java)| [Product Reference](https://cloud.google.com/kms)  
---|---  
  
Service Description: Provides interfaces for managing [Cloud KMS Autokey](https://cloud.google.com/kms/help/autokey) folder-level or project-level configurations. A configuration is inherited by all descendent folders and projects. A configuration at a folder or project overrides any other configurations in its ancestry. Setting a configuration on a folder is a prerequisite for Cloud KMS Autokey, so that users working in a descendant project can request provisioned CryptoKeys, ready for Customer Managed Encryption Key (CMEK) use, on-demand when using the dedicated key project mode. This is not required when using the delegated key management mode for same-project keys.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       AutokeyConfig autokeyConfig = AutokeyConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AutokeyConfig response = autokeyAdminClient.updateAutokeyConfig(autokeyConfig, updateMask);
     }
     

Note: close() needs to be called on the AutokeyAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
UpdateAutokeyConfig |  Updates the AutokeyConfig for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A KeyHandle creation in the folder's descendant projects will use this configuration to determine where to create the resulting CryptoKey. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAutokeyConfig(UpdateAutokeyConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAutokeyConfig(AutokeyConfig autokeyConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAutokeyConfigCallable() 

  
GetAutokeyConfig |  Returns the AutokeyConfig for a folder or project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAutokeyConfig(GetAutokeyConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAutokeyConfig(AutokeyConfigName name) 
  * getAutokeyConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAutokeyConfigCallable() 

  
ShowEffectiveAutokeyConfig |  Returns the effective Cloud KMS Autokey configuration for a given project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * showEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * showEffectiveAutokeyConfig(ProjectName parent) 
  * showEffectiveAutokeyConfig(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * showEffectiveAutokeyConfigCallable() 

  
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

This class can be customized by passing in a custom instance of AutokeyAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutokeyAdminSettings autokeyAdminSettings =
         AutokeyAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create(autokeyAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutokeyAdminSettings autokeyAdminSettings =
         AutokeyAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create(autokeyAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutokeyAdminSettings autokeyAdminSettings = AutokeyAdminSettings.newHttpJsonBuilder().build();
     AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create(autokeyAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AutokeyAdminClient

## Static Methods 

### create()
    
    
    public static final AutokeyAdminClient create()

Constructs an instance of AutokeyAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutokeyAdminSettings settings)
    
    
    public static final AutokeyAdminClient create(AutokeyAdminSettings settings)

Constructs an instance of AutokeyAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutokeyAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutokeyAdminStub stub)
    
    
    public static final AutokeyAdminClient create(AutokeyAdminStub stub)

Constructs an instance of AutokeyAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(AutokeyAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutokeyAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.stub.AutokeyAdminStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient)` |   
  
## Constructors 

### AutokeyAdminClient(AutokeyAdminSettings settings)
    
    
    protected AutokeyAdminClient(AutokeyAdminSettings settings)

Constructs an instance of AutokeyAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutokeyAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminSettings)`  
  
  
### AutokeyAdminClient(AutokeyAdminStub stub)
    
    
    protected AutokeyAdminClient(AutokeyAdminStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutokeyAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.stub.AutokeyAdminStub)`  
  
  
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

### getAutokeyConfig(@Nullable AutokeyConfigName name)
    
    
    public final AutokeyConfig getAutokeyConfig(@Nullable AutokeyConfigName name)

Returns the AutokeyConfig for a folder or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       AutokeyConfigName name = AutokeyConfigName.ofFolderName("[FOLDER]");
       AutokeyConfig response = autokeyAdminClient.getAutokeyConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.kms.v1.AutokeyConfigName`  
Required. Name of the AutokeyConfig resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)` |   
  
### getAutokeyConfig(GetAutokeyConfigRequest request)
    
    
    public final AutokeyConfig getAutokeyConfig(GetAutokeyConfigRequest request)

Returns the AutokeyConfig for a folder or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetAutokeyConfigRequest request =
           GetAutokeyConfigRequest.newBuilder()
               .setName(AutokeyConfigName.ofFolderName("[FOLDER]").toString())
               .build();
       AutokeyConfig response = autokeyAdminClient.getAutokeyConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)` |   
  
### getAutokeyConfig(String name)
    
    
    public final AutokeyConfig getAutokeyConfig(String name)

Returns the AutokeyConfig for a folder or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       String name = AutokeyConfigName.ofFolderName("[FOLDER]").toString();
       AutokeyConfig response = autokeyAdminClient.getAutokeyConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the AutokeyConfig resource, e.g. `folders/{FOLDER_NUMBER}/autokeyConfig` or `projects/{PROJECT_NUMBER}/autokeyConfig`.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)` |   
  
### getAutokeyConfigCallable()
    
    
    public final UnaryCallable<GetAutokeyConfigRequest,AutokeyConfig> getAutokeyConfigCallable()

Returns the AutokeyConfig for a folder or project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetAutokeyConfigRequest request =
           GetAutokeyConfigRequest.newBuilder()
               .setName(AutokeyConfigName.ofFolderName("[FOLDER]").toString())
               .build();
       ApiFuture<AutokeyConfig> future =
           autokeyAdminClient.getAutokeyConfigCallable().futureCall(request);
       // Do something.
       AutokeyConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetAutokeyConfigRequest),[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = autokeyAdminClient.getIamPolicy(request);
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = autokeyAdminClient.getIamPolicyCallable().futureCall(request);
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = autokeyAdminClient.getLocation(request);
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = autokeyAdminClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable AutokeyAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.kms.v1.AutokeyAdminSettings` |   
  
### getStub()
    
    
    public AutokeyAdminStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AutokeyAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.stub.AutokeyAdminStub)` |   
  
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
    
    
    public final AutokeyAdminClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : autokeyAdminClient.listLocations(request).iterateAll()) {
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
`[AutokeyAdminClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient.ListLocationsPagedResponse)` |   
  
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = autokeyAdminClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,AutokeyAdminClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           autokeyAdminClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyAdminClient.ListLocationsPagedResponse)>` |   
  
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = autokeyAdminClient.setIamPolicy(request);
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = autokeyAdminClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### showEffectiveAutokeyConfig(@Nullable ProjectName parent)
    
    
    public final ShowEffectiveAutokeyConfigResponse showEffectiveAutokeyConfig(@Nullable ProjectName parent)

Returns the effective Cloud KMS Autokey configuration for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       ShowEffectiveAutokeyConfigResponse response =
           autokeyAdminClient.showEffectiveAutokeyConfig(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.kms.v1.ProjectName`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigResponse)` |   
  
### showEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request)
    
    
    public final ShowEffectiveAutokeyConfigResponse showEffectiveAutokeyConfig(ShowEffectiveAutokeyConfigRequest request)

Returns the effective Cloud KMS Autokey configuration for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ShowEffectiveAutokeyConfigRequest request =
           ShowEffectiveAutokeyConfigRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .build();
       ShowEffectiveAutokeyConfigResponse response =
           autokeyAdminClient.showEffectiveAutokeyConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigResponse)` |   
  
### showEffectiveAutokeyConfig(String parent)
    
    
    public final ShowEffectiveAutokeyConfigResponse showEffectiveAutokeyConfig(String parent)

Returns the effective Cloud KMS Autokey configuration for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       ShowEffectiveAutokeyConfigResponse response =
           autokeyAdminClient.showEffectiveAutokeyConfig(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource project to the show effective Cloud KMS Autokey configuration for. This may be helpful for interrogating the effect of nested folder configurations on a given resource project.  
**Returns**  
---  
**Type** | **Description**  
`[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigResponse)` |   
  
### showEffectiveAutokeyConfigCallable()
    
    
    public final UnaryCallable<ShowEffectiveAutokeyConfigRequest,ShowEffectiveAutokeyConfigResponse> showEffectiveAutokeyConfigCallable()

Returns the effective Cloud KMS Autokey configuration for a given project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       ShowEffectiveAutokeyConfigRequest request =
           ShowEffectiveAutokeyConfigRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .build();
       ApiFuture<ShowEffectiveAutokeyConfigResponse> future =
           autokeyAdminClient.showEffectiveAutokeyConfigCallable().futureCall(request);
       // Do something.
       ShowEffectiveAutokeyConfigResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ShowEffectiveAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigRequest),[ShowEffectiveAutokeyConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ShowEffectiveAutokeyConfigResponse)>` |   
  
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = autokeyAdminClient.testIamPermissions(request);
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
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   CryptoKeyName.of("[PROJECT]", "[LOCATION]", "[KEY_RING]", "[CRYPTO_KEY]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           autokeyAdminClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAutokeyConfig(AutokeyConfig autokeyConfig, FieldMask updateMask)
    
    
    public final AutokeyConfig updateAutokeyConfig(AutokeyConfig autokeyConfig, FieldMask updateMask)

Updates the AutokeyConfig for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A KeyHandle creation in the folder's descendant projects will use this configuration to determine where to create the resulting CryptoKey.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       AutokeyConfig autokeyConfig = AutokeyConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AutokeyConfig response = autokeyAdminClient.updateAutokeyConfig(autokeyConfig, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`autokeyConfig` | `[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)`  
Required. AutokeyConfig with values to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Masks which fields of the AutokeyConfig to update, e.g. `keyProject`.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)` |   
  
### updateAutokeyConfig(UpdateAutokeyConfigRequest request)
    
    
    public final AutokeyConfig updateAutokeyConfig(UpdateAutokeyConfigRequest request)

Updates the AutokeyConfig for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A KeyHandle creation in the folder's descendant projects will use this configuration to determine where to create the resulting CryptoKey.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       UpdateAutokeyConfigRequest request =
           UpdateAutokeyConfigRequest.newBuilder()
               .setAutokeyConfig(AutokeyConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AutokeyConfig response = autokeyAdminClient.updateAutokeyConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.UpdateAutokeyConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)` |   
  
### updateAutokeyConfigCallable()
    
    
    public final UnaryCallable<UpdateAutokeyConfigRequest,AutokeyConfig> updateAutokeyConfigCallable()

Updates the AutokeyConfig for a folder or a project. The caller must have both `cloudkms.autokeyConfigs.update` permission on the parent folder and `cloudkms.cryptoKeys.setIamPolicy` permission on the provided key project. A KeyHandle creation in the folder's descendant projects will use this configuration to determine where to create the resulting CryptoKey.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutokeyAdminClient autokeyAdminClient = AutokeyAdminClient.create()) {
       UpdateAutokeyConfigRequest request =
           UpdateAutokeyConfigRequest.newBuilder()
               .setAutokeyConfig(AutokeyConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AutokeyConfig> future =
           autokeyAdminClient.updateAutokeyConfigCallable().futureCall(request);
       // Do something.
       AutokeyConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAutokeyConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.UpdateAutokeyConfigRequest),[AutokeyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AutokeyConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
