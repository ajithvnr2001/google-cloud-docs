---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient
title: Class DaiAuthenticationKeyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:42.623616+00:00
---

# Class DaiAuthenticationKeyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DaiAuthenticationKeyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/DaiAuthenticationKeyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `DaiAuthenticationKey` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       DaiAuthenticationKeyName name =
           DaiAuthenticationKeyName.of("[NETWORK_CODE]", "[DAI_AUTHENTICATION_KEY]");
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.getDaiAuthenticationKey(name);
     }
     

Note: close() needs to be called on the DaiAuthenticationKeyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDaiAuthenticationKey |  Retrieves a `DaiAuthenticationKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDaiAuthenticationKey(GetDaiAuthenticationKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDaiAuthenticationKey(DaiAuthenticationKeyName name) 
  * getDaiAuthenticationKey(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDaiAuthenticationKeyCallable() 

  
ListDaiAuthenticationKeys |  Lists `DaiAuthenticationKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDaiAuthenticationKeys(ListDaiAuthenticationKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDaiAuthenticationKeys(NetworkName parent) 
  * listDaiAuthenticationKeys(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDaiAuthenticationKeysPagedCallable() 
  * listDaiAuthenticationKeysCallable() 

  
CreateDaiAuthenticationKey |  Creates a `DaiAuthenticationKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDaiAuthenticationKey(CreateDaiAuthenticationKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDaiAuthenticationKey(NetworkName parent, DaiAuthenticationKey daiAuthenticationKey) 
  * createDaiAuthenticationKey(String parent, DaiAuthenticationKey daiAuthenticationKey) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDaiAuthenticationKeyCallable() 

  
BatchCreateDaiAuthenticationKeys |  Batch creates `DaiAuthenticationKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateDaiAuthenticationKeys(NetworkName parent, List<CreateDaiAuthenticationKeyRequest> requests) 
  * batchCreateDaiAuthenticationKeys(String parent, List<CreateDaiAuthenticationKeyRequest> requests) 
  * batchCreateDaiAuthenticationKeys(BatchCreateDaiAuthenticationKeysRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateDaiAuthenticationKeysCallable() 

  
UpdateDaiAuthenticationKey |  Updates a `DaiAuthenticationKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDaiAuthenticationKey(UpdateDaiAuthenticationKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDaiAuthenticationKey(DaiAuthenticationKey daiAuthenticationKey, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDaiAuthenticationKeyCallable() 

  
BatchUpdateDaiAuthenticationKeys |  Batch updates `DaiAuthenticationKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateDaiAuthenticationKeys(NetworkName parent, List<UpdateDaiAuthenticationKeyRequest> requests) 
  * batchUpdateDaiAuthenticationKeys(String parent, List<UpdateDaiAuthenticationKeyRequest> requests) 
  * batchUpdateDaiAuthenticationKeys(BatchUpdateDaiAuthenticationKeysRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateDaiAuthenticationKeysCallable() 

  
BatchActivateDaiAuthenticationKeys |  Activates a list of `DaiAuthenticationKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateDaiAuthenticationKeys(BatchActivateDaiAuthenticationKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateDaiAuthenticationKeys(NetworkName parent, List<String> names) 
  * batchActivateDaiAuthenticationKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateDaiAuthenticationKeysCallable() 

  
BatchDeactivateDaiAuthenticationKeys |  Deactivates a list of `DaiAuthenticationKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateDaiAuthenticationKeys(BatchDeactivateDaiAuthenticationKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateDaiAuthenticationKeys(NetworkName parent, List<String> names) 
  * batchDeactivateDaiAuthenticationKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateDaiAuthenticationKeysCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DaiAuthenticationKeyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiAuthenticationKeyServiceSettings daiAuthenticationKeyServiceSettings =
         DaiAuthenticationKeyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create(daiAuthenticationKeyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DaiAuthenticationKeyServiceSettings daiAuthenticationKeyServiceSettings =
         DaiAuthenticationKeyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create(daiAuthenticationKeyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DaiAuthenticationKeyServiceClient

## Static Methods 

### create()
    
    
    public static final DaiAuthenticationKeyServiceClient create()

Constructs an instance of DaiAuthenticationKeyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiAuthenticationKeyServiceSettings settings)
    
    
    public static final DaiAuthenticationKeyServiceClient create(DaiAuthenticationKeyServiceSettings settings)

Constructs an instance of DaiAuthenticationKeyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiAuthenticationKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DaiAuthenticationKeyServiceStub stub)
    
    
    public static final DaiAuthenticationKeyServiceClient create(DaiAuthenticationKeyServiceStub stub)

Constructs an instance of DaiAuthenticationKeyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DaiAuthenticationKeyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiAuthenticationKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiAuthenticationKeyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient)` |   
  
## Constructors 

### DaiAuthenticationKeyServiceClient(DaiAuthenticationKeyServiceSettings settings)
    
    
    protected DaiAuthenticationKeyServiceClient(DaiAuthenticationKeyServiceSettings settings)

Constructs an instance of DaiAuthenticationKeyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DaiAuthenticationKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceSettings)`  
  
  
### DaiAuthenticationKeyServiceClient(DaiAuthenticationKeyServiceStub stub)
    
    
    protected DaiAuthenticationKeyServiceClient(DaiAuthenticationKeyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DaiAuthenticationKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiAuthenticationKeyServiceStub)`  
  
  
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
  
### batchActivateDaiAuthenticationKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateDaiAuthenticationKeysResponse batchActivateDaiAuthenticationKeys(@Nullable NetworkName parent, List<String> names)

Activates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchActivateDaiAuthenticationKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the DaiAuthenticationKey. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysResponse)` |   
  
### batchActivateDaiAuthenticationKeys(BatchActivateDaiAuthenticationKeysRequest request)
    
    
    public final BatchActivateDaiAuthenticationKeysResponse batchActivateDaiAuthenticationKeys(BatchActivateDaiAuthenticationKeysRequest request)

Activates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchActivateDaiAuthenticationKeysRequest request =
           BatchActivateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchActivateDaiAuthenticationKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysResponse)` |   
  
### batchActivateDaiAuthenticationKeys(String parent, List<String> names)
    
    
    public final BatchActivateDaiAuthenticationKeysResponse batchActivateDaiAuthenticationKeys(String parent, List<String> names)

Activates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchActivateDaiAuthenticationKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the DaiAuthenticationKey. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysResponse)` |   
  
### batchActivateDaiAuthenticationKeysCallable()
    
    
    public final UnaryCallable<BatchActivateDaiAuthenticationKeysRequest,BatchActivateDaiAuthenticationKeysResponse> batchActivateDaiAuthenticationKeysCallable()

Activates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchActivateDaiAuthenticationKeysRequest request =
           BatchActivateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateDaiAuthenticationKeysResponse> future =
           daiAuthenticationKeyServiceClient
               .batchActivateDaiAuthenticationKeysCallable()
               .futureCall(request);
       // Do something.
       BatchActivateDaiAuthenticationKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysRequest),[BatchActivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateDaiAuthenticationKeysResponse)>` |   
  
### batchCreateDaiAuthenticationKeys(@Nullable NetworkName parent, List<CreateDaiAuthenticationKeyRequest> requests)
    
    
    public final BatchCreateDaiAuthenticationKeysResponse batchCreateDaiAuthenticationKeys(@Nullable NetworkName parent, List<CreateDaiAuthenticationKeyRequest> requests)

Batch creates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateDaiAuthenticationKeyRequest> requests = new ArrayList<>();
       BatchCreateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchCreateDaiAuthenticationKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `DaiAuthenticationKeys` will be created. Format: `networks/{network_code}` The parent field in the CreateDaiAuthenticationKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiAuthenticationKeyRequest)>`  
Required. The `DaiAuthenticationKey` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysResponse)` |   
  
### batchCreateDaiAuthenticationKeys(BatchCreateDaiAuthenticationKeysRequest request)
    
    
    public final BatchCreateDaiAuthenticationKeysResponse batchCreateDaiAuthenticationKeys(BatchCreateDaiAuthenticationKeysRequest request)

Batch creates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchCreateDaiAuthenticationKeysRequest request =
           BatchCreateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateDaiAuthenticationKeyRequest>())
               .build();
       BatchCreateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchCreateDaiAuthenticationKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysResponse)` |   
  
### batchCreateDaiAuthenticationKeys(String parent, List<CreateDaiAuthenticationKeyRequest> requests)
    
    
    public final BatchCreateDaiAuthenticationKeysResponse batchCreateDaiAuthenticationKeys(String parent, List<CreateDaiAuthenticationKeyRequest> requests)

Batch creates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateDaiAuthenticationKeyRequest> requests = new ArrayList<>();
       BatchCreateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchCreateDaiAuthenticationKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `DaiAuthenticationKeys` will be created. Format: `networks/{network_code}` The parent field in the CreateDaiAuthenticationKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiAuthenticationKeyRequest)>`  
Required. The `DaiAuthenticationKey` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysResponse)` |   
  
### batchCreateDaiAuthenticationKeysCallable()
    
    
    public final UnaryCallable<BatchCreateDaiAuthenticationKeysRequest,BatchCreateDaiAuthenticationKeysResponse> batchCreateDaiAuthenticationKeysCallable()

Batch creates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchCreateDaiAuthenticationKeysRequest request =
           BatchCreateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateDaiAuthenticationKeyRequest>())
               .build();
       ApiFuture<BatchCreateDaiAuthenticationKeysResponse> future =
           daiAuthenticationKeyServiceClient
               .batchCreateDaiAuthenticationKeysCallable()
               .futureCall(request);
       // Do something.
       BatchCreateDaiAuthenticationKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysRequest),[BatchCreateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateDaiAuthenticationKeysResponse)>` |   
  
### batchDeactivateDaiAuthenticationKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateDaiAuthenticationKeysResponse batchDeactivateDaiAuthenticationKeys(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchDeactivateDaiAuthenticationKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the DaiAuthenticationKey. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysResponse)` |   
  
### batchDeactivateDaiAuthenticationKeys(BatchDeactivateDaiAuthenticationKeysRequest request)
    
    
    public final BatchDeactivateDaiAuthenticationKeysResponse batchDeactivateDaiAuthenticationKeys(BatchDeactivateDaiAuthenticationKeysRequest request)

Deactivates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchDeactivateDaiAuthenticationKeysRequest request =
           BatchDeactivateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchDeactivateDaiAuthenticationKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysResponse)` |   
  
### batchDeactivateDaiAuthenticationKeys(String parent, List<String> names)
    
    
    public final BatchDeactivateDaiAuthenticationKeysResponse batchDeactivateDaiAuthenticationKeys(String parent, List<String> names)

Deactivates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchDeactivateDaiAuthenticationKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. Resource names for the DaiAuthenticationKey. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysResponse)` |   
  
### batchDeactivateDaiAuthenticationKeysCallable()
    
    
    public final UnaryCallable<BatchDeactivateDaiAuthenticationKeysRequest,BatchDeactivateDaiAuthenticationKeysResponse> batchDeactivateDaiAuthenticationKeysCallable()

Deactivates a list of `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchDeactivateDaiAuthenticationKeysRequest request =
           BatchDeactivateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateDaiAuthenticationKeysResponse> future =
           daiAuthenticationKeyServiceClient
               .batchDeactivateDaiAuthenticationKeysCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateDaiAuthenticationKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysRequest),[BatchDeactivateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateDaiAuthenticationKeysResponse)>` |   
  
### batchUpdateDaiAuthenticationKeys(@Nullable NetworkName parent, List<UpdateDaiAuthenticationKeyRequest> requests)
    
    
    public final BatchUpdateDaiAuthenticationKeysResponse batchUpdateDaiAuthenticationKeys(@Nullable NetworkName parent, List<UpdateDaiAuthenticationKeyRequest> requests)

Batch updates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateDaiAuthenticationKeyRequest> requests = new ArrayList<>();
       BatchUpdateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchUpdateDaiAuthenticationKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `DaiAuthenticationKeys` will be updated. Format: `networks/{network_code}` The parent field in the UpdateDaiAuthenticationKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiAuthenticationKeyRequest)>`  
Required. The `DaiAuthenticationKey` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysResponse)` |   
  
### batchUpdateDaiAuthenticationKeys(BatchUpdateDaiAuthenticationKeysRequest request)
    
    
    public final BatchUpdateDaiAuthenticationKeysResponse batchUpdateDaiAuthenticationKeys(BatchUpdateDaiAuthenticationKeysRequest request)

Batch updates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchUpdateDaiAuthenticationKeysRequest request =
           BatchUpdateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateDaiAuthenticationKeyRequest>())
               .build();
       BatchUpdateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchUpdateDaiAuthenticationKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysResponse)` |   
  
### batchUpdateDaiAuthenticationKeys(String parent, List<UpdateDaiAuthenticationKeyRequest> requests)
    
    
    public final BatchUpdateDaiAuthenticationKeysResponse batchUpdateDaiAuthenticationKeys(String parent, List<UpdateDaiAuthenticationKeyRequest> requests)

Batch updates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateDaiAuthenticationKeyRequest> requests = new ArrayList<>();
       BatchUpdateDaiAuthenticationKeysResponse response =
           daiAuthenticationKeyServiceClient.batchUpdateDaiAuthenticationKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `DaiAuthenticationKeys` will be updated. Format: `networks/{network_code}` The parent field in the UpdateDaiAuthenticationKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiAuthenticationKeyRequest)>`  
Required. The `DaiAuthenticationKey` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysResponse)` |   
  
### batchUpdateDaiAuthenticationKeysCallable()
    
    
    public final UnaryCallable<BatchUpdateDaiAuthenticationKeysRequest,BatchUpdateDaiAuthenticationKeysResponse> batchUpdateDaiAuthenticationKeysCallable()

Batch updates `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       BatchUpdateDaiAuthenticationKeysRequest request =
           BatchUpdateDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateDaiAuthenticationKeyRequest>())
               .build();
       ApiFuture<BatchUpdateDaiAuthenticationKeysResponse> future =
           daiAuthenticationKeyServiceClient
               .batchUpdateDaiAuthenticationKeysCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateDaiAuthenticationKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysRequest),[BatchUpdateDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateDaiAuthenticationKeysResponse)>` |   
  
### close()
    
    
    public final void close()

### createDaiAuthenticationKey(@Nullable NetworkName parent, DaiAuthenticationKey daiAuthenticationKey)
    
    
    public final DaiAuthenticationKey createDaiAuthenticationKey(@Nullable NetworkName parent, DaiAuthenticationKey daiAuthenticationKey)

Creates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       DaiAuthenticationKey daiAuthenticationKey = DaiAuthenticationKey.newBuilder().build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.createDaiAuthenticationKey(
               parent, daiAuthenticationKey);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `DaiAuthenticationKey` will be created. Format: `networks/{network_code}`  
`daiAuthenticationKey` | `[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)`  
Required. The `DaiAuthenticationKey` to create.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### createDaiAuthenticationKey(CreateDaiAuthenticationKeyRequest request)
    
    
    public final DaiAuthenticationKey createDaiAuthenticationKey(CreateDaiAuthenticationKeyRequest request)

Creates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       CreateDaiAuthenticationKeyRequest request =
           CreateDaiAuthenticationKeyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setDaiAuthenticationKey(DaiAuthenticationKey.newBuilder().build())
               .build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.createDaiAuthenticationKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiAuthenticationKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### createDaiAuthenticationKey(String parent, DaiAuthenticationKey daiAuthenticationKey)
    
    
    public final DaiAuthenticationKey createDaiAuthenticationKey(String parent, DaiAuthenticationKey daiAuthenticationKey)

Creates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       DaiAuthenticationKey daiAuthenticationKey = DaiAuthenticationKey.newBuilder().build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.createDaiAuthenticationKey(
               parent, daiAuthenticationKey);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `DaiAuthenticationKey` will be created. Format: `networks/{network_code}`  
`daiAuthenticationKey` | `[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)`  
Required. The `DaiAuthenticationKey` to create.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### createDaiAuthenticationKeyCallable()
    
    
    public final UnaryCallable<CreateDaiAuthenticationKeyRequest,DaiAuthenticationKey> createDaiAuthenticationKeyCallable()

Creates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       CreateDaiAuthenticationKeyRequest request =
           CreateDaiAuthenticationKeyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setDaiAuthenticationKey(DaiAuthenticationKey.newBuilder().build())
               .build();
       ApiFuture<DaiAuthenticationKey> future =
           daiAuthenticationKeyServiceClient
               .createDaiAuthenticationKeyCallable()
               .futureCall(request);
       // Do something.
       DaiAuthenticationKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateDaiAuthenticationKeyRequest),[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)>` |   
  
### getDaiAuthenticationKey(@Nullable DaiAuthenticationKeyName name)
    
    
    public final DaiAuthenticationKey getDaiAuthenticationKey(@Nullable DaiAuthenticationKeyName name)

Retrieves a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       DaiAuthenticationKeyName name =
           DaiAuthenticationKeyName.of("[NETWORK_CODE]", "[DAI_AUTHENTICATION_KEY]");
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.getDaiAuthenticationKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiAuthenticationKeyName`  
Required. The resource name of the `DaiAuthenticationKey`. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### getDaiAuthenticationKey(GetDaiAuthenticationKeyRequest request)
    
    
    public final DaiAuthenticationKey getDaiAuthenticationKey(GetDaiAuthenticationKeyRequest request)

Retrieves a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       GetDaiAuthenticationKeyRequest request =
           GetDaiAuthenticationKeyRequest.newBuilder()
               .setName(
                   DaiAuthenticationKeyName.of("[NETWORK_CODE]", "[DAI_AUTHENTICATION_KEY]")
                       .toString())
               .build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.getDaiAuthenticationKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiAuthenticationKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### getDaiAuthenticationKey(String name)
    
    
    public final DaiAuthenticationKey getDaiAuthenticationKey(String name)

Retrieves a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String name =
           DaiAuthenticationKeyName.of("[NETWORK_CODE]", "[DAI_AUTHENTICATION_KEY]").toString();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.getDaiAuthenticationKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the `DaiAuthenticationKey`. Format: `networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### getDaiAuthenticationKeyCallable()
    
    
    public final UnaryCallable<GetDaiAuthenticationKeyRequest,DaiAuthenticationKey> getDaiAuthenticationKeyCallable()

Retrieves a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       GetDaiAuthenticationKeyRequest request =
           GetDaiAuthenticationKeyRequest.newBuilder()
               .setName(
                   DaiAuthenticationKeyName.of("[NETWORK_CODE]", "[DAI_AUTHENTICATION_KEY]")
                       .toString())
               .build();
       ApiFuture<DaiAuthenticationKey> future =
           daiAuthenticationKeyServiceClient.getDaiAuthenticationKeyCallable().futureCall(request);
       // Do something.
       DaiAuthenticationKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetDaiAuthenticationKeyRequest),[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)>` |   
  
### getSettings()
    
    
    public final @Nullable DaiAuthenticationKeyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.DaiAuthenticationKeyServiceSettings` |   
  
### getStub()
    
    
    public DaiAuthenticationKeyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.DaiAuthenticationKeyServiceStub)` |   
  
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
  
### listDaiAuthenticationKeys(@Nullable NetworkName parent)
    
    
    public final DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse listDaiAuthenticationKeys(@Nullable NetworkName parent)

Lists `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (DaiAuthenticationKey element :
           daiAuthenticationKeyServiceClient.listDaiAuthenticationKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of DaiAuthenticationKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse)` |   
  
### listDaiAuthenticationKeys(ListDaiAuthenticationKeysRequest request)
    
    
    public final DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse listDaiAuthenticationKeys(ListDaiAuthenticationKeysRequest request)

Lists `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       ListDaiAuthenticationKeysRequest request =
           ListDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (DaiAuthenticationKey element :
           daiAuthenticationKeyServiceClient.listDaiAuthenticationKeys(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiAuthenticationKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse)` |   
  
### listDaiAuthenticationKeys(String parent)
    
    
    public final DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse listDaiAuthenticationKeys(String parent)

Lists `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (DaiAuthenticationKey element :
           daiAuthenticationKeyServiceClient.listDaiAuthenticationKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of DaiAuthenticationKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse)` |   
  
### listDaiAuthenticationKeysCallable()
    
    
    public final UnaryCallable<ListDaiAuthenticationKeysRequest,ListDaiAuthenticationKeysResponse> listDaiAuthenticationKeysCallable()

Lists `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       ListDaiAuthenticationKeysRequest request =
           ListDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListDaiAuthenticationKeysResponse response =
             daiAuthenticationKeyServiceClient.listDaiAuthenticationKeysCallable().call(request);
         for (DaiAuthenticationKey element : response.getDaiAuthenticationKeysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiAuthenticationKeysRequest),[ListDaiAuthenticationKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiAuthenticationKeysResponse)>` |   
  
### listDaiAuthenticationKeysPagedCallable()
    
    
    public final UnaryCallable<ListDaiAuthenticationKeysRequest,DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse> listDaiAuthenticationKeysPagedCallable()

Lists `DaiAuthenticationKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       ListDaiAuthenticationKeysRequest request =
           ListDaiAuthenticationKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<DaiAuthenticationKey> future =
           daiAuthenticationKeyServiceClient
               .listDaiAuthenticationKeysPagedCallable()
               .futureCall(request);
       // Do something.
       for (DaiAuthenticationKey element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDaiAuthenticationKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListDaiAuthenticationKeysRequest),[ListDaiAuthenticationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKeyServiceClient.ListDaiAuthenticationKeysPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDaiAuthenticationKey(DaiAuthenticationKey daiAuthenticationKey, FieldMask updateMask)
    
    
    public final DaiAuthenticationKey updateDaiAuthenticationKey(DaiAuthenticationKey daiAuthenticationKey, FieldMask updateMask)

Updates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       DaiAuthenticationKey daiAuthenticationKey = DaiAuthenticationKey.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.updateDaiAuthenticationKey(
               daiAuthenticationKey, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`daiAuthenticationKey` | `[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)`  
Required. The `DaiAuthenticationKey` to update. The `DaiAuthenticationKey`'s `name` is used to identify the `DaiAuthenticationKey` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### updateDaiAuthenticationKey(UpdateDaiAuthenticationKeyRequest request)
    
    
    public final DaiAuthenticationKey updateDaiAuthenticationKey(UpdateDaiAuthenticationKeyRequest request)

Updates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       UpdateDaiAuthenticationKeyRequest request =
           UpdateDaiAuthenticationKeyRequest.newBuilder()
               .setDaiAuthenticationKey(DaiAuthenticationKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DaiAuthenticationKey response =
           daiAuthenticationKeyServiceClient.updateDaiAuthenticationKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiAuthenticationKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)` |   
  
### updateDaiAuthenticationKeyCallable()
    
    
    public final UnaryCallable<UpdateDaiAuthenticationKeyRequest,DaiAuthenticationKey> updateDaiAuthenticationKeyCallable()

Updates a `DaiAuthenticationKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DaiAuthenticationKeyServiceClient daiAuthenticationKeyServiceClient =
         DaiAuthenticationKeyServiceClient.create()) {
       UpdateDaiAuthenticationKeyRequest request =
           UpdateDaiAuthenticationKeyRequest.newBuilder()
               .setDaiAuthenticationKey(DaiAuthenticationKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DaiAuthenticationKey> future =
           daiAuthenticationKeyServiceClient
               .updateDaiAuthenticationKeyCallable()
               .futureCall(request);
       // Do something.
       DaiAuthenticationKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDaiAuthenticationKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateDaiAuthenticationKeyRequest),[DaiAuthenticationKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiAuthenticationKey)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
