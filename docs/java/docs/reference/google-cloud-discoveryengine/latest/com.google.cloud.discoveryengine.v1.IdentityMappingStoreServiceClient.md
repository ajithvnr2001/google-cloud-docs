---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient
title: Class IdentityMappingStoreServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:37.648351+00:00
---

# Class IdentityMappingStoreServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IdentityMappingStoreServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/IdentityMappingStoreServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing Identity Mapping Stores.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       IdentityMappingStore identityMappingStore = IdentityMappingStore.newBuilder().build();
       String identityMappingStoreId = "identityMappingStoreId677904780";
       IdentityMappingStore response =
           identityMappingStoreServiceClient.createIdentityMappingStore(
               parent, identityMappingStore, identityMappingStoreId);
     }
     

Note: close() needs to be called on the IdentityMappingStoreServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateIdentityMappingStore |  Creates a new Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIdentityMappingStore(CreateIdentityMappingStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createIdentityMappingStore(LocationName parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId) 
  * createIdentityMappingStore(String parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIdentityMappingStoreCallable() 

  
GetIdentityMappingStore |  Gets the Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIdentityMappingStore(GetIdentityMappingStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIdentityMappingStore(IdentityMappingStoreName name) 
  * getIdentityMappingStore(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIdentityMappingStoreCallable() 

  
DeleteIdentityMappingStore |  Deletes the Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteIdentityMappingStoreAsync(IdentityMappingStoreName name) 
  * deleteIdentityMappingStoreAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIdentityMappingStoreOperationCallable() 
  * deleteIdentityMappingStoreCallable() 

  
ImportIdentityMappings |  Imports a list of Identity Mapping Entries to an Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importIdentityMappingsAsync(ImportIdentityMappingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importIdentityMappingsOperationCallable() 
  * importIdentityMappingsCallable() 

  
PurgeIdentityMappings |  Purges specified or all Identity Mapping Entries from an Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * purgeIdentityMappingsAsync(PurgeIdentityMappingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * purgeIdentityMappingsOperationCallable() 
  * purgeIdentityMappingsCallable() 

  
ListIdentityMappings |  Lists Identity Mappings in an Identity Mapping Store. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIdentityMappings(ListIdentityMappingsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIdentityMappingsPagedCallable() 
  * listIdentityMappingsCallable() 

  
ListIdentityMappingStores |  Lists all Identity Mapping Stores. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIdentityMappingStores(ListIdentityMappingStoresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listIdentityMappingStores(LocationName parent) 
  * listIdentityMappingStores(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIdentityMappingStoresPagedCallable() 
  * listIdentityMappingStoresCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of IdentityMappingStoreServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IdentityMappingStoreServiceSettings identityMappingStoreServiceSettings =
         IdentityMappingStoreServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create(identityMappingStoreServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IdentityMappingStoreServiceSettings identityMappingStoreServiceSettings =
         IdentityMappingStoreServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create(identityMappingStoreServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IdentityMappingStoreServiceSettings identityMappingStoreServiceSettings =
         IdentityMappingStoreServiceSettings.newHttpJsonBuilder().build();
     IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create(identityMappingStoreServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IdentityMappingStoreServiceClient

## Static Methods 

### create()
    
    
    public static final IdentityMappingStoreServiceClient create()

Constructs an instance of IdentityMappingStoreServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IdentityMappingStoreServiceSettings settings)
    
    
    public static final IdentityMappingStoreServiceClient create(IdentityMappingStoreServiceSettings settings)

Constructs an instance of IdentityMappingStoreServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IdentityMappingStoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IdentityMappingStoreServiceStub stub)
    
    
    public static final IdentityMappingStoreServiceClient create(IdentityMappingStoreServiceStub stub)

Constructs an instance of IdentityMappingStoreServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(IdentityMappingStoreServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IdentityMappingStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.IdentityMappingStoreServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient)` |   
  
## Constructors 

### IdentityMappingStoreServiceClient(IdentityMappingStoreServiceSettings settings)
    
    
    protected IdentityMappingStoreServiceClient(IdentityMappingStoreServiceSettings settings)

Constructs an instance of IdentityMappingStoreServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IdentityMappingStoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceSettings)`  
  
  
### IdentityMappingStoreServiceClient(IdentityMappingStoreServiceStub stub)
    
    
    protected IdentityMappingStoreServiceClient(IdentityMappingStoreServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IdentityMappingStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.IdentityMappingStoreServiceStub)`  
  
  
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

### createIdentityMappingStore(@Nullable LocationName parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId)
    
    
    public final IdentityMappingStore createIdentityMappingStore(@Nullable LocationName parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId)

Creates a new Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       IdentityMappingStore identityMappingStore = IdentityMappingStore.newBuilder().build();
       String identityMappingStoreId = "identityMappingStoreId677904780";
       IdentityMappingStore response =
           identityMappingStoreServiceClient.createIdentityMappingStore(
               parent, identityMappingStore, identityMappingStoreId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.LocationName`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### createIdentityMappingStore(CreateIdentityMappingStoreRequest request)
    
    
    public final IdentityMappingStore createIdentityMappingStore(CreateIdentityMappingStoreRequest request)

Creates a new Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       CreateIdentityMappingStoreRequest request =
           CreateIdentityMappingStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setIdentityMappingStoreId("identityMappingStoreId677904780")
               .setIdentityMappingStore(IdentityMappingStore.newBuilder().build())
               .build();
       IdentityMappingStore response =
           identityMappingStoreServiceClient.createIdentityMappingStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### createIdentityMappingStore(String parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId)
    
    
    public final IdentityMappingStore createIdentityMappingStore(String parent, IdentityMappingStore identityMappingStore, String identityMappingStoreId)

Creates a new Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       IdentityMappingStore identityMappingStore = IdentityMappingStore.newBuilder().build();
       String identityMappingStoreId = "identityMappingStoreId677904780";
       IdentityMappingStore response =
           identityMappingStoreServiceClient.createIdentityMappingStore(
               parent, identityMappingStore, identityMappingStoreId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent collection resource name, such as `projects/{project}/locations/{location}`.  
`identityMappingStore` | `[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)`  
Required. The Identity Mapping Store to create.  
`identityMappingStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the Identity Mapping Store to create. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 63 characters.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### createIdentityMappingStoreCallable()
    
    
    public final UnaryCallable<CreateIdentityMappingStoreRequest,IdentityMappingStore> createIdentityMappingStoreCallable()

Creates a new Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       CreateIdentityMappingStoreRequest request =
           CreateIdentityMappingStoreRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setIdentityMappingStoreId("identityMappingStoreId677904780")
               .setIdentityMappingStore(IdentityMappingStore.newBuilder().build())
               .build();
       ApiFuture<IdentityMappingStore> future =
           identityMappingStoreServiceClient
               .createIdentityMappingStoreCallable()
               .futureCall(request);
       // Do something.
       IdentityMappingStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequest),[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)>` |   
  
### deleteIdentityMappingStoreAsync(@Nullable IdentityMappingStoreName name)
    
    
    public final OperationFuture<Empty,DeleteIdentityMappingStoreMetadata> deleteIdentityMappingStoreAsync(@Nullable IdentityMappingStoreName name)

Deletes the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       IdentityMappingStoreName name =
           IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
       identityMappingStoreServiceClient.deleteIdentityMappingStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.IdentityMappingStoreName`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata)>` |   
  
### deleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest request)
    
    
    public final OperationFuture<Empty,DeleteIdentityMappingStoreMetadata> deleteIdentityMappingStoreAsync(DeleteIdentityMappingStoreRequest request)

Deletes the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       DeleteIdentityMappingStoreRequest request =
           DeleteIdentityMappingStoreRequest.newBuilder()
               .setName(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       identityMappingStoreServiceClient.deleteIdentityMappingStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata)>` |   
  
### deleteIdentityMappingStoreAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteIdentityMappingStoreMetadata> deleteIdentityMappingStoreAsync(String name)

Deletes the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       String name =
           IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
               .toString();
       identityMappingStoreServiceClient.deleteIdentityMappingStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Identity Mapping Store to delete. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata)>` |   
  
### deleteIdentityMappingStoreCallable()
    
    
    public final UnaryCallable<DeleteIdentityMappingStoreRequest,Operation> deleteIdentityMappingStoreCallable()

Deletes the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       DeleteIdentityMappingStoreRequest request =
           DeleteIdentityMappingStoreRequest.newBuilder()
               .setName(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           identityMappingStoreServiceClient
               .deleteIdentityMappingStoreCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteIdentityMappingStoreOperationCallable()
    
    
    public final OperationCallable<DeleteIdentityMappingStoreRequest,Empty,DeleteIdentityMappingStoreMetadata> deleteIdentityMappingStoreOperationCallable()

Deletes the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       DeleteIdentityMappingStoreRequest request =
           DeleteIdentityMappingStoreRequest.newBuilder()
               .setName(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteIdentityMappingStoreMetadata> future =
           identityMappingStoreServiceClient
               .deleteIdentityMappingStoreOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteIdentityMappingStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIdentityMappingStore(@Nullable IdentityMappingStoreName name)
    
    
    public final IdentityMappingStore getIdentityMappingStore(@Nullable IdentityMappingStoreName name)

Gets the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       IdentityMappingStoreName name =
           IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]");
       IdentityMappingStore response =
           identityMappingStoreServiceClient.getIdentityMappingStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.IdentityMappingStoreName`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### getIdentityMappingStore(GetIdentityMappingStoreRequest request)
    
    
    public final IdentityMappingStore getIdentityMappingStore(GetIdentityMappingStoreRequest request)

Gets the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       GetIdentityMappingStoreRequest request =
           GetIdentityMappingStoreRequest.newBuilder()
               .setName(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       IdentityMappingStore response =
           identityMappingStoreServiceClient.getIdentityMappingStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetIdentityMappingStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### getIdentityMappingStore(String name)
    
    
    public final IdentityMappingStore getIdentityMappingStore(String name)

Gets the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       String name =
           IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
               .toString();
       IdentityMappingStore response =
           identityMappingStoreServiceClient.getIdentityMappingStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Identity Mapping Store to get. Format: `projects/{project}/locations/{location}/identityMappingStores/{identityMappingStore}`  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)` |   
  
### getIdentityMappingStoreCallable()
    
    
    public final UnaryCallable<GetIdentityMappingStoreRequest,IdentityMappingStore> getIdentityMappingStoreCallable()

Gets the Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       GetIdentityMappingStoreRequest request =
           GetIdentityMappingStoreRequest.newBuilder()
               .setName(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       ApiFuture<IdentityMappingStore> future =
           identityMappingStoreServiceClient.getIdentityMappingStoreCallable().futureCall(request);
       // Do something.
       IdentityMappingStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIdentityMappingStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetIdentityMappingStoreRequest),[IdentityMappingStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStore)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable IdentityMappingStoreServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceSettings` |   
  
### getStub()
    
    
    public IdentityMappingStoreServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.IdentityMappingStoreServiceStub)` |   
  
### importIdentityMappingsAsync(ImportIdentityMappingsRequest request)
    
    
    public final OperationFuture<ImportIdentityMappingsResponse,IdentityMappingEntryOperationMetadata> importIdentityMappingsAsync(ImportIdentityMappingsRequest request)

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ImportIdentityMappingsRequest request =
           ImportIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       ImportIdentityMappingsResponse response =
           identityMappingStoreServiceClient.importIdentityMappingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportIdentityMappingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportIdentityMappingsResponse),[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata)>` |   
  
### importIdentityMappingsCallable()
    
    
    public final UnaryCallable<ImportIdentityMappingsRequest,Operation> importIdentityMappingsCallable()

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ImportIdentityMappingsRequest request =
           ImportIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           identityMappingStoreServiceClient.importIdentityMappingsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportIdentityMappingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importIdentityMappingsOperationCallable()
    
    
    public final OperationCallable<ImportIdentityMappingsRequest,ImportIdentityMappingsResponse,IdentityMappingEntryOperationMetadata> importIdentityMappingsOperationCallable()

Imports a list of Identity Mapping Entries to an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ImportIdentityMappingsRequest request =
           ImportIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .build();
       OperationFuture<ImportIdentityMappingsResponse, IdentityMappingEntryOperationMetadata>
           future =
               identityMappingStoreServiceClient
                   .importIdentityMappingsOperationCallable()
                   .futureCall(request);
       // Do something.
       ImportIdentityMappingsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportIdentityMappingsRequest),[ImportIdentityMappingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ImportIdentityMappingsResponse),[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata)>` |   
  
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
  
### listIdentityMappingStores(@Nullable LocationName parent)
    
    
    public final IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse listIdentityMappingStores(@Nullable LocationName parent)

Lists all Identity Mapping Stores.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (IdentityMappingStore element :
           identityMappingStoreServiceClient.listIdentityMappingStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.LocationName`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse)` |   
  
### listIdentityMappingStores(ListIdentityMappingStoresRequest request)
    
    
    public final IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse listIdentityMappingStores(ListIdentityMappingStoresRequest request)

Lists all Identity Mapping Stores.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingStoresRequest request =
           ListIdentityMappingStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (IdentityMappingStore element :
           identityMappingStoreServiceClient.listIdentityMappingStores(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingStoresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse)` |   
  
### listIdentityMappingStores(String parent)
    
    
    public final IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse listIdentityMappingStores(String parent)

Lists all Identity Mapping Stores.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (IdentityMappingStore element :
           identityMappingStoreServiceClient.listIdentityMappingStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the Identity Mapping Stores to list. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse)` |   
  
### listIdentityMappingStoresCallable()
    
    
    public final UnaryCallable<ListIdentityMappingStoresRequest,ListIdentityMappingStoresResponse> listIdentityMappingStoresCallable()

Lists all Identity Mapping Stores.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingStoresRequest request =
           ListIdentityMappingStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListIdentityMappingStoresResponse response =
             identityMappingStoreServiceClient.listIdentityMappingStoresCallable().call(request);
         for (IdentityMappingStore element : response.getIdentityMappingStoresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingStoresRequest),[ListIdentityMappingStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingStoresResponse)>` |   
  
### listIdentityMappingStoresPagedCallable()
    
    
    public final UnaryCallable<ListIdentityMappingStoresRequest,IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse> listIdentityMappingStoresPagedCallable()

Lists all Identity Mapping Stores.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingStoresRequest request =
           ListIdentityMappingStoresRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<IdentityMappingStore> future =
           identityMappingStoreServiceClient
               .listIdentityMappingStoresPagedCallable()
               .futureCall(request);
       // Do something.
       for (IdentityMappingStore element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIdentityMappingStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingStoresRequest),[ListIdentityMappingStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingStoresPagedResponse)>` |   
  
### listIdentityMappings(ListIdentityMappingsRequest request)
    
    
    public final IdentityMappingStoreServiceClient.ListIdentityMappingsPagedResponse listIdentityMappings(ListIdentityMappingsRequest request)

Lists Identity Mappings in an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingsRequest request =
           ListIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (IdentityMappingEntry element :
           identityMappingStoreServiceClient.listIdentityMappings(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IdentityMappingStoreServiceClient.ListIdentityMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingsPagedResponse)` |   
  
### listIdentityMappingsCallable()
    
    
    public final UnaryCallable<ListIdentityMappingsRequest,ListIdentityMappingsResponse> listIdentityMappingsCallable()

Lists Identity Mappings in an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingsRequest request =
           ListIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListIdentityMappingsResponse response =
             identityMappingStoreServiceClient.listIdentityMappingsCallable().call(request);
         for (IdentityMappingEntry element : response.getIdentityMappingEntriesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingsRequest),[ListIdentityMappingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingsResponse)>` |   
  
### listIdentityMappingsPagedCallable()
    
    
    public final UnaryCallable<ListIdentityMappingsRequest,IdentityMappingStoreServiceClient.ListIdentityMappingsPagedResponse> listIdentityMappingsPagedCallable()

Lists Identity Mappings in an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       ListIdentityMappingsRequest request =
           ListIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<IdentityMappingEntry> future =
           identityMappingStoreServiceClient.listIdentityMappingsPagedCallable().futureCall(request);
       // Do something.
       for (IdentityMappingEntry element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListIdentityMappingsRequest),[ListIdentityMappingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingStoreServiceClient.ListIdentityMappingsPagedResponse)>` |   
  
### purgeIdentityMappingsAsync(PurgeIdentityMappingsRequest request)
    
    
    public final OperationFuture<Empty,IdentityMappingEntryOperationMetadata> purgeIdentityMappingsAsync(PurgeIdentityMappingsRequest request)

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       PurgeIdentityMappingsRequest request =
           PurgeIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       identityMappingStoreServiceClient.purgeIdentityMappingsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeIdentityMappingsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata)>` |   
  
### purgeIdentityMappingsCallable()
    
    
    public final UnaryCallable<PurgeIdentityMappingsRequest,Operation> purgeIdentityMappingsCallable()

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       PurgeIdentityMappingsRequest request =
           PurgeIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           identityMappingStoreServiceClient.purgeIdentityMappingsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeIdentityMappingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### purgeIdentityMappingsOperationCallable()
    
    
    public final OperationCallable<PurgeIdentityMappingsRequest,Empty,IdentityMappingEntryOperationMetadata> purgeIdentityMappingsOperationCallable()

Purges specified or all Identity Mapping Entries from an Identity Mapping Store.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IdentityMappingStoreServiceClient identityMappingStoreServiceClient =
         IdentityMappingStoreServiceClient.create()) {
       PurgeIdentityMappingsRequest request =
           PurgeIdentityMappingsRequest.newBuilder()
               .setIdentityMappingStore(
                   IdentityMappingStoreName.of("[PROJECT]", "[LOCATION]", "[IDENTITY_MAPPING_STORE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setForce(true)
               .build();
       OperationFuture<Empty, IdentityMappingEntryOperationMetadata> future =
           identityMappingStoreServiceClient
               .purgeIdentityMappingsOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PurgeIdentityMappingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.PurgeIdentityMappingsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[IdentityMappingEntryOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
