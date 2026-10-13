---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient
title: Class NativeStyleServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:53.204233+00:00
---

# Class NativeStyleServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NativeStyleServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/NativeStyleServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `NativeStyle` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NativeStyleName name = NativeStyleName.of("[NETWORK_CODE]", "[NATIVE_STYLE]");
       NativeStyle response = nativeStyleServiceClient.getNativeStyle(name);
     }
     

Note: close() needs to be called on the NativeStyleServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetNativeStyle |  Retrieves a `NativeStyle` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNativeStyle(GetNativeStyleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNativeStyle(NativeStyleName name) 
  * getNativeStyle(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNativeStyleCallable() 

  
ListNativeStyles |  Lists `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNativeStyles(ListNativeStylesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNativeStyles(NetworkName parent) 
  * listNativeStyles(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNativeStylesPagedCallable() 
  * listNativeStylesCallable() 

  
BatchCreateNativeStyles |  Creates `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateNativeStyles(NetworkName parent, List<CreateNativeStyleRequest> requests) 
  * batchCreateNativeStyles(String parent, List<CreateNativeStyleRequest> requests) 
  * batchCreateNativeStyles(BatchCreateNativeStylesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateNativeStylesCallable() 

  
BatchUpdateNativeStyles |  Batch updates `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateNativeStyles(NetworkName parent, List<UpdateNativeStyleRequest> requests) 
  * batchUpdateNativeStyles(String parent, List<UpdateNativeStyleRequest> requests) 
  * batchUpdateNativeStyles(BatchUpdateNativeStylesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateNativeStylesCallable() 

  
BatchActivateNativeStyles |  Beginning of non-CRUD Activates a list of `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateNativeStyles(BatchActivateNativeStylesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateNativeStyles(NetworkName parent, List<String> names) 
  * batchActivateNativeStyles(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateNativeStylesCallable() 

  
BatchDeactivateNativeStyles |  Deactivates a list of `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateNativeStyles(BatchDeactivateNativeStylesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateNativeStyles(NetworkName parent, List<String> names) 
  * batchDeactivateNativeStyles(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateNativeStylesCallable() 

  
BatchArchiveNativeStyles |  Archives a list of `NativeStyle` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveNativeStyles(BatchArchiveNativeStylesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveNativeStyles(NetworkName parent, List<String> names) 
  * batchArchiveNativeStyles(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveNativeStylesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NativeStyleServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NativeStyleServiceSettings nativeStyleServiceSettings =
         NativeStyleServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NativeStyleServiceClient nativeStyleServiceClient =
         NativeStyleServiceClient.create(nativeStyleServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NativeStyleServiceSettings nativeStyleServiceSettings =
         NativeStyleServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     NativeStyleServiceClient nativeStyleServiceClient =
         NativeStyleServiceClient.create(nativeStyleServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NativeStyleServiceClient

## Static Methods 

### create()
    
    
    public static final NativeStyleServiceClient create()

Constructs an instance of NativeStyleServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NativeStyleServiceSettings settings)
    
    
    public static final NativeStyleServiceClient create(NativeStyleServiceSettings settings)

Constructs an instance of NativeStyleServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NativeStyleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NativeStyleServiceStub stub)
    
    
    public static final NativeStyleServiceClient create(NativeStyleServiceStub stub)

Constructs an instance of NativeStyleServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(NativeStyleServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NativeStyleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NativeStyleServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient)` |   
  
## Constructors 

### NativeStyleServiceClient(NativeStyleServiceSettings settings)
    
    
    protected NativeStyleServiceClient(NativeStyleServiceSettings settings)

Constructs an instance of NativeStyleServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NativeStyleServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceSettings)`  
  
  
### NativeStyleServiceClient(NativeStyleServiceStub stub)
    
    
    protected NativeStyleServiceClient(NativeStyleServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NativeStyleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NativeStyleServiceStub)`  
  
  
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
  
### batchActivateNativeStyles(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateNativeStylesResponse batchActivateNativeStyles(@Nullable NetworkName parent, List<String> names)

Beginning of non-CRUD Activates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateNativeStylesResponse response =
           nativeStyleServiceClient.batchActivateNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesResponse)` |   
  
### batchActivateNativeStyles(BatchActivateNativeStylesRequest request)
    
    
    public final BatchActivateNativeStylesResponse batchActivateNativeStyles(BatchActivateNativeStylesRequest request)

Beginning of non-CRUD Activates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchActivateNativeStylesRequest request =
           BatchActivateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateNativeStylesResponse response =
           nativeStyleServiceClient.batchActivateNativeStyles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesResponse)` |   
  
### batchActivateNativeStyles(String parent, List<String> names)
    
    
    public final BatchActivateNativeStylesResponse batchActivateNativeStyles(String parent, List<String> names)

Beginning of non-CRUD Activates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateNativeStylesResponse response =
           nativeStyleServiceClient.batchActivateNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesResponse)` |   
  
### batchActivateNativeStylesCallable()
    
    
    public final UnaryCallable<BatchActivateNativeStylesRequest,BatchActivateNativeStylesResponse> batchActivateNativeStylesCallable()

Beginning of non-CRUD Activates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchActivateNativeStylesRequest request =
           BatchActivateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateNativeStylesResponse> future =
           nativeStyleServiceClient.batchActivateNativeStylesCallable().futureCall(request);
       // Do something.
       BatchActivateNativeStylesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesRequest),[BatchActivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateNativeStylesResponse)>` |   
  
### batchArchiveNativeStyles(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveNativeStylesResponse batchArchiveNativeStyles(@Nullable NetworkName parent, List<String> names)

Archives a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveNativeStylesResponse response =
           nativeStyleServiceClient.batchArchiveNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesResponse)` |   
  
### batchArchiveNativeStyles(BatchArchiveNativeStylesRequest request)
    
    
    public final BatchArchiveNativeStylesResponse batchArchiveNativeStyles(BatchArchiveNativeStylesRequest request)

Archives a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchArchiveNativeStylesRequest request =
           BatchArchiveNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveNativeStylesResponse response =
           nativeStyleServiceClient.batchArchiveNativeStyles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesResponse)` |   
  
### batchArchiveNativeStyles(String parent, List<String> names)
    
    
    public final BatchArchiveNativeStylesResponse batchArchiveNativeStyles(String parent, List<String> names)

Archives a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveNativeStylesResponse response =
           nativeStyleServiceClient.batchArchiveNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesResponse)` |   
  
### batchArchiveNativeStylesCallable()
    
    
    public final UnaryCallable<BatchArchiveNativeStylesRequest,BatchArchiveNativeStylesResponse> batchArchiveNativeStylesCallable()

Archives a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchArchiveNativeStylesRequest request =
           BatchArchiveNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveNativeStylesResponse> future =
           nativeStyleServiceClient.batchArchiveNativeStylesCallable().futureCall(request);
       // Do something.
       BatchArchiveNativeStylesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesRequest),[BatchArchiveNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveNativeStylesResponse)>` |   
  
### batchCreateNativeStyles(@Nullable NetworkName parent, List<CreateNativeStyleRequest> requests)
    
    
    public final BatchCreateNativeStylesResponse batchCreateNativeStyles(@Nullable NetworkName parent, List<CreateNativeStyleRequest> requests)

Creates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateNativeStyleRequest> requests = new ArrayList<>();
       BatchCreateNativeStylesResponse response =
           nativeStyleServiceClient.batchCreateNativeStyles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `NativeStyles` will be created. Format: `networks/{network_code}` The parent field in the CreateNativeStyleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateNativeStyleRequest)>`  
Required. The `NativeStyle` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesResponse)` |   
  
### batchCreateNativeStyles(BatchCreateNativeStylesRequest request)
    
    
    public final BatchCreateNativeStylesResponse batchCreateNativeStyles(BatchCreateNativeStylesRequest request)

Creates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchCreateNativeStylesRequest request =
           BatchCreateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateNativeStyleRequest>())
               .build();
       BatchCreateNativeStylesResponse response =
           nativeStyleServiceClient.batchCreateNativeStyles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesResponse)` |   
  
### batchCreateNativeStyles(String parent, List<CreateNativeStyleRequest> requests)
    
    
    public final BatchCreateNativeStylesResponse batchCreateNativeStyles(String parent, List<CreateNativeStyleRequest> requests)

Creates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateNativeStyleRequest> requests = new ArrayList<>();
       BatchCreateNativeStylesResponse response =
           nativeStyleServiceClient.batchCreateNativeStyles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `NativeStyles` will be created. Format: `networks/{network_code}` The parent field in the CreateNativeStyleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateNativeStyleRequest)>`  
Required. The `NativeStyle` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesResponse)` |   
  
### batchCreateNativeStylesCallable()
    
    
    public final UnaryCallable<BatchCreateNativeStylesRequest,BatchCreateNativeStylesResponse> batchCreateNativeStylesCallable()

Creates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchCreateNativeStylesRequest request =
           BatchCreateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateNativeStyleRequest>())
               .build();
       ApiFuture<BatchCreateNativeStylesResponse> future =
           nativeStyleServiceClient.batchCreateNativeStylesCallable().futureCall(request);
       // Do something.
       BatchCreateNativeStylesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesRequest),[BatchCreateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateNativeStylesResponse)>` |   
  
### batchDeactivateNativeStyles(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateNativeStylesResponse batchDeactivateNativeStyles(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateNativeStylesResponse response =
           nativeStyleServiceClient.batchDeactivateNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesResponse)` |   
  
### batchDeactivateNativeStyles(BatchDeactivateNativeStylesRequest request)
    
    
    public final BatchDeactivateNativeStylesResponse batchDeactivateNativeStyles(BatchDeactivateNativeStylesRequest request)

Deactivates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchDeactivateNativeStylesRequest request =
           BatchDeactivateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateNativeStylesResponse response =
           nativeStyleServiceClient.batchDeactivateNativeStyles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesResponse)` |   
  
### batchDeactivateNativeStyles(String parent, List<String> names)
    
    
    public final BatchDeactivateNativeStylesResponse batchDeactivateNativeStyles(String parent, List<String> names)

Deactivates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateNativeStylesResponse response =
           nativeStyleServiceClient.batchDeactivateNativeStyles(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the `NativeStyle`s. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesResponse)` |   
  
### batchDeactivateNativeStylesCallable()
    
    
    public final UnaryCallable<BatchDeactivateNativeStylesRequest,BatchDeactivateNativeStylesResponse> batchDeactivateNativeStylesCallable()

Deactivates a list of `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchDeactivateNativeStylesRequest request =
           BatchDeactivateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateNativeStylesResponse> future =
           nativeStyleServiceClient.batchDeactivateNativeStylesCallable().futureCall(request);
       // Do something.
       BatchDeactivateNativeStylesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesRequest),[BatchDeactivateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateNativeStylesResponse)>` |   
  
### batchUpdateNativeStyles(@Nullable NetworkName parent, List<UpdateNativeStyleRequest> requests)
    
    
    public final BatchUpdateNativeStylesResponse batchUpdateNativeStyles(@Nullable NetworkName parent, List<UpdateNativeStyleRequest> requests)

Batch updates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateNativeStyleRequest> requests = new ArrayList<>();
       BatchUpdateNativeStylesResponse response =
           nativeStyleServiceClient.batchUpdateNativeStyles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `NativeStyles` will be updated. Format: `networks/{network_code}` The parent field in the UpdateNativeStyleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateNativeStyleRequest)>`  
Required. The `NativeStyle` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesResponse)` |   
  
### batchUpdateNativeStyles(BatchUpdateNativeStylesRequest request)
    
    
    public final BatchUpdateNativeStylesResponse batchUpdateNativeStyles(BatchUpdateNativeStylesRequest request)

Batch updates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchUpdateNativeStylesRequest request =
           BatchUpdateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateNativeStyleRequest>())
               .build();
       BatchUpdateNativeStylesResponse response =
           nativeStyleServiceClient.batchUpdateNativeStyles(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesResponse)` |   
  
### batchUpdateNativeStyles(String parent, List<UpdateNativeStyleRequest> requests)
    
    
    public final BatchUpdateNativeStylesResponse batchUpdateNativeStyles(String parent, List<UpdateNativeStyleRequest> requests)

Batch updates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateNativeStyleRequest> requests = new ArrayList<>();
       BatchUpdateNativeStylesResponse response =
           nativeStyleServiceClient.batchUpdateNativeStyles(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `NativeStyles` will be updated. Format: `networks/{network_code}` The parent field in the UpdateNativeStyleRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateNativeStyleRequest)>`  
Required. The `NativeStyle` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesResponse)` |   
  
### batchUpdateNativeStylesCallable()
    
    
    public final UnaryCallable<BatchUpdateNativeStylesRequest,BatchUpdateNativeStylesResponse> batchUpdateNativeStylesCallable()

Batch updates `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       BatchUpdateNativeStylesRequest request =
           BatchUpdateNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateNativeStyleRequest>())
               .build();
       ApiFuture<BatchUpdateNativeStylesResponse> future =
           nativeStyleServiceClient.batchUpdateNativeStylesCallable().futureCall(request);
       // Do something.
       BatchUpdateNativeStylesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesRequest),[BatchUpdateNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateNativeStylesResponse)>` |   
  
### close()
    
    
    public final void close()

### getNativeStyle(@Nullable NativeStyleName name)
    
    
    public final NativeStyle getNativeStyle(@Nullable NativeStyleName name)

Retrieves a `NativeStyle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NativeStyleName name = NativeStyleName.of("[NETWORK_CODE]", "[NATIVE_STYLE]");
       NativeStyle response = nativeStyleServiceClient.getNativeStyle(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NativeStyleName`  
Required. The resource name of the NativeStyle. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyle)` |   
  
### getNativeStyle(GetNativeStyleRequest request)
    
    
    public final NativeStyle getNativeStyle(GetNativeStyleRequest request)

Retrieves a `NativeStyle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       GetNativeStyleRequest request =
           GetNativeStyleRequest.newBuilder()
               .setName(NativeStyleName.of("[NETWORK_CODE]", "[NATIVE_STYLE]").toString())
               .build();
       NativeStyle response = nativeStyleServiceClient.getNativeStyle(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetNativeStyleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyle)` |   
  
### getNativeStyle(String name)
    
    
    public final NativeStyle getNativeStyle(String name)

Retrieves a `NativeStyle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String name = NativeStyleName.of("[NETWORK_CODE]", "[NATIVE_STYLE]").toString();
       NativeStyle response = nativeStyleServiceClient.getNativeStyle(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the NativeStyle. Format: `networks/{network_code}/nativeStyles/{native_style_id}`  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyle)` |   
  
### getNativeStyleCallable()
    
    
    public final UnaryCallable<GetNativeStyleRequest,NativeStyle> getNativeStyleCallable()

Retrieves a `NativeStyle` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       GetNativeStyleRequest request =
           GetNativeStyleRequest.newBuilder()
               .setName(NativeStyleName.of("[NETWORK_CODE]", "[NATIVE_STYLE]").toString())
               .build();
       ApiFuture<NativeStyle> future =
           nativeStyleServiceClient.getNativeStyleCallable().futureCall(request);
       // Do something.
       NativeStyle response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNativeStyleRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetNativeStyleRequest),[NativeStyle](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyle)>` |   
  
### getSettings()
    
    
    public final @Nullable NativeStyleServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NativeStyleServiceSettings` |   
  
### getStub()
    
    
    public NativeStyleServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.NativeStyleServiceStub)` |   
  
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
  
### listNativeStyles(@Nullable NetworkName parent)
    
    
    public final NativeStyleServiceClient.ListNativeStylesPagedResponse listNativeStyles(@Nullable NetworkName parent)

Lists `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (NativeStyle element : nativeStyleServiceClient.listNativeStyles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of NativeStyles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient.ListNativeStylesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient.ListNativeStylesPagedResponse)` |   
  
### listNativeStyles(ListNativeStylesRequest request)
    
    
    public final NativeStyleServiceClient.ListNativeStylesPagedResponse listNativeStyles(ListNativeStylesRequest request)

Lists `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       ListNativeStylesRequest request =
           ListNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (NativeStyle element : nativeStyleServiceClient.listNativeStyles(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNativeStylesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient.ListNativeStylesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient.ListNativeStylesPagedResponse)` |   
  
### listNativeStyles(String parent)
    
    
    public final NativeStyleServiceClient.ListNativeStylesPagedResponse listNativeStyles(String parent)

Lists `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (NativeStyle element : nativeStyleServiceClient.listNativeStyles(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of NativeStyles. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[NativeStyleServiceClient.ListNativeStylesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient.ListNativeStylesPagedResponse)` |   
  
### listNativeStylesCallable()
    
    
    public final UnaryCallable<ListNativeStylesRequest,ListNativeStylesResponse> listNativeStylesCallable()

Lists `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       ListNativeStylesRequest request =
           ListNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListNativeStylesResponse response =
             nativeStyleServiceClient.listNativeStylesCallable().call(request);
         for (NativeStyle element : response.getNativeStylesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNativeStylesRequest),[ListNativeStylesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNativeStylesResponse)>` |   
  
### listNativeStylesPagedCallable()
    
    
    public final UnaryCallable<ListNativeStylesRequest,NativeStyleServiceClient.ListNativeStylesPagedResponse> listNativeStylesPagedCallable()

Lists `NativeStyle` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NativeStyleServiceClient nativeStyleServiceClient = NativeStyleServiceClient.create()) {
       ListNativeStylesRequest request =
           ListNativeStylesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<NativeStyle> future =
           nativeStyleServiceClient.listNativeStylesPagedCallable().futureCall(request);
       // Do something.
       for (NativeStyle element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNativeStylesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListNativeStylesRequest),[ListNativeStylesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.NativeStyleServiceClient.ListNativeStylesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
