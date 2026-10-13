---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient
title: Class TargetingPresetServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:09:05.727115+00:00
---

# Class TargetingPresetServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetingPresetServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/TargetingPresetServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `TargetingPreset` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       TargetingPresetName name = TargetingPresetName.of("[NETWORK_CODE]", "[TARGETING_PRESET]");
       TargetingPreset response = targetingPresetServiceClient.getTargetingPreset(name);
     }
     

Note: close() needs to be called on the TargetingPresetServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetTargetingPreset |  Retrieves a `TargetingPreset` object. Note: Deactivated targeting presets are "logically deleted" (filtered out) by the get logic in the manager layer, so they will not be returned by the `GetTargetingPreset` RPC. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTargetingPreset(GetTargetingPresetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTargetingPreset(TargetingPresetName name) 
  * getTargetingPreset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTargetingPresetCallable() 

  
ListTargetingPresets |  Lists `TargetingPreset` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTargetingPresets(ListTargetingPresetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTargetingPresets(NetworkName parent) 
  * listTargetingPresets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTargetingPresetsPagedCallable() 
  * listTargetingPresetsCallable() 

  
CreateTargetingPreset |  Creates a `TargetingPreset` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTargetingPreset(CreateTargetingPresetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTargetingPreset(NetworkName parent, TargetingPreset targetingPreset) 
  * createTargetingPreset(String parent, TargetingPreset targetingPreset) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTargetingPresetCallable() 

  
BatchCreateTargetingPresets |  Creates `TargetingPreset` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateTargetingPresets(NetworkName parent, List<CreateTargetingPresetRequest> requests) 
  * batchCreateTargetingPresets(String parent, List<CreateTargetingPresetRequest> requests) 
  * batchCreateTargetingPresets(BatchCreateTargetingPresetsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateTargetingPresetsCallable() 

  
UpdateTargetingPreset |  Updates a `TargetingPreset` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTargetingPreset(UpdateTargetingPresetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateTargetingPreset(TargetingPreset targetingPreset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTargetingPresetCallable() 

  
BatchUpdateTargetingPresets |  Batch updates `TargetingPreset` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateTargetingPresets(NetworkName parent, List<UpdateTargetingPresetRequest> requests) 
  * batchUpdateTargetingPresets(String parent, List<UpdateTargetingPresetRequest> requests) 
  * batchUpdateTargetingPresets(BatchUpdateTargetingPresetsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateTargetingPresetsCallable() 

  
BatchDeactivateTargetingPresets |  Batch deactivates `TargetingPreset` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateTargetingPresets(NetworkName parent, List<DeactivateTargetingPresetRequest> requests) 
  * batchDeactivateTargetingPresets(String parent, List<DeactivateTargetingPresetRequest> requests) 
  * batchDeactivateTargetingPresets(BatchDeactivateTargetingPresetsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateTargetingPresetsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetingPresetServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetingPresetServiceSettings targetingPresetServiceSettings =
         TargetingPresetServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create(targetingPresetServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetingPresetServiceSettings targetingPresetServiceSettings =
         TargetingPresetServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create(targetingPresetServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetingPresetServiceClient

## Static Methods 

### create()
    
    
    public static final TargetingPresetServiceClient create()

Constructs an instance of TargetingPresetServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetingPresetServiceSettings settings)
    
    
    public static final TargetingPresetServiceClient create(TargetingPresetServiceSettings settings)

Constructs an instance of TargetingPresetServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetingPresetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetingPresetServiceStub stub)
    
    
    public static final TargetingPresetServiceClient create(TargetingPresetServiceStub stub)

Constructs an instance of TargetingPresetServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetingPresetServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetingPresetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TargetingPresetServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient)` |   
  
## Constructors 

### TargetingPresetServiceClient(TargetingPresetServiceSettings settings)
    
    
    protected TargetingPresetServiceClient(TargetingPresetServiceSettings settings)

Constructs an instance of TargetingPresetServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetingPresetServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceSettings)`  
  
  
### TargetingPresetServiceClient(TargetingPresetServiceStub stub)
    
    
    protected TargetingPresetServiceClient(TargetingPresetServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetingPresetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TargetingPresetServiceStub)`  
  
  
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
  
### batchCreateTargetingPresets(@Nullable NetworkName parent, List<CreateTargetingPresetRequest> requests)
    
    
    public final BatchCreateTargetingPresetsResponse batchCreateTargetingPresets(@Nullable NetworkName parent, List<CreateTargetingPresetRequest> requests)

Creates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateTargetingPresetRequest> requests = new ArrayList<>();
       BatchCreateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchCreateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `TargetingPresets` will be created. Format: `networks/{network_code}` The parent field in the CreateTargetingPresetRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsResponse)` |   
  
### batchCreateTargetingPresets(BatchCreateTargetingPresetsRequest request)
    
    
    public final BatchCreateTargetingPresetsResponse batchCreateTargetingPresets(BatchCreateTargetingPresetsRequest request)

Creates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchCreateTargetingPresetsRequest request =
           BatchCreateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateTargetingPresetRequest>())
               .build();
       BatchCreateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchCreateTargetingPresets(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsResponse)` |   
  
### batchCreateTargetingPresets(String parent, List<CreateTargetingPresetRequest> requests)
    
    
    public final BatchCreateTargetingPresetsResponse batchCreateTargetingPresets(String parent, List<CreateTargetingPresetRequest> requests)

Creates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateTargetingPresetRequest> requests = new ArrayList<>();
       BatchCreateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchCreateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `TargetingPresets` will be created. Format: `networks/{network_code}` The parent field in the CreateTargetingPresetRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsResponse)` |   
  
### batchCreateTargetingPresetsCallable()
    
    
    public final UnaryCallable<BatchCreateTargetingPresetsRequest,BatchCreateTargetingPresetsResponse> batchCreateTargetingPresetsCallable()

Creates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchCreateTargetingPresetsRequest request =
           BatchCreateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateTargetingPresetRequest>())
               .build();
       ApiFuture<BatchCreateTargetingPresetsResponse> future =
           targetingPresetServiceClient.batchCreateTargetingPresetsCallable().futureCall(request);
       // Do something.
       BatchCreateTargetingPresetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsRequest),[BatchCreateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateTargetingPresetsResponse)>` |   
  
### batchDeactivateTargetingPresets(@Nullable NetworkName parent, List<DeactivateTargetingPresetRequest> requests)
    
    
    public final BatchDeactivateTargetingPresetsResponse batchDeactivateTargetingPresets(@Nullable NetworkName parent, List<DeactivateTargetingPresetRequest> requests)

Batch deactivates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<DeactivateTargetingPresetRequest> requests = new ArrayList<>();
       BatchDeactivateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchDeactivateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeactivateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeactivateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsResponse)` |   
  
### batchDeactivateTargetingPresets(BatchDeactivateTargetingPresetsRequest request)
    
    
    public final BatchDeactivateTargetingPresetsResponse batchDeactivateTargetingPresets(BatchDeactivateTargetingPresetsRequest request)

Batch deactivates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchDeactivateTargetingPresetsRequest request =
           BatchDeactivateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<DeactivateTargetingPresetRequest>())
               .build();
       BatchDeactivateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchDeactivateTargetingPresets(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsResponse)` |   
  
### batchDeactivateTargetingPresets(String parent, List<DeactivateTargetingPresetRequest> requests)
    
    
    public final BatchDeactivateTargetingPresetsResponse batchDeactivateTargetingPresets(String parent, List<DeactivateTargetingPresetRequest> requests)

Batch deactivates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<DeactivateTargetingPresetRequest> requests = new ArrayList<>();
       BatchDeactivateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchDeactivateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeactivateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeactivateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to deactivate.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsResponse)` |   
  
### batchDeactivateTargetingPresetsCallable()
    
    
    public final UnaryCallable<BatchDeactivateTargetingPresetsRequest,BatchDeactivateTargetingPresetsResponse> batchDeactivateTargetingPresetsCallable()

Batch deactivates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchDeactivateTargetingPresetsRequest request =
           BatchDeactivateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<DeactivateTargetingPresetRequest>())
               .build();
       ApiFuture<BatchDeactivateTargetingPresetsResponse> future =
           targetingPresetServiceClient
               .batchDeactivateTargetingPresetsCallable()
               .futureCall(request);
       // Do something.
       BatchDeactivateTargetingPresetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsRequest),[BatchDeactivateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateTargetingPresetsResponse)>` |   
  
### batchUpdateTargetingPresets(@Nullable NetworkName parent, List<UpdateTargetingPresetRequest> requests)
    
    
    public final BatchUpdateTargetingPresetsResponse batchUpdateTargetingPresets(@Nullable NetworkName parent, List<UpdateTargetingPresetRequest> requests)

Batch updates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateTargetingPresetRequest> requests = new ArrayList<>();
       BatchUpdateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchUpdateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `TargetingPresets` will be updated. Format: `networks/{network_code}` The parent field in the UpdateTargetingPresetRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsResponse)` |   
  
### batchUpdateTargetingPresets(BatchUpdateTargetingPresetsRequest request)
    
    
    public final BatchUpdateTargetingPresetsResponse batchUpdateTargetingPresets(BatchUpdateTargetingPresetsRequest request)

Batch updates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchUpdateTargetingPresetsRequest request =
           BatchUpdateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateTargetingPresetRequest>())
               .build();
       BatchUpdateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchUpdateTargetingPresets(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsResponse)` |   
  
### batchUpdateTargetingPresets(String parent, List<UpdateTargetingPresetRequest> requests)
    
    
    public final BatchUpdateTargetingPresetsResponse batchUpdateTargetingPresets(String parent, List<UpdateTargetingPresetRequest> requests)

Batch updates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateTargetingPresetRequest> requests = new ArrayList<>();
       BatchUpdateTargetingPresetsResponse response =
           targetingPresetServiceClient.batchUpdateTargetingPresets(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `TargetingPresets` will be updated. Format: `networks/{network_code}` The parent field in the UpdateTargetingPresetRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTargetingPresetRequest)>`  
Required. The `TargetingPreset` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsResponse)` |   
  
### batchUpdateTargetingPresetsCallable()
    
    
    public final UnaryCallable<BatchUpdateTargetingPresetsRequest,BatchUpdateTargetingPresetsResponse> batchUpdateTargetingPresetsCallable()

Batch updates `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       BatchUpdateTargetingPresetsRequest request =
           BatchUpdateTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateTargetingPresetRequest>())
               .build();
       ApiFuture<BatchUpdateTargetingPresetsResponse> future =
           targetingPresetServiceClient.batchUpdateTargetingPresetsCallable().futureCall(request);
       // Do something.
       BatchUpdateTargetingPresetsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsRequest),[BatchUpdateTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateTargetingPresetsResponse)>` |   
  
### close()
    
    
    public final void close()

### createTargetingPreset(@Nullable NetworkName parent, TargetingPreset targetingPreset)
    
    
    public final TargetingPreset createTargetingPreset(@Nullable NetworkName parent, TargetingPreset targetingPreset)

Creates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       TargetingPreset targetingPreset = TargetingPreset.newBuilder().build();
       TargetingPreset response =
           targetingPresetServiceClient.createTargetingPreset(parent, targetingPreset);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `TargetingPreset` will be created. Format: `networks/{network_code}`  
`targetingPreset` | `[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)`  
Required. The `TargetingPreset` to create.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### createTargetingPreset(CreateTargetingPresetRequest request)
    
    
    public final TargetingPreset createTargetingPreset(CreateTargetingPresetRequest request)

Creates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       CreateTargetingPresetRequest request =
           CreateTargetingPresetRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setTargetingPreset(TargetingPreset.newBuilder().build())
               .build();
       TargetingPreset response = targetingPresetServiceClient.createTargetingPreset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTargetingPresetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### createTargetingPreset(String parent, TargetingPreset targetingPreset)
    
    
    public final TargetingPreset createTargetingPreset(String parent, TargetingPreset targetingPreset)

Creates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       TargetingPreset targetingPreset = TargetingPreset.newBuilder().build();
       TargetingPreset response =
           targetingPresetServiceClient.createTargetingPreset(parent, targetingPreset);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `TargetingPreset` will be created. Format: `networks/{network_code}`  
`targetingPreset` | `[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)`  
Required. The `TargetingPreset` to create.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### createTargetingPresetCallable()
    
    
    public final UnaryCallable<CreateTargetingPresetRequest,TargetingPreset> createTargetingPresetCallable()

Creates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       CreateTargetingPresetRequest request =
           CreateTargetingPresetRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setTargetingPreset(TargetingPreset.newBuilder().build())
               .build();
       ApiFuture<TargetingPreset> future =
           targetingPresetServiceClient.createTargetingPresetCallable().futureCall(request);
       // Do something.
       TargetingPreset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateTargetingPresetRequest),[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetingPresetServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TargetingPresetServiceSettings` |   
  
### getStub()
    
    
    public TargetingPresetServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.TargetingPresetServiceStub)` |   
  
### getTargetingPreset(@Nullable TargetingPresetName name)
    
    
    public final TargetingPreset getTargetingPreset(@Nullable TargetingPresetName name)

Retrieves a `TargetingPreset` object. Note: Deactivated targeting presets are "logically deleted" (filtered out) by the get logic in the manager layer, so they will not be returned by the `GetTargetingPreset` RPC.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       TargetingPresetName name = TargetingPresetName.of("[NETWORK_CODE]", "[TARGETING_PRESET]");
       TargetingPreset response = targetingPresetServiceClient.getTargetingPreset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.TargetingPresetName`  
Required. The resource name of the TargetingPreset. Format: `networks/{network_code}/targetingPresets/{targeting_preset_id}`  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### getTargetingPreset(GetTargetingPresetRequest request)
    
    
    public final TargetingPreset getTargetingPreset(GetTargetingPresetRequest request)

Retrieves a `TargetingPreset` object. Note: Deactivated targeting presets are "logically deleted" (filtered out) by the get logic in the manager layer, so they will not be returned by the `GetTargetingPreset` RPC.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       GetTargetingPresetRequest request =
           GetTargetingPresetRequest.newBuilder()
               .setName(TargetingPresetName.of("[NETWORK_CODE]", "[TARGETING_PRESET]").toString())
               .build();
       TargetingPreset response = targetingPresetServiceClient.getTargetingPreset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTargetingPresetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### getTargetingPreset(String name)
    
    
    public final TargetingPreset getTargetingPreset(String name)

Retrieves a `TargetingPreset` object. Note: Deactivated targeting presets are "logically deleted" (filtered out) by the get logic in the manager layer, so they will not be returned by the `GetTargetingPreset` RPC.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String name = TargetingPresetName.of("[NETWORK_CODE]", "[TARGETING_PRESET]").toString();
       TargetingPreset response = targetingPresetServiceClient.getTargetingPreset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the TargetingPreset. Format: `networks/{network_code}/targetingPresets/{targeting_preset_id}`  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### getTargetingPresetCallable()
    
    
    public final UnaryCallable<GetTargetingPresetRequest,TargetingPreset> getTargetingPresetCallable()

Retrieves a `TargetingPreset` object. Note: Deactivated targeting presets are "logically deleted" (filtered out) by the get logic in the manager layer, so they will not be returned by the `GetTargetingPreset` RPC.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       GetTargetingPresetRequest request =
           GetTargetingPresetRequest.newBuilder()
               .setName(TargetingPresetName.of("[NETWORK_CODE]", "[TARGETING_PRESET]").toString())
               .build();
       ApiFuture<TargetingPreset> future =
           targetingPresetServiceClient.getTargetingPresetCallable().futureCall(request);
       // Do something.
       TargetingPreset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetTargetingPresetRequest),[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)>` |   
  
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
  
### listTargetingPresets(@Nullable NetworkName parent)
    
    
    public final TargetingPresetServiceClient.ListTargetingPresetsPagedResponse listTargetingPresets(@Nullable NetworkName parent)

Lists `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (TargetingPreset element :
           targetingPresetServiceClient.listTargetingPresets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of TargetingPresets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient.ListTargetingPresetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient.ListTargetingPresetsPagedResponse)` |   
  
### listTargetingPresets(ListTargetingPresetsRequest request)
    
    
    public final TargetingPresetServiceClient.ListTargetingPresetsPagedResponse listTargetingPresets(ListTargetingPresetsRequest request)

Lists `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       ListTargetingPresetsRequest request =
           ListTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (TargetingPreset element :
           targetingPresetServiceClient.listTargetingPresets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTargetingPresetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient.ListTargetingPresetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient.ListTargetingPresetsPagedResponse)` |   
  
### listTargetingPresets(String parent)
    
    
    public final TargetingPresetServiceClient.ListTargetingPresetsPagedResponse listTargetingPresets(String parent)

Lists `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (TargetingPreset element :
           targetingPresetServiceClient.listTargetingPresets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of TargetingPresets. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPresetServiceClient.ListTargetingPresetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient.ListTargetingPresetsPagedResponse)` |   
  
### listTargetingPresetsCallable()
    
    
    public final UnaryCallable<ListTargetingPresetsRequest,ListTargetingPresetsResponse> listTargetingPresetsCallable()

Lists `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       ListTargetingPresetsRequest request =
           ListTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListTargetingPresetsResponse response =
             targetingPresetServiceClient.listTargetingPresetsCallable().call(request);
         for (TargetingPreset element : response.getTargetingPresetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTargetingPresetsRequest),[ListTargetingPresetsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTargetingPresetsResponse)>` |   
  
### listTargetingPresetsPagedCallable()
    
    
    public final UnaryCallable<ListTargetingPresetsRequest,TargetingPresetServiceClient.ListTargetingPresetsPagedResponse> listTargetingPresetsPagedCallable()

Lists `TargetingPreset` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       ListTargetingPresetsRequest request =
           ListTargetingPresetsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<TargetingPreset> future =
           targetingPresetServiceClient.listTargetingPresetsPagedCallable().futureCall(request);
       // Do something.
       for (TargetingPreset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetingPresetsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListTargetingPresetsRequest),[ListTargetingPresetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPresetServiceClient.ListTargetingPresetsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateTargetingPreset(TargetingPreset targetingPreset, FieldMask updateMask)
    
    
    public final TargetingPreset updateTargetingPreset(TargetingPreset targetingPreset, FieldMask updateMask)

Updates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       TargetingPreset targetingPreset = TargetingPreset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       TargetingPreset response =
           targetingPresetServiceClient.updateTargetingPreset(targetingPreset, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`targetingPreset` | `[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)`  
Required. The `TargetingPreset` to update. The `TargetingPreset`'s `name` is used to identify the `TargetingPreset` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### updateTargetingPreset(UpdateTargetingPresetRequest request)
    
    
    public final TargetingPreset updateTargetingPreset(UpdateTargetingPresetRequest request)

Updates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       UpdateTargetingPresetRequest request =
           UpdateTargetingPresetRequest.newBuilder()
               .setTargetingPreset(TargetingPreset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       TargetingPreset response = targetingPresetServiceClient.updateTargetingPreset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTargetingPresetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)` |   
  
### updateTargetingPresetCallable()
    
    
    public final UnaryCallable<UpdateTargetingPresetRequest,TargetingPreset> updateTargetingPresetCallable()

Updates a `TargetingPreset` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetingPresetServiceClient targetingPresetServiceClient =
         TargetingPresetServiceClient.create()) {
       UpdateTargetingPresetRequest request =
           UpdateTargetingPresetRequest.newBuilder()
               .setTargetingPreset(TargetingPreset.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TargetingPreset> future =
           targetingPresetServiceClient.updateTargetingPresetCallable().futureCall(request);
       // Do something.
       TargetingPreset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTargetingPresetRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateTargetingPresetRequest),[TargetingPreset](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.TargetingPreset)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
