---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient
title: Class CustomTargetingValueServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:41.798461+00:00
---

# Class CustomTargetingValueServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CustomTargetingValueServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/CustomTargetingValueServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `CustomTargetingValue` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       CustomTargetingValueName name =
           CustomTargetingValueName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_VALUE]");
       CustomTargetingValue response =
           customTargetingValueServiceClient.getCustomTargetingValue(name);
     }
     

Note: close() needs to be called on the CustomTargetingValueServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetCustomTargetingValue |  Retrieves a `CustomTargetingValue` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomTargetingValue(GetCustomTargetingValueRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomTargetingValue(CustomTargetingValueName name) 
  * getCustomTargetingValue(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomTargetingValueCallable() 

  
ListCustomTargetingValues |  Lists `CustomTargetingValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomTargetingValues(ListCustomTargetingValuesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomTargetingValues(NetworkName parent) 
  * listCustomTargetingValues(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomTargetingValuesPagedCallable() 
  * listCustomTargetingValuesCallable() 

  
CreateCustomTargetingValue |  Creates a `CustomTargetingValue` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomTargetingValue(CreateCustomTargetingValueRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomTargetingValue(NetworkName parent, CustomTargetingValue customTargetingValue) 
  * createCustomTargetingValue(String parent, CustomTargetingValue customTargetingValue) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomTargetingValueCallable() 

  
BatchCreateCustomTargetingValues |  Creates `CustomTargetingValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateCustomTargetingValues(NetworkName parent, List<CreateCustomTargetingValueRequest> requests) 
  * batchCreateCustomTargetingValues(String parent, List<CreateCustomTargetingValueRequest> requests) 
  * batchCreateCustomTargetingValues(BatchCreateCustomTargetingValuesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateCustomTargetingValuesCallable() 

  
UpdateCustomTargetingValue |  Updates a `CustomTargetingValue` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCustomTargetingValue(UpdateCustomTargetingValueRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateCustomTargetingValue(CustomTargetingValue customTargetingValue, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCustomTargetingValueCallable() 

  
BatchUpdateCustomTargetingValues |  Batch updates `CustomTargetingValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateCustomTargetingValues(NetworkName parent, List<UpdateCustomTargetingValueRequest> requests) 
  * batchUpdateCustomTargetingValues(String parent, List<UpdateCustomTargetingValueRequest> requests) 
  * batchUpdateCustomTargetingValues(BatchUpdateCustomTargetingValuesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateCustomTargetingValuesCallable() 

  
BatchActivateCustomTargetingValues |  Batch activates `CustomTargetingValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateCustomTargetingValues(NetworkName parent, List<ActivateCustomTargetingValueRequest> requests) 
  * batchActivateCustomTargetingValues(String parent, List<ActivateCustomTargetingValueRequest> requests) 
  * batchActivateCustomTargetingValues(BatchActivateCustomTargetingValuesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateCustomTargetingValuesCallable() 

  
BatchDeactivateCustomTargetingValues |  Deactivates a list of `CustomTargetingValue` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateCustomTargetingValues(NetworkName parent, List<DeactivateCustomTargetingValueRequest> requests) 
  * batchDeactivateCustomTargetingValues(String parent, List<DeactivateCustomTargetingValueRequest> requests) 
  * batchDeactivateCustomTargetingValues(BatchDeactivateCustomTargetingValuesRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateCustomTargetingValuesCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CustomTargetingValueServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomTargetingValueServiceSettings customTargetingValueServiceSettings =
         CustomTargetingValueServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create(customTargetingValueServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CustomTargetingValueServiceSettings customTargetingValueServiceSettings =
         CustomTargetingValueServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create(customTargetingValueServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CustomTargetingValueServiceClient

## Static Methods 

### create()
    
    
    public static final CustomTargetingValueServiceClient create()

Constructs an instance of CustomTargetingValueServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomTargetingValueServiceSettings settings)
    
    
    public static final CustomTargetingValueServiceClient create(CustomTargetingValueServiceSettings settings)

Constructs an instance of CustomTargetingValueServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomTargetingValueServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CustomTargetingValueServiceStub stub)
    
    
    public static final CustomTargetingValueServiceClient create(CustomTargetingValueServiceStub stub)

Constructs an instance of CustomTargetingValueServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(CustomTargetingValueServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomTargetingValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingValueServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient)` |   
  
## Constructors 

### CustomTargetingValueServiceClient(CustomTargetingValueServiceSettings settings)
    
    
    protected CustomTargetingValueServiceClient(CustomTargetingValueServiceSettings settings)

Constructs an instance of CustomTargetingValueServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CustomTargetingValueServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceSettings)`  
  
  
### CustomTargetingValueServiceClient(CustomTargetingValueServiceStub stub)
    
    
    protected CustomTargetingValueServiceClient(CustomTargetingValueServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CustomTargetingValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingValueServiceStub)`  
  
  
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
  
### batchActivateCustomTargetingValues(@Nullable NetworkName parent, List<ActivateCustomTargetingValueRequest> requests)
    
    
    public final BatchActivateCustomTargetingValuesResponse batchActivateCustomTargetingValues(@Nullable NetworkName parent, List<ActivateCustomTargetingValueRequest> requests)

Batch activates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<ActivateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchActivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchActivateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ActivateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ActivateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to activate. A maximum of 100 objects can be activated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesResponse)` |   
  
### batchActivateCustomTargetingValues(BatchActivateCustomTargetingValuesRequest request)
    
    
    public final BatchActivateCustomTargetingValuesResponse batchActivateCustomTargetingValues(BatchActivateCustomTargetingValuesRequest request)

Batch activates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchActivateCustomTargetingValuesRequest request =
           BatchActivateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ActivateCustomTargetingValueRequest>())
               .build();
       BatchActivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchActivateCustomTargetingValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesResponse)` |   
  
### batchActivateCustomTargetingValues(String parent, List<ActivateCustomTargetingValueRequest> requests)
    
    
    public final BatchActivateCustomTargetingValuesResponse batchActivateCustomTargetingValues(String parent, List<ActivateCustomTargetingValueRequest> requests)

Batch activates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<ActivateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchActivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchActivateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ActivateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ActivateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to activate. A maximum of 100 objects can be activated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesResponse)` |   
  
### batchActivateCustomTargetingValuesCallable()
    
    
    public final UnaryCallable<BatchActivateCustomTargetingValuesRequest,BatchActivateCustomTargetingValuesResponse> batchActivateCustomTargetingValuesCallable()

Batch activates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchActivateCustomTargetingValuesRequest request =
           BatchActivateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<ActivateCustomTargetingValueRequest>())
               .build();
       ApiFuture<BatchActivateCustomTargetingValuesResponse> future =
           customTargetingValueServiceClient
               .batchActivateCustomTargetingValuesCallable()
               .futureCall(request);
       // Do something.
       BatchActivateCustomTargetingValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesRequest),[BatchActivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateCustomTargetingValuesResponse)>` |   
  
### batchCreateCustomTargetingValues(@Nullable NetworkName parent, List<CreateCustomTargetingValueRequest> requests)
    
    
    public final BatchCreateCustomTargetingValuesResponse batchCreateCustomTargetingValues(@Nullable NetworkName parent, List<CreateCustomTargetingValueRequest> requests)

Creates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchCreateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchCreateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesResponse)` |   
  
### batchCreateCustomTargetingValues(BatchCreateCustomTargetingValuesRequest request)
    
    
    public final BatchCreateCustomTargetingValuesResponse batchCreateCustomTargetingValues(BatchCreateCustomTargetingValuesRequest request)

Creates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchCreateCustomTargetingValuesRequest request =
           BatchCreateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomTargetingValueRequest>())
               .build();
       BatchCreateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchCreateCustomTargetingValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesResponse)` |   
  
### batchCreateCustomTargetingValues(String parent, List<CreateCustomTargetingValueRequest> requests)
    
    
    public final BatchCreateCustomTargetingValuesResponse batchCreateCustomTargetingValues(String parent, List<CreateCustomTargetingValueRequest> requests)

Creates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchCreateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchCreateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesResponse)` |   
  
### batchCreateCustomTargetingValuesCallable()
    
    
    public final UnaryCallable<BatchCreateCustomTargetingValuesRequest,BatchCreateCustomTargetingValuesResponse> batchCreateCustomTargetingValuesCallable()

Creates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchCreateCustomTargetingValuesRequest request =
           BatchCreateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateCustomTargetingValueRequest>())
               .build();
       ApiFuture<BatchCreateCustomTargetingValuesResponse> future =
           customTargetingValueServiceClient
               .batchCreateCustomTargetingValuesCallable()
               .futureCall(request);
       // Do something.
       BatchCreateCustomTargetingValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesRequest),[BatchCreateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateCustomTargetingValuesResponse)>` |   
  
### batchDeactivateCustomTargetingValues(@Nullable NetworkName parent, List<DeactivateCustomTargetingValueRequest> requests)
    
    
    public final BatchDeactivateCustomTargetingValuesResponse batchDeactivateCustomTargetingValues(@Nullable NetworkName parent, List<DeactivateCustomTargetingValueRequest> requests)

Deactivates a list of `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<DeactivateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchDeactivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchDeactivateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}/`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeactivateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeactivateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesResponse)` |   
  
### batchDeactivateCustomTargetingValues(BatchDeactivateCustomTargetingValuesRequest request)
    
    
    public final BatchDeactivateCustomTargetingValuesResponse batchDeactivateCustomTargetingValues(BatchDeactivateCustomTargetingValuesRequest request)

Deactivates a list of `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchDeactivateCustomTargetingValuesRequest request =
           BatchDeactivateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<DeactivateCustomTargetingValueRequest>())
               .build();
       BatchDeactivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchDeactivateCustomTargetingValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesResponse)` |   
  
### batchDeactivateCustomTargetingValues(String parent, List<DeactivateCustomTargetingValueRequest> requests)
    
    
    public final BatchDeactivateCustomTargetingValuesResponse batchDeactivateCustomTargetingValues(String parent, List<DeactivateCustomTargetingValueRequest> requests)

Deactivates a list of `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<DeactivateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchDeactivateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchDeactivateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}/`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeactivateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeactivateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesResponse)` |   
  
### batchDeactivateCustomTargetingValuesCallable()
    
    
    public final UnaryCallable<BatchDeactivateCustomTargetingValuesRequest,BatchDeactivateCustomTargetingValuesResponse> batchDeactivateCustomTargetingValuesCallable()

Deactivates a list of `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchDeactivateCustomTargetingValuesRequest request =
           BatchDeactivateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<DeactivateCustomTargetingValueRequest>())
               .build();
       ApiFuture<BatchDeactivateCustomTargetingValuesResponse> future =
           customTargetingValueServiceClient
               .batchDeactivateCustomTargetingValuesCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateCustomTargetingValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesRequest),[BatchDeactivateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateCustomTargetingValuesResponse)>` |   
  
### batchUpdateCustomTargetingValues(@Nullable NetworkName parent, List<UpdateCustomTargetingValueRequest> requests)
    
    
    public final BatchUpdateCustomTargetingValuesResponse batchUpdateCustomTargetingValues(@Nullable NetworkName parent, List<UpdateCustomTargetingValueRequest> requests)

Batch updates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchUpdateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchUpdateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesResponse)` |   
  
### batchUpdateCustomTargetingValues(BatchUpdateCustomTargetingValuesRequest request)
    
    
    public final BatchUpdateCustomTargetingValuesResponse batchUpdateCustomTargetingValues(BatchUpdateCustomTargetingValuesRequest request)

Batch updates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchUpdateCustomTargetingValuesRequest request =
           BatchUpdateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomTargetingValueRequest>())
               .build();
       BatchUpdateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchUpdateCustomTargetingValues(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesResponse)` |   
  
### batchUpdateCustomTargetingValues(String parent, List<UpdateCustomTargetingValueRequest> requests)
    
    
    public final BatchUpdateCustomTargetingValuesResponse batchUpdateCustomTargetingValues(String parent, List<UpdateCustomTargetingValueRequest> requests)

Batch updates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateCustomTargetingValueRequest> requests = new ArrayList<>();
       BatchUpdateCustomTargetingValuesResponse response =
           customTargetingValueServiceClient.batchUpdateCustomTargetingValues(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingValueRequest)>`  
Required. The `CustomTargetingValue` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesResponse)` |   
  
### batchUpdateCustomTargetingValuesCallable()
    
    
    public final UnaryCallable<BatchUpdateCustomTargetingValuesRequest,BatchUpdateCustomTargetingValuesResponse> batchUpdateCustomTargetingValuesCallable()

Batch updates `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       BatchUpdateCustomTargetingValuesRequest request =
           BatchUpdateCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateCustomTargetingValueRequest>())
               .build();
       ApiFuture<BatchUpdateCustomTargetingValuesResponse> future =
           customTargetingValueServiceClient
               .batchUpdateCustomTargetingValuesCallable()
               .futureCall(request);
       // Do something.
       BatchUpdateCustomTargetingValuesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesRequest),[BatchUpdateCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateCustomTargetingValuesResponse)>` |   
  
### close()
    
    
    public final void close()

### createCustomTargetingValue(@Nullable NetworkName parent, CustomTargetingValue customTargetingValue)
    
    
    public final CustomTargetingValue createCustomTargetingValue(@Nullable NetworkName parent, CustomTargetingValue customTargetingValue)

Creates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       CustomTargetingValue customTargetingValue = CustomTargetingValue.newBuilder().build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.createCustomTargetingValue(
               parent, customTargetingValue);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`customTargetingValue` | `[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)`  
Required. The `CustomTargetingValue` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### createCustomTargetingValue(CreateCustomTargetingValueRequest request)
    
    
    public final CustomTargetingValue createCustomTargetingValue(CreateCustomTargetingValueRequest request)

Creates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       CreateCustomTargetingValueRequest request =
           CreateCustomTargetingValueRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomTargetingValue(CustomTargetingValue.newBuilder().build())
               .build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.createCustomTargetingValue(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingValueRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### createCustomTargetingValue(String parent, CustomTargetingValue customTargetingValue)
    
    
    public final CustomTargetingValue createCustomTargetingValue(String parent, CustomTargetingValue customTargetingValue)

Creates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       CustomTargetingValue customTargetingValue = CustomTargetingValue.newBuilder().build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.createCustomTargetingValue(
               parent, customTargetingValue);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
`customTargetingValue` | `[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)`  
Required. The `CustomTargetingValue` to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### createCustomTargetingValueCallable()
    
    
    public final UnaryCallable<CreateCustomTargetingValueRequest,CustomTargetingValue> createCustomTargetingValueCallable()

Creates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       CreateCustomTargetingValueRequest request =
           CreateCustomTargetingValueRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setCustomTargetingValue(CustomTargetingValue.newBuilder().build())
               .build();
       ApiFuture<CustomTargetingValue> future =
           customTargetingValueServiceClient
               .createCustomTargetingValueCallable()
               .futureCall(request);
       // Do something.
       CustomTargetingValue response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateCustomTargetingValueRequest),[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)>` |   
  
### getCustomTargetingValue(@Nullable CustomTargetingValueName name)
    
    
    public final CustomTargetingValue getCustomTargetingValue(@Nullable CustomTargetingValueName name)

Retrieves a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       CustomTargetingValueName name =
           CustomTargetingValueName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_VALUE]");
       CustomTargetingValue response =
           customTargetingValueServiceClient.getCustomTargetingValue(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomTargetingValueName`  
Required. The resource name of the CustomTargetingValue. Format: `networks/{network_code}/customTargetingValues/{custom_targeting_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### getCustomTargetingValue(GetCustomTargetingValueRequest request)
    
    
    public final CustomTargetingValue getCustomTargetingValue(GetCustomTargetingValueRequest request)

Retrieves a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       GetCustomTargetingValueRequest request =
           GetCustomTargetingValueRequest.newBuilder()
               .setName(
                   CustomTargetingValueName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_VALUE]")
                       .toString())
               .build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.getCustomTargetingValue(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomTargetingValueRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### getCustomTargetingValue(String name)
    
    
    public final CustomTargetingValue getCustomTargetingValue(String name)

Retrieves a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String name =
           CustomTargetingValueName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_VALUE]").toString();
       CustomTargetingValue response =
           customTargetingValueServiceClient.getCustomTargetingValue(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the CustomTargetingValue. Format: `networks/{network_code}/customTargetingValues/{custom_targeting_value_id}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### getCustomTargetingValueCallable()
    
    
    public final UnaryCallable<GetCustomTargetingValueRequest,CustomTargetingValue> getCustomTargetingValueCallable()

Retrieves a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       GetCustomTargetingValueRequest request =
           GetCustomTargetingValueRequest.newBuilder()
               .setName(
                   CustomTargetingValueName.of("[NETWORK_CODE]", "[CUSTOM_TARGETING_VALUE]")
                       .toString())
               .build();
       ApiFuture<CustomTargetingValue> future =
           customTargetingValueServiceClient.getCustomTargetingValueCallable().futureCall(request);
       // Do something.
       CustomTargetingValue response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetCustomTargetingValueRequest),[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)>` |   
  
### getSettings()
    
    
    public final @Nullable CustomTargetingValueServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.CustomTargetingValueServiceSettings` |   
  
### getStub()
    
    
    public CustomTargetingValueServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.CustomTargetingValueServiceStub)` |   
  
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
  
### listCustomTargetingValues(@Nullable NetworkName parent)
    
    
    public final CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse listCustomTargetingValues(@Nullable NetworkName parent)

Lists `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (CustomTargetingValue element :
           customTargetingValueServiceClient.listCustomTargetingValues(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse)` |   
  
### listCustomTargetingValues(ListCustomTargetingValuesRequest request)
    
    
    public final CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse listCustomTargetingValues(ListCustomTargetingValuesRequest request)

Lists `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       ListCustomTargetingValuesRequest request =
           ListCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (CustomTargetingValue element :
           customTargetingValueServiceClient.listCustomTargetingValues(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingValuesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse)` |   
  
### listCustomTargetingValues(String parent)
    
    
    public final CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse listCustomTargetingValues(String parent)

Lists `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (CustomTargetingValue element :
           customTargetingValueServiceClient.listCustomTargetingValues(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of CustomTargetingValues. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse)` |   
  
### listCustomTargetingValuesCallable()
    
    
    public final UnaryCallable<ListCustomTargetingValuesRequest,ListCustomTargetingValuesResponse> listCustomTargetingValuesCallable()

Lists `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       ListCustomTargetingValuesRequest request =
           ListCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListCustomTargetingValuesResponse response =
             customTargetingValueServiceClient.listCustomTargetingValuesCallable().call(request);
         for (CustomTargetingValue element : response.getCustomTargetingValuesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingValuesRequest),[ListCustomTargetingValuesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingValuesResponse)>` |   
  
### listCustomTargetingValuesPagedCallable()
    
    
    public final UnaryCallable<ListCustomTargetingValuesRequest,CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse> listCustomTargetingValuesPagedCallable()

Lists `CustomTargetingValue` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       ListCustomTargetingValuesRequest request =
           ListCustomTargetingValuesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<CustomTargetingValue> future =
           customTargetingValueServiceClient
               .listCustomTargetingValuesPagedCallable()
               .futureCall(request);
       // Do something.
       for (CustomTargetingValue element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomTargetingValuesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingValuesRequest),[ListCustomTargetingValuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValueServiceClient.ListCustomTargetingValuesPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCustomTargetingValue(CustomTargetingValue customTargetingValue, FieldMask updateMask)
    
    
    public final CustomTargetingValue updateCustomTargetingValue(CustomTargetingValue customTargetingValue, FieldMask updateMask)

Updates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       CustomTargetingValue customTargetingValue = CustomTargetingValue.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.updateCustomTargetingValue(
               customTargetingValue, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`customTargetingValue` | `[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)`  
Required. The `CustomTargetingValue` to update. The `CustomTargetingValue`'s `name` is used to identify the `CustomTargetingValue` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### updateCustomTargetingValue(UpdateCustomTargetingValueRequest request)
    
    
    public final CustomTargetingValue updateCustomTargetingValue(UpdateCustomTargetingValueRequest request)

Updates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       UpdateCustomTargetingValueRequest request =
           UpdateCustomTargetingValueRequest.newBuilder()
               .setCustomTargetingValue(CustomTargetingValue.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CustomTargetingValue response =
           customTargetingValueServiceClient.updateCustomTargetingValue(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingValueRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)` |   
  
### updateCustomTargetingValueCallable()
    
    
    public final UnaryCallable<UpdateCustomTargetingValueRequest,CustomTargetingValue> updateCustomTargetingValueCallable()

Updates a `CustomTargetingValue` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CustomTargetingValueServiceClient customTargetingValueServiceClient =
         CustomTargetingValueServiceClient.create()) {
       UpdateCustomTargetingValueRequest request =
           UpdateCustomTargetingValueRequest.newBuilder()
               .setCustomTargetingValue(CustomTargetingValue.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<CustomTargetingValue> future =
           customTargetingValueServiceClient
               .updateCustomTargetingValueCallable()
               .futureCall(request);
       // Do something.
       CustomTargetingValue response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCustomTargetingValueRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateCustomTargetingValueRequest),[CustomTargetingValue](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingValue)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
