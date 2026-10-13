---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient
title: Class CustomTargetingKeyServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:40.753518+00:00
---

# Class CustomTargetingKeyServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CustomTargetingKeyServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CustomTargetingKeyServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CustomTargetingKey` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       CustomTargetingKeyName name =
           CustomTargetingKeyName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_KEY]");
       CustomTargetingKey response = customTargetingKeyServiceClient.getCustomTargetingKey(name);
     }
     

Note: close() needs to be called on the CustomTargetingKeyServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCustomTargetingKey |  Retrieves a `CustomTargetingKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomTargetingKey(GetCustomTargetingKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomTargetingKey(CustomTargetingKeyName name) 
  * getCustomTargetingKey(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomTargetingKeyCallable() 

  
ListCustomTargetingKeys |  Lists `CustomTargetingKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomTargetingKeys(ListCustomTargetingKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomTargetingKeys(NetworkName parent) 
  * listCustomTargetingKeys(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomTargetingKeysPagedCallable() 
  * listCustomTargetingKeysCallable() 

  
CreateCustomTargetingKey |  Creates a `CustomTargetingKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomTargetingKey(CreateCustomTargetingKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomTargetingKey(NetworkName parent, CustomTargetingKey customTargetingKey) 
  * createCustomTargetingKey(String parent, CustomTargetingKey customTargetingKey) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomTargetingKeyCallable() 

  
BatchCreateCustomTargetingKeys |  Creates `CustomTargetingKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCustomTargetingKeys(NetworkName parent, List<CreateCustomTargetingKeyRequest> requests) 
  * batchCreateCustomTargetingKeys(String parent, List<CreateCustomTargetingKeyRequest> requests) 
  * batchCreateCustomTargetingKeys(BatchCreateCustomTargetingKeysRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCustomTargetingKeysCallable() 

  
UpdateCustomTargetingKey |  Updates a `CustomTargetingKey` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomTargetingKey(UpdateCustomTargetingKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCustomTargetingKey(CustomTargetingKey customTargetingKey, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomTargetingKeyCallable() 

  
BatchUpdateCustomTargetingKeys |  Batch updates `CustomTargetingKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCustomTargetingKeys(NetworkName parent, List<UpdateCustomTargetingKeyRequest> requests) 
  * batchUpdateCustomTargetingKeys(String parent, List<UpdateCustomTargetingKeyRequest> requests) 
  * batchUpdateCustomTargetingKeys(BatchUpdateCustomTargetingKeysRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCustomTargetingKeysCallable() 

  
BatchActivateCustomTargetingKeys |  Batch activates `CustomTargetingKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCustomTargetingKeys(BatchActivateCustomTargetingKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateCustomTargetingKeys(NetworkName parent, List<String> names) 
  * batchActivateCustomTargetingKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCustomTargetingKeysCallable() 

  
BatchDeactivateCustomTargetingKeys |  Deactivates a list of `CustomTargetingKey` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCustomTargetingKeys(BatchDeactivateCustomTargetingKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateCustomTargetingKeys(NetworkName parent, List<String> names) 
  * batchDeactivateCustomTargetingKeys(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCustomTargetingKeysCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CustomTargetingKeyServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomTargetingKeyServiceSettings customTargetingKeyServiceSettings =
         CustomTargetingKeyServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create(customTargetingKeyServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomTargetingKeyServiceSettings customTargetingKeyServiceSettings =
         CustomTargetingKeyServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create(customTargetingKeyServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CustomTargetingKeyServiceClient

## Static Methods 

### create()
    
    
    public static final CustomTargetingKeyServiceClient create()

Constructs an instance of CustomTargetingKeyServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomTargetingKeyServiceSettings settings)
    
    
    public static final CustomTargetingKeyServiceClient create(CustomTargetingKeyServiceSettings settings)

Constructs an instance of CustomTargetingKeyServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomTargetingKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomTargetingKeyServiceStub stub)
    
    
    public static final CustomTargetingKeyServiceClient create(CustomTargetingKeyServiceStub stub)

Constructs an instance of CustomTargetingKeyServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CustomTargetingKeyServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomTargetingKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingKeyServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient)` |   
  
## Constructors 

### CustomTargetingKeyServiceClient(CustomTargetingKeyServiceSettings settings)
    
    
    protected CustomTargetingKeyServiceClient(CustomTargetingKeyServiceSettings settings)

Constructs an instance of CustomTargetingKeyServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomTargetingKeyServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceSettings)`  
  
  
### CustomTargetingKeyServiceClient(CustomTargetingKeyServiceStub stub)
    
    
    protected CustomTargetingKeyServiceClient(CustomTargetingKeyServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomTargetingKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingKeyServiceStub)`  
  
  
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
  
### batchActivateCustomTargetingKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateCustomTargetingKeysResponse batchActivateCustomTargetingKeys(@Nullable NetworkName parent, List<String> names)

Batch activates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchActivateCustomTargetingKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomTargetingKey`s to activate. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysResponse)` |   
  
### batchActivateCustomTargetingKeys(BatchActivateCustomTargetingKeysRequest request)
    
    
    public final BatchActivateCustomTargetingKeysResponse batchActivateCustomTargetingKeys(BatchActivateCustomTargetingKeysRequest request)

Batch activates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchActivateCustomTargetingKeysRequest request =
           BatchActivateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchActivateCustomTargetingKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysResponse)` |   
  
### batchActivateCustomTargetingKeys(String parent, List<String> names)
    
    
    public final BatchActivateCustomTargetingKeysResponse batchActivateCustomTargetingKeys(String parent, List<String> names)

Batch activates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchActivateCustomTargetingKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomTargetingKey`s to activate. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysResponse)` |   
  
### batchActivateCustomTargetingKeysCallable()
    
    
    public final UnaryCallable<BatchActivateCustomTargetingKeysRequest,BatchActivateCustomTargetingKeysResponse> batchActivateCustomTargetingKeysCallable()

Batch activates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchActivateCustomTargetingKeysRequest request =
           BatchActivateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateCustomTargetingKeysResponse> future =
           customTargetingKeyServiceClient
               .batchActivateCustomTargetingKeysCallable()
               .futureCall(request);
       // Do something.
       BatchActivateCustomTargetingKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysRequest),[BatchActivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingKeysResponse)>` |   
  
### batchCreateCustomTargetingKeys(@Nullable NetworkName parent, List<CreateCustomTargetingKeyRequest> requests)
    
    
    public final BatchCreateCustomTargetingKeysResponse batchCreateCustomTargetingKeys(@Nullable NetworkName parent, List<CreateCustomTargetingKeyRequest> requests)

Creates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCustomTargetingKeyRequest> requests = new ArrayList<>();
       BatchCreateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchCreateCustomTargetingKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CustomTargetingKeys` will be created. Format: `networks/{network_code}` The parent field in the CreateCustomTargetingKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingKeyRequest)>`  
Required. The `CustomTargetingKey` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysResponse)` |   
  
### batchCreateCustomTargetingKeys(BatchCreateCustomTargetingKeysRequest request)
    
    
    public final BatchCreateCustomTargetingKeysResponse batchCreateCustomTargetingKeys(BatchCreateCustomTargetingKeysRequest request)

Creates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchCreateCustomTargetingKeysRequest request =
           BatchCreateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomTargetingKeyRequest>())
               .build();
       BatchCreateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchCreateCustomTargetingKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysResponse)` |   
  
### batchCreateCustomTargetingKeys(String parent, List<CreateCustomTargetingKeyRequest> requests)
    
    
    public final BatchCreateCustomTargetingKeysResponse batchCreateCustomTargetingKeys(String parent, List<CreateCustomTargetingKeyRequest> requests)

Creates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCustomTargetingKeyRequest> requests = new ArrayList<>();
       BatchCreateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchCreateCustomTargetingKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CustomTargetingKeys` will be created. Format: `networks/{network_code}` The parent field in the CreateCustomTargetingKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingKeyRequest)>`  
Required. The `CustomTargetingKey` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysResponse)` |   
  
### batchCreateCustomTargetingKeysCallable()
    
    
    public final UnaryCallable<BatchCreateCustomTargetingKeysRequest,BatchCreateCustomTargetingKeysResponse> batchCreateCustomTargetingKeysCallable()

Creates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchCreateCustomTargetingKeysRequest request =
           BatchCreateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomTargetingKeyRequest>())
               .build();
       ApiFuture<BatchCreateCustomTargetingKeysResponse> future =
           customTargetingKeyServiceClient
               .batchCreateCustomTargetingKeysCallable()
               .futureCall(request);
       // Do something.
       BatchCreateCustomTargetingKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysRequest),[BatchCreateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingKeysResponse)>` |   
  
### batchDeactivateCustomTargetingKeys(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateCustomTargetingKeysResponse batchDeactivateCustomTargetingKeys(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchDeactivateCustomTargetingKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomTargetingKey`s to deactivate. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysResponse)` |   
  
### batchDeactivateCustomTargetingKeys(BatchDeactivateCustomTargetingKeysRequest request)
    
    
    public final BatchDeactivateCustomTargetingKeysResponse batchDeactivateCustomTargetingKeys(BatchDeactivateCustomTargetingKeysRequest request)

Deactivates a list of `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchDeactivateCustomTargetingKeysRequest request =
           BatchDeactivateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchDeactivateCustomTargetingKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysResponse)` |   
  
### batchDeactivateCustomTargetingKeys(String parent, List<String> names)
    
    
    public final BatchDeactivateCustomTargetingKeysResponse batchDeactivateCustomTargetingKeys(String parent, List<String> names)

Deactivates a list of `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchDeactivateCustomTargetingKeys(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `CustomTargetingKey`s to deactivate. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysResponse)` |   
  
### batchDeactivateCustomTargetingKeysCallable()
    
    
    public final UnaryCallable<BatchDeactivateCustomTargetingKeysRequest,BatchDeactivateCustomTargetingKeysResponse> batchDeactivateCustomTargetingKeysCallable()

Deactivates a list of `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchDeactivateCustomTargetingKeysRequest request =
           BatchDeactivateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateCustomTargetingKeysResponse> future =
           customTargetingKeyServiceClient
               .batchDeactivateCustomTargetingKeysCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateCustomTargetingKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysRequest),[BatchDeactivateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingKeysResponse)>` |   
  
### batchUpdateCustomTargetingKeys(@Nullable NetworkName parent, List<UpdateCustomTargetingKeyRequest> requests)
    
    
    public final BatchUpdateCustomTargetingKeysResponse batchUpdateCustomTargetingKeys(@Nullable NetworkName parent, List<UpdateCustomTargetingKeyRequest> requests)

Batch updates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCustomTargetingKeyRequest> requests = new ArrayList<>();
       BatchUpdateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchUpdateCustomTargetingKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `CustomTargetingKeys` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCustomTargetingKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingKeyRequest)>`  
Required. The `CustomTargetingKey` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysResponse)` |   
  
### batchUpdateCustomTargetingKeys(BatchUpdateCustomTargetingKeysRequest request)
    
    
    public final BatchUpdateCustomTargetingKeysResponse batchUpdateCustomTargetingKeys(BatchUpdateCustomTargetingKeysRequest request)

Batch updates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchUpdateCustomTargetingKeysRequest request =
           BatchUpdateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomTargetingKeyRequest>())
               .build();
       BatchUpdateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchUpdateCustomTargetingKeys(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysResponse)` |   
  
### batchUpdateCustomTargetingKeys(String parent, List<UpdateCustomTargetingKeyRequest> requests)
    
    
    public final BatchUpdateCustomTargetingKeysResponse batchUpdateCustomTargetingKeys(String parent, List<UpdateCustomTargetingKeyRequest> requests)

Batch updates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCustomTargetingKeyRequest> requests = new ArrayList<>();
       BatchUpdateCustomTargetingKeysResponse response =
           customTargetingKeyServiceClient.batchUpdateCustomTargetingKeys(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `CustomTargetingKeys` will be updated. Format: `networks/{network_code}` The parent field in the UpdateCustomTargetingKeyRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingKeyRequest)>`  
Required. The `CustomTargetingKey` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysResponse)` |   
  
### batchUpdateCustomTargetingKeysCallable()
    
    
    public final UnaryCallable<BatchUpdateCustomTargetingKeysRequest,BatchUpdateCustomTargetingKeysResponse> batchUpdateCustomTargetingKeysCallable()

Batch updates `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       BatchUpdateCustomTargetingKeysRequest request =
           BatchUpdateCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomTargetingKeyRequest>())
               .build();
       ApiFuture<BatchUpdateCustomTargetingKeysResponse> future =
           customTargetingKeyServiceClient
               .batchUpdateCustomTargetingKeysCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateCustomTargetingKeysResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysRequest),[BatchUpdateCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingKeysResponse)>` |   
  
### close()
    
    
    public final void close()

### createCustomTargetingKey(@Nullable NetworkName parent, CustomTargetingKey customTargetingKey)
    
    
    public final CustomTargetingKey createCustomTargetingKey(@Nullable NetworkName parent, CustomTargetingKey customTargetingKey)

Creates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CustomTargetingKey customTargetingKey = CustomTargetingKey.newBuilder().build();
       CustomTargetingKey response =
           customTargetingKeyServiceClient.createCustomTargetingKey(parent, customTargetingKey);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `CustomTargetingKey` will be created. Format: `networks/{network_code}`  
`customTargetingKey` | `[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)`  
Required. The `CustomTargetingKey` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### createCustomTargetingKey(CreateCustomTargetingKeyRequest request)
    
    
    public final CustomTargetingKey createCustomTargetingKey(CreateCustomTargetingKeyRequest request)

Creates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       CreateCustomTargetingKeyRequest request =
           CreateCustomTargetingKeyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomTargetingKey(CustomTargetingKey.newBuilder().build())
               .build();
       CustomTargetingKey response =
           customTargetingKeyServiceClient.createCustomTargetingKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### createCustomTargetingKey(String parent, CustomTargetingKey customTargetingKey)
    
    
    public final CustomTargetingKey createCustomTargetingKey(String parent, CustomTargetingKey customTargetingKey)

Creates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CustomTargetingKey customTargetingKey = CustomTargetingKey.newBuilder().build();
       CustomTargetingKey response =
           customTargetingKeyServiceClient.createCustomTargetingKey(parent, customTargetingKey);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `CustomTargetingKey` will be created. Format: `networks/{network_code}`  
`customTargetingKey` | `[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)`  
Required. The `CustomTargetingKey` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### createCustomTargetingKeyCallable()
    
    
    public final UnaryCallable<CreateCustomTargetingKeyRequest,CustomTargetingKey> createCustomTargetingKeyCallable()

Creates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       CreateCustomTargetingKeyRequest request =
           CreateCustomTargetingKeyRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomTargetingKey(CustomTargetingKey.newBuilder().build())
               .build();
       ApiFuture<CustomTargetingKey> future =
           customTargetingKeyServiceClient.createCustomTargetingKeyCallable().futureCall(request);
       // Do something.
       CustomTargetingKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingKeyRequest),[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)>` |   
  
### getCustomTargetingKey(@Nullable CustomTargetingKeyName name)
    
    
    public final CustomTargetingKey getCustomTargetingKey(@Nullable CustomTargetingKeyName name)

Retrieves a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       CustomTargetingKeyName name =
           CustomTargetingKeyName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_KEY]");
       CustomTargetingKey response = customTargetingKeyServiceClient.getCustomTargetingKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomTargetingKeyName`  
Required. The resource name of the CustomTargetingKey. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### getCustomTargetingKey(GetCustomTargetingKeyRequest request)
    
    
    public final CustomTargetingKey getCustomTargetingKey(GetCustomTargetingKeyRequest request)

Retrieves a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       GetCustomTargetingKeyRequest request =
           GetCustomTargetingKeyRequest.newBuilder()
               .setName(
                   CustomTargetingKeyName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_KEY]").toString())
               .build();
       CustomTargetingKey response = customTargetingKeyServiceClient.getCustomTargetingKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomTargetingKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### getCustomTargetingKey(String name)
    
    
    public final CustomTargetingKey getCustomTargetingKey(String name)

Retrieves a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String name =
           CustomTargetingKeyName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_KEY]").toString();
       CustomTargetingKey response = customTargetingKeyServiceClient.getCustomTargetingKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CustomTargetingKey. Format: `networks/{network_code}/customTargetingKeys/{custom_targeting_key_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### getCustomTargetingKeyCallable()
    
    
    public final UnaryCallable<GetCustomTargetingKeyRequest,CustomTargetingKey> getCustomTargetingKeyCallable()

Retrieves a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       GetCustomTargetingKeyRequest request =
           GetCustomTargetingKeyRequest.newBuilder()
               .setName(
                   CustomTargetingKeyName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_KEY]").toString())
               .build();
       ApiFuture<CustomTargetingKey> future =
           customTargetingKeyServiceClient.getCustomTargetingKeyCallable().futureCall(request);
       // Do something.
       CustomTargetingKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomTargetingKeyRequest),[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)>` |   
  
### getSettings()
    
    
    public final @Nullable CustomTargetingKeyServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomTargetingKeyServiceSettings` |   
  
### getStub()
    
    
    public CustomTargetingKeyServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingKeyServiceStub)` |   
  
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
  
### listCustomTargetingKeys(@Nullable NetworkName parent)
    
    
    public final CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse listCustomTargetingKeys(@Nullable NetworkName parent)

Lists `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CustomTargetingKey element :
           customTargetingKeyServiceClient.listCustomTargetingKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse)` |   
  
### listCustomTargetingKeys(ListCustomTargetingKeysRequest request)
    
    
    public final CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse listCustomTargetingKeys(ListCustomTargetingKeysRequest request)

Lists `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       ListCustomTargetingKeysRequest request =
           ListCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CustomTargetingKey element :
           customTargetingKeyServiceClient.listCustomTargetingKeys(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse)` |   
  
### listCustomTargetingKeys(String parent)
    
    
    public final CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse listCustomTargetingKeys(String parent)

Lists `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CustomTargetingKey element :
           customTargetingKeyServiceClient.listCustomTargetingKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingKeys. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse)` |   
  
### listCustomTargetingKeysCallable()
    
    
    public final UnaryCallable<ListCustomTargetingKeysRequest,ListCustomTargetingKeysResponse> listCustomTargetingKeysCallable()

Lists `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       ListCustomTargetingKeysRequest request =
           ListCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCustomTargetingKeysResponse response =
             customTargetingKeyServiceClient.listCustomTargetingKeysCallable().call(request);
         for (CustomTargetingKey element : response.getCustomTargetingKeysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysRequest),[ListCustomTargetingKeysResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysResponse)>` |   
  
### listCustomTargetingKeysPagedCallable()
    
    
    public final UnaryCallable<ListCustomTargetingKeysRequest,CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse> listCustomTargetingKeysPagedCallable()

Lists `CustomTargetingKey` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       ListCustomTargetingKeysRequest request =
           ListCustomTargetingKeysRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CustomTargetingKey> future =
           customTargetingKeyServiceClient
               .listCustomTargetingKeysPagedCallable()
               .futureCall(request);
       // Do something.
       for (CustomTargetingKey element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomTargetingKeysRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysRequest),[ListCustomTargetingKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyServiceClient.ListCustomTargetingKeysPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCustomTargetingKey(CustomTargetingKey customTargetingKey, FieldMask updateMask)
    
    
    public final CustomTargetingKey updateCustomTargetingKey(CustomTargetingKey customTargetingKey, FieldMask updateMask)

Updates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       CustomTargetingKey customTargetingKey = CustomTargetingKey.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CustomTargetingKey response =
           customTargetingKeyServiceClient.updateCustomTargetingKey(customTargetingKey, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`customTargetingKey` | `[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)`  
Required. The `CustomTargetingKey` to update. The `CustomTargetingKey`'s `name` is used to identify the `CustomTargetingKey` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### updateCustomTargetingKey(UpdateCustomTargetingKeyRequest request)
    
    
    public final CustomTargetingKey updateCustomTargetingKey(UpdateCustomTargetingKeyRequest request)

Updates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       UpdateCustomTargetingKeyRequest request =
           UpdateCustomTargetingKeyRequest.newBuilder()
               .setCustomTargetingKey(CustomTargetingKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CustomTargetingKey response =
           customTargetingKeyServiceClient.updateCustomTargetingKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### updateCustomTargetingKeyCallable()
    
    
    public final UnaryCallable<UpdateCustomTargetingKeyRequest,CustomTargetingKey> updateCustomTargetingKeyCallable()

Updates a `CustomTargetingKey` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingKeyServiceClient customTargetingKeyServiceClient =
         CustomTargetingKeyServiceClient.create()) {
       UpdateCustomTargetingKeyRequest request =
           UpdateCustomTargetingKeyRequest.newBuilder()
               .setCustomTargetingKey(CustomTargetingKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CustomTargetingKey> future =
           customTargetingKeyServiceClient.updateCustomTargetingKeyCallable().futureCall(request);
       // Do something.
       CustomTargetingKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomTargetingKeyRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingKeyRequest),[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
