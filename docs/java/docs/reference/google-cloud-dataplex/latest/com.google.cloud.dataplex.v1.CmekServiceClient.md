---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient
title: Class CmekServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:32:07.950864+00:00
---

# Class CmekServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CmekServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/CmekServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Dataplex Universal Catalog Customer Managed Encryption Keys (CMEK) Service

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       EncryptionConfigName name =
           EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]");
       EncryptionConfig response = cmekServiceClient.getEncryptionConfig(name);
     }
     

Note: close() needs to be called on the CmekServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateEncryptionConfig |  Create an EncryptionConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createEncryptionConfigAsync(CreateEncryptionConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createEncryptionConfigAsync(OrganizationLocationName parent, EncryptionConfig encryptionConfig, String encryptionConfigId) 
  * createEncryptionConfigAsync(String parent, EncryptionConfig encryptionConfig, String encryptionConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createEncryptionConfigOperationCallable() 
  * createEncryptionConfigCallable() 

  
UpdateEncryptionConfig |  Update an EncryptionConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateEncryptionConfigAsync(UpdateEncryptionConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateEncryptionConfigAsync(EncryptionConfig encryptionConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateEncryptionConfigOperationCallable() 
  * updateEncryptionConfigCallable() 

  
DeleteEncryptionConfig |  Delete an EncryptionConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteEncryptionConfigAsync(DeleteEncryptionConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteEncryptionConfigAsync(EncryptionConfigName name) 
  * deleteEncryptionConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteEncryptionConfigOperationCallable() 
  * deleteEncryptionConfigCallable() 

  
ListEncryptionConfigs |  List EncryptionConfigs. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listEncryptionConfigs(ListEncryptionConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listEncryptionConfigs(OrganizationLocationName parent) 
  * listEncryptionConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listEncryptionConfigsPagedCallable() 
  * listEncryptionConfigsCallable() 

  
GetEncryptionConfig |  Get an EncryptionConfig. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getEncryptionConfig(GetEncryptionConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getEncryptionConfig(EncryptionConfigName name) 
  * getEncryptionConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getEncryptionConfigCallable() 

  
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

This class can be customized by passing in a custom instance of CmekServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekServiceSettings cmekServiceSettings =
         CmekServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CmekServiceClient cmekServiceClient = CmekServiceClient.create(cmekServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekServiceSettings cmekServiceSettings =
         CmekServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CmekServiceClient cmekServiceClient = CmekServiceClient.create(cmekServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CmekServiceSettings cmekServiceSettings = CmekServiceSettings.newHttpJsonBuilder().build();
     CmekServiceClient cmekServiceClient = CmekServiceClient.create(cmekServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CmekServiceClient

## Static Methods 

### create()
    
    
    public static final CmekServiceClient create()

Constructs an instance of CmekServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmekServiceSettings settings)
    
    
    public static final CmekServiceClient create(CmekServiceSettings settings)

Constructs an instance of CmekServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmekServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CmekServiceStub stub)
    
    
    public static final CmekServiceClient create(CmekServiceStub stub)

Constructs an instance of CmekServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CmekServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmekServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CmekServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient)` |   
  
## Constructors 

### CmekServiceClient(CmekServiceSettings settings)
    
    
    protected CmekServiceClient(CmekServiceSettings settings)

Constructs an instance of CmekServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CmekServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceSettings)`  
  
  
### CmekServiceClient(CmekServiceStub stub)
    
    
    protected CmekServiceClient(CmekServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CmekServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CmekServiceStub)`  
  
  
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

### createEncryptionConfigAsync(@Nullable OrganizationLocationName parent, EncryptionConfig encryptionConfig, String encryptionConfigId)
    
    
    public final OperationFuture<EncryptionConfig,OperationMetadata> createEncryptionConfigAsync(@Nullable OrganizationLocationName parent, EncryptionConfig encryptionConfig, String encryptionConfigId)

Create an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       EncryptionConfig encryptionConfig = EncryptionConfig.newBuilder().build();
       String encryptionConfigId = "encryptionConfigId-1583151968";
       EncryptionConfig response =
           cmekServiceClient
               .createEncryptionConfigAsync(parent, encryptionConfig, encryptionConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.OrganizationLocationName`  
Required. The location at which the EncryptionConfig is to be created.  
`encryptionConfig` | `[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)`  
Required. The EncryptionConfig to create.  
`encryptionConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the EncryptionConfig to create. Currently, only a value of "default" is supported.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEncryptionConfigAsync(CreateEncryptionConfigRequest request)
    
    
    public final OperationFuture<EncryptionConfig,OperationMetadata> createEncryptionConfigAsync(CreateEncryptionConfigRequest request)

Create an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       CreateEncryptionConfigRequest request =
           CreateEncryptionConfigRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setEncryptionConfigId("encryptionConfigId-1583151968")
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .build();
       EncryptionConfig response = cmekServiceClient.createEncryptionConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEncryptionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEncryptionConfigAsync(String parent, EncryptionConfig encryptionConfig, String encryptionConfigId)
    
    
    public final OperationFuture<EncryptionConfig,OperationMetadata> createEncryptionConfigAsync(String parent, EncryptionConfig encryptionConfig, String encryptionConfigId)

Create an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       EncryptionConfig encryptionConfig = EncryptionConfig.newBuilder().build();
       String encryptionConfigId = "encryptionConfigId-1583151968";
       EncryptionConfig response =
           cmekServiceClient
               .createEncryptionConfigAsync(parent, encryptionConfig, encryptionConfigId)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location at which the EncryptionConfig is to be created.  
`encryptionConfig` | `[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)`  
Required. The EncryptionConfig to create.  
`encryptionConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the EncryptionConfig to create. Currently, only a value of "default" is supported.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createEncryptionConfigCallable()
    
    
    public final UnaryCallable<CreateEncryptionConfigRequest,Operation> createEncryptionConfigCallable()

Create an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       CreateEncryptionConfigRequest request =
           CreateEncryptionConfigRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setEncryptionConfigId("encryptionConfigId-1583151968")
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           cmekServiceClient.createEncryptionConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEncryptionConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEncryptionConfigOperationCallable()
    
    
    public final OperationCallable<CreateEncryptionConfigRequest,EncryptionConfig,OperationMetadata> createEncryptionConfigOperationCallable()

Create an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       CreateEncryptionConfigRequest request =
           CreateEncryptionConfigRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setEncryptionConfigId("encryptionConfigId-1583151968")
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .build();
       OperationFuture<EncryptionConfig, OperationMetadata> future =
           cmekServiceClient.createEncryptionConfigOperationCallable().futureCall(request);
       // Do something.
       EncryptionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateEncryptionConfigRequest),[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEncryptionConfigAsync(@Nullable EncryptionConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEncryptionConfigAsync(@Nullable EncryptionConfigName name)

Delete an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       EncryptionConfigName name =
           EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]");
       cmekServiceClient.deleteEncryptionConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EncryptionConfigName`  
Required. The name of the EncryptionConfig to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEncryptionConfigAsync(DeleteEncryptionConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEncryptionConfigAsync(DeleteEncryptionConfigRequest request)

Delete an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       DeleteEncryptionConfigRequest request =
           DeleteEncryptionConfigRequest.newBuilder()
               .setName(
                   EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       cmekServiceClient.deleteEncryptionConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEncryptionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEncryptionConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteEncryptionConfigAsync(String name)

Delete an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       String name =
           EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]").toString();
       cmekServiceClient.deleteEncryptionConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the EncryptionConfig to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteEncryptionConfigCallable()
    
    
    public final UnaryCallable<DeleteEncryptionConfigRequest,Operation> deleteEncryptionConfigCallable()

Delete an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       DeleteEncryptionConfigRequest request =
           DeleteEncryptionConfigRequest.newBuilder()
               .setName(
                   EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           cmekServiceClient.deleteEncryptionConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEncryptionConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEncryptionConfigOperationCallable()
    
    
    public final OperationCallable<DeleteEncryptionConfigRequest,Empty,OperationMetadata> deleteEncryptionConfigOperationCallable()

Delete an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       DeleteEncryptionConfigRequest request =
           DeleteEncryptionConfigRequest.newBuilder()
               .setName(
                   EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           cmekServiceClient.deleteEncryptionConfigOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteEncryptionConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### getEncryptionConfig(@Nullable EncryptionConfigName name)
    
    
    public final EncryptionConfig getEncryptionConfig(@Nullable EncryptionConfigName name)

Get an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       EncryptionConfigName name =
           EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]");
       EncryptionConfig response = cmekServiceClient.getEncryptionConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.EncryptionConfigName`  
Required. The name of the EncryptionConfig to fetch.  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)` |   
  
### getEncryptionConfig(GetEncryptionConfigRequest request)
    
    
    public final EncryptionConfig getEncryptionConfig(GetEncryptionConfigRequest request)

Get an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetEncryptionConfigRequest request =
           GetEncryptionConfigRequest.newBuilder()
               .setName(
                   EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]")
                       .toString())
               .build();
       EncryptionConfig response = cmekServiceClient.getEncryptionConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEncryptionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)` |   
  
### getEncryptionConfig(String name)
    
    
    public final EncryptionConfig getEncryptionConfig(String name)

Get an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       String name =
           EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]").toString();
       EncryptionConfig response = cmekServiceClient.getEncryptionConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the EncryptionConfig to fetch.  
**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)` |   
  
### getEncryptionConfigCallable()
    
    
    public final UnaryCallable<GetEncryptionConfigRequest,EncryptionConfig> getEncryptionConfigCallable()

Get an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetEncryptionConfigRequest request =
           GetEncryptionConfigRequest.newBuilder()
               .setName(
                   EncryptionConfigName.of("[ORGANIZATION]", "[LOCATION]", "[ENCRYPTION_CONFIG]")
                       .toString())
               .build();
       ApiFuture<EncryptionConfig> future =
           cmekServiceClient.getEncryptionConfigCallable().futureCall(request);
       // Do something.
       EncryptionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetEncryptionConfigRequest),[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)>` |   
  
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = cmekServiceClient.getIamPolicy(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = cmekServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = cmekServiceClient.getLocation(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = cmekServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable CmekServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.CmekServiceSettings` |   
  
### getStub()
    
    
    public CmekServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CmekServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.CmekServiceStub)` |   
  
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
  
### listEncryptionConfigs(@Nullable OrganizationLocationName parent)
    
    
    public final CmekServiceClient.ListEncryptionConfigsPagedResponse listEncryptionConfigs(@Nullable OrganizationLocationName parent)

List EncryptionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       OrganizationLocationName parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]");
       for (EncryptionConfig element :
           cmekServiceClient.listEncryptionConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.OrganizationLocationName`  
Required. The location for which the EncryptionConfig is to be listed.  
**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient.ListEncryptionConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListEncryptionConfigsPagedResponse)` |   
  
### listEncryptionConfigs(ListEncryptionConfigsRequest request)
    
    
    public final CmekServiceClient.ListEncryptionConfigsPagedResponse listEncryptionConfigs(ListEncryptionConfigsRequest request)

List EncryptionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListEncryptionConfigsRequest request =
           ListEncryptionConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (EncryptionConfig element :
           cmekServiceClient.listEncryptionConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEncryptionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEncryptionConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient.ListEncryptionConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListEncryptionConfigsPagedResponse)` |   
  
### listEncryptionConfigs(String parent)
    
    
    public final CmekServiceClient.ListEncryptionConfigsPagedResponse listEncryptionConfigs(String parent)

List EncryptionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       String parent = OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString();
       for (EncryptionConfig element :
           cmekServiceClient.listEncryptionConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location for which the EncryptionConfig is to be listed.  
**Returns**  
---  
**Type** | **Description**  
`[CmekServiceClient.ListEncryptionConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListEncryptionConfigsPagedResponse)` |   
  
### listEncryptionConfigsCallable()
    
    
    public final UnaryCallable<ListEncryptionConfigsRequest,ListEncryptionConfigsResponse> listEncryptionConfigsCallable()

List EncryptionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListEncryptionConfigsRequest request =
           ListEncryptionConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListEncryptionConfigsResponse response =
             cmekServiceClient.listEncryptionConfigsCallable().call(request);
         for (EncryptionConfig element : response.getEncryptionConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEncryptionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEncryptionConfigsRequest),[ListEncryptionConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEncryptionConfigsResponse)>` |   
  
### listEncryptionConfigsPagedCallable()
    
    
    public final UnaryCallable<ListEncryptionConfigsRequest,CmekServiceClient.ListEncryptionConfigsPagedResponse> listEncryptionConfigsPagedCallable()

List EncryptionConfigs.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListEncryptionConfigsRequest request =
           ListEncryptionConfigsRequest.newBuilder()
               .setParent(OrganizationLocationName.of("[ORGANIZATION]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<EncryptionConfig> future =
           cmekServiceClient.listEncryptionConfigsPagedCallable().futureCall(request);
       // Do something.
       for (EncryptionConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListEncryptionConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListEncryptionConfigsRequest),[ListEncryptionConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListEncryptionConfigsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final CmekServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : cmekServiceClient.listLocations(request).iterateAll()) {
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
`[CmekServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = cmekServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,CmekServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           cmekServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CmekServiceClient.ListLocationsPagedResponse)>` |   
  
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = cmekServiceClient.setIamPolicy(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = cmekServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = cmekServiceClient.testIamPermissions(request);
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
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           cmekServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateEncryptionConfigAsync(EncryptionConfig encryptionConfig, FieldMask updateMask)
    
    
    public final OperationFuture<EncryptionConfig,OperationMetadata> updateEncryptionConfigAsync(EncryptionConfig encryptionConfig, FieldMask updateMask)

Update an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       EncryptionConfig encryptionConfig = EncryptionConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       EncryptionConfig response =
           cmekServiceClient.updateEncryptionConfigAsync(encryptionConfig, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`encryptionConfig` | `[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig)`  
Required. The EncryptionConfig to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Mask of fields to update. The service treats an omitted field mask as an implied field mask equivalent to all fields that are populated (have a non-empty value).  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEncryptionConfigAsync(UpdateEncryptionConfigRequest request)
    
    
    public final OperationFuture<EncryptionConfig,OperationMetadata> updateEncryptionConfigAsync(UpdateEncryptionConfigRequest request)

Update an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       UpdateEncryptionConfigRequest request =
           UpdateEncryptionConfigRequest.newBuilder()
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       EncryptionConfig response = cmekServiceClient.updateEncryptionConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEncryptionConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateEncryptionConfigCallable()
    
    
    public final UnaryCallable<UpdateEncryptionConfigRequest,Operation> updateEncryptionConfigCallable()

Update an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       UpdateEncryptionConfigRequest request =
           UpdateEncryptionConfigRequest.newBuilder()
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           cmekServiceClient.updateEncryptionConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEncryptionConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEncryptionConfigOperationCallable()
    
    
    public final OperationCallable<UpdateEncryptionConfigRequest,EncryptionConfig,OperationMetadata> updateEncryptionConfigOperationCallable()

Update an EncryptionConfig.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CmekServiceClient cmekServiceClient = CmekServiceClient.create()) {
       UpdateEncryptionConfigRequest request =
           UpdateEncryptionConfigRequest.newBuilder()
               .setEncryptionConfig(EncryptionConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<EncryptionConfig, OperationMetadata> future =
           cmekServiceClient.updateEncryptionConfigOperationCallable().futureCall(request);
       // Do something.
       EncryptionConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateEncryptionConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateEncryptionConfigRequest),[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.EncryptionConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
