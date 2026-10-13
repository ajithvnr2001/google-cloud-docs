---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient
title: Class AdSpotServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:25.767214+00:00
---

# Class AdSpotServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdSpotServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AdSpotServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `AdSpot` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       AdSpotName name = AdSpotName.of("[NETWORK_CODE]", "[AD_SPOT]");
       AdSpot response = adSpotServiceClient.getAdSpot(name);
     }
     

Note: close() needs to be called on the AdSpotServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetAdSpot |  Retrieves an `AdSpot` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAdSpot(GetAdSpotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAdSpot(AdSpotName name) 
  * getAdSpot(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAdSpotCallable() 

  
ListAdSpots |  Lists `AdSpot` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdSpots(ListAdSpotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdSpots(NetworkName parent) 
  * listAdSpots(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdSpotsPagedCallable() 
  * listAdSpotsCallable() 

  
CreateAdSpot |  Creates an `AdSpot` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAdSpot(CreateAdSpotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAdSpot(NetworkName parent, AdSpot adSpot) 
  * createAdSpot(String parent, AdSpot adSpot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAdSpotCallable() 

  
BatchCreateAdSpots |  Batch creates `AdSpot` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateAdSpots(NetworkName parent, List<CreateAdSpotRequest> requests) 
  * batchCreateAdSpots(String parent, List<CreateAdSpotRequest> requests) 
  * batchCreateAdSpots(BatchCreateAdSpotsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateAdSpotsCallable() 

  
UpdateAdSpot |  Updates an `AdSpot` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAdSpot(UpdateAdSpotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAdSpot(AdSpot adSpot, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAdSpotCallable() 

  
BatchUpdateAdSpots |  Batch updates `AdSpot` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateAdSpots(NetworkName parent, List<UpdateAdSpotRequest> requests) 
  * batchUpdateAdSpots(String parent, List<UpdateAdSpotRequest> requests) 
  * batchUpdateAdSpots(BatchUpdateAdSpotsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateAdSpotsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdSpotServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdSpotServiceSettings adSpotServiceSettings =
         AdSpotServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create(adSpotServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdSpotServiceSettings adSpotServiceSettings =
         AdSpotServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create(adSpotServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdSpotServiceClient

## Static Methods 

### create()
    
    
    public static final AdSpotServiceClient create()

Constructs an instance of AdSpotServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdSpotServiceSettings settings)
    
    
    public static final AdSpotServiceClient create(AdSpotServiceSettings settings)

Constructs an instance of AdSpotServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdSpotServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdSpotServiceStub stub)
    
    
    public static final AdSpotServiceClient create(AdSpotServiceStub stub)

Constructs an instance of AdSpotServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdSpotServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdSpotServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdSpotServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient)` |   
  
## Constructors 

### AdSpotServiceClient(AdSpotServiceSettings settings)
    
    
    protected AdSpotServiceClient(AdSpotServiceSettings settings)

Constructs an instance of AdSpotServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdSpotServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceSettings)`  
  
  
### AdSpotServiceClient(AdSpotServiceStub stub)
    
    
    protected AdSpotServiceClient(AdSpotServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdSpotServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdSpotServiceStub)`  
  
  
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
  
### batchCreateAdSpots(@Nullable NetworkName parent, List<CreateAdSpotRequest> requests)
    
    
    public final BatchCreateAdSpotsResponse batchCreateAdSpots(@Nullable NetworkName parent, List<CreateAdSpotRequest> requests)

Batch creates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateAdSpotRequest> requests = new ArrayList<>();
       BatchCreateAdSpotsResponse response =
           adSpotServiceClient.batchCreateAdSpots(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdSpots` will be created. Format: `networks/{network_code}` The parent field in the CreateAdSpotRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdSpotRequest)>`  
Required. The `AdSpot` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsResponse)` |   
  
### batchCreateAdSpots(BatchCreateAdSpotsRequest request)
    
    
    public final BatchCreateAdSpotsResponse batchCreateAdSpots(BatchCreateAdSpotsRequest request)

Batch creates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       BatchCreateAdSpotsRequest request =
           BatchCreateAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdSpotRequest>())
               .build();
       BatchCreateAdSpotsResponse response = adSpotServiceClient.batchCreateAdSpots(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsResponse)` |   
  
### batchCreateAdSpots(String parent, List<CreateAdSpotRequest> requests)
    
    
    public final BatchCreateAdSpotsResponse batchCreateAdSpots(String parent, List<CreateAdSpotRequest> requests)

Batch creates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateAdSpotRequest> requests = new ArrayList<>();
       BatchCreateAdSpotsResponse response =
           adSpotServiceClient.batchCreateAdSpots(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdSpots` will be created. Format: `networks/{network_code}` The parent field in the CreateAdSpotRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdSpotRequest)>`  
Required. The `AdSpot` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsResponse)` |   
  
### batchCreateAdSpotsCallable()
    
    
    public final UnaryCallable<BatchCreateAdSpotsRequest,BatchCreateAdSpotsResponse> batchCreateAdSpotsCallable()

Batch creates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       BatchCreateAdSpotsRequest request =
           BatchCreateAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdSpotRequest>())
               .build();
       ApiFuture<BatchCreateAdSpotsResponse> future =
           adSpotServiceClient.batchCreateAdSpotsCallable().futureCall(request);
       // Do something.
       BatchCreateAdSpotsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsRequest),[BatchCreateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdSpotsResponse)>` |   
  
### batchUpdateAdSpots(@Nullable NetworkName parent, List<UpdateAdSpotRequest> requests)
    
    
    public final BatchUpdateAdSpotsResponse batchUpdateAdSpots(@Nullable NetworkName parent, List<UpdateAdSpotRequest> requests)

Batch updates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateAdSpotRequest> requests = new ArrayList<>();
       BatchUpdateAdSpotsResponse response =
           adSpotServiceClient.batchUpdateAdSpots(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdSpots` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdSpotRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdSpotRequest)>`  
Required. The `AdSpot` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsResponse)` |   
  
### batchUpdateAdSpots(BatchUpdateAdSpotsRequest request)
    
    
    public final BatchUpdateAdSpotsResponse batchUpdateAdSpots(BatchUpdateAdSpotsRequest request)

Batch updates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       BatchUpdateAdSpotsRequest request =
           BatchUpdateAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdSpotRequest>())
               .build();
       BatchUpdateAdSpotsResponse response = adSpotServiceClient.batchUpdateAdSpots(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsResponse)` |   
  
### batchUpdateAdSpots(String parent, List<UpdateAdSpotRequest> requests)
    
    
    public final BatchUpdateAdSpotsResponse batchUpdateAdSpots(String parent, List<UpdateAdSpotRequest> requests)

Batch updates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateAdSpotRequest> requests = new ArrayList<>();
       BatchUpdateAdSpotsResponse response =
           adSpotServiceClient.batchUpdateAdSpots(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdSpots` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdSpotRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdSpotRequest)>`  
Required. The `AdSpot` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsResponse)` |   
  
### batchUpdateAdSpotsCallable()
    
    
    public final UnaryCallable<BatchUpdateAdSpotsRequest,BatchUpdateAdSpotsResponse> batchUpdateAdSpotsCallable()

Batch updates `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       BatchUpdateAdSpotsRequest request =
           BatchUpdateAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdSpotRequest>())
               .build();
       ApiFuture<BatchUpdateAdSpotsResponse> future =
           adSpotServiceClient.batchUpdateAdSpotsCallable().futureCall(request);
       // Do something.
       BatchUpdateAdSpotsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsRequest),[BatchUpdateAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdSpotsResponse)>` |   
  
### close()
    
    
    public final void close()

### createAdSpot(@Nullable NetworkName parent, AdSpot adSpot)
    
    
    public final AdSpot createAdSpot(@Nullable NetworkName parent, AdSpot adSpot)

Creates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       AdSpot adSpot = AdSpot.newBuilder().build();
       AdSpot response = adSpotServiceClient.createAdSpot(parent, adSpot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `AdSpot` will be created. Format: `networks/{network_code}`  
`adSpot` | `[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)`  
Required. The `AdSpot` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### createAdSpot(CreateAdSpotRequest request)
    
    
    public final AdSpot createAdSpot(CreateAdSpotRequest request)

Creates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       CreateAdSpotRequest request =
           CreateAdSpotRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdSpot(AdSpot.newBuilder().build())
               .build();
       AdSpot response = adSpotServiceClient.createAdSpot(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdSpotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### createAdSpot(String parent, AdSpot adSpot)
    
    
    public final AdSpot createAdSpot(String parent, AdSpot adSpot)

Creates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       AdSpot adSpot = AdSpot.newBuilder().build();
       AdSpot response = adSpotServiceClient.createAdSpot(parent, adSpot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `AdSpot` will be created. Format: `networks/{network_code}`  
`adSpot` | `[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)`  
Required. The `AdSpot` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### createAdSpotCallable()
    
    
    public final UnaryCallable<CreateAdSpotRequest,AdSpot> createAdSpotCallable()

Creates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       CreateAdSpotRequest request =
           CreateAdSpotRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdSpot(AdSpot.newBuilder().build())
               .build();
       ApiFuture<AdSpot> future = adSpotServiceClient.createAdSpotCallable().futureCall(request);
       // Do something.
       AdSpot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdSpotRequest),[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)>` |   
  
### getAdSpot(@Nullable AdSpotName name)
    
    
    public final AdSpot getAdSpot(@Nullable AdSpotName name)

Retrieves an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       AdSpotName name = AdSpotName.of("[NETWORK_CODE]", "[AD_SPOT]");
       AdSpot response = adSpotServiceClient.getAdSpot(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdSpotName`  
Required. The resource name of the AdSpot. Format: `networks/{network_code}/adSpots/{ad_spot_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### getAdSpot(GetAdSpotRequest request)
    
    
    public final AdSpot getAdSpot(GetAdSpotRequest request)

Retrieves an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       GetAdSpotRequest request =
           GetAdSpotRequest.newBuilder()
               .setName(AdSpotName.of("[NETWORK_CODE]", "[AD_SPOT]").toString())
               .build();
       AdSpot response = adSpotServiceClient.getAdSpot(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdSpotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### getAdSpot(String name)
    
    
    public final AdSpot getAdSpot(String name)

Retrieves an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       String name = AdSpotName.of("[NETWORK_CODE]", "[AD_SPOT]").toString();
       AdSpot response = adSpotServiceClient.getAdSpot(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AdSpot. Format: `networks/{network_code}/adSpots/{ad_spot_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### getAdSpotCallable()
    
    
    public final UnaryCallable<GetAdSpotRequest,AdSpot> getAdSpotCallable()

Retrieves an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       GetAdSpotRequest request =
           GetAdSpotRequest.newBuilder()
               .setName(AdSpotName.of("[NETWORK_CODE]", "[AD_SPOT]").toString())
               .build();
       ApiFuture<AdSpot> future = adSpotServiceClient.getAdSpotCallable().futureCall(request);
       // Do something.
       AdSpot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdSpotRequest),[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)>` |   
  
### getSettings()
    
    
    public final @Nullable AdSpotServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdSpotServiceSettings` |   
  
### getStub()
    
    
    public AdSpotServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdSpotServiceStub)` |   
  
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
  
### listAdSpots(@Nullable NetworkName parent)
    
    
    public final AdSpotServiceClient.ListAdSpotsPagedResponse listAdSpots(@Nullable NetworkName parent)

Lists `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (AdSpot element : adSpotServiceClient.listAdSpots(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of AdSpots. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient.ListAdSpotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient.ListAdSpotsPagedResponse)` |   
  
### listAdSpots(ListAdSpotsRequest request)
    
    
    public final AdSpotServiceClient.ListAdSpotsPagedResponse listAdSpots(ListAdSpotsRequest request)

Lists `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       ListAdSpotsRequest request =
           ListAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AdSpot element : adSpotServiceClient.listAdSpots(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdSpotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient.ListAdSpotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient.ListAdSpotsPagedResponse)` |   
  
### listAdSpots(String parent)
    
    
    public final AdSpotServiceClient.ListAdSpotsPagedResponse listAdSpots(String parent)

Lists `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (AdSpot element : adSpotServiceClient.listAdSpots(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdSpots. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdSpotServiceClient.ListAdSpotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient.ListAdSpotsPagedResponse)` |   
  
### listAdSpotsCallable()
    
    
    public final UnaryCallable<ListAdSpotsRequest,ListAdSpotsResponse> listAdSpotsCallable()

Lists `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       ListAdSpotsRequest request =
           ListAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAdSpotsResponse response = adSpotServiceClient.listAdSpotsCallable().call(request);
         for (AdSpot element : response.getAdSpotsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdSpotsRequest),[ListAdSpotsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdSpotsResponse)>` |   
  
### listAdSpotsPagedCallable()
    
    
    public final UnaryCallable<ListAdSpotsRequest,AdSpotServiceClient.ListAdSpotsPagedResponse> listAdSpotsPagedCallable()

Lists `AdSpot` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       ListAdSpotsRequest request =
           ListAdSpotsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AdSpot> future = adSpotServiceClient.listAdSpotsPagedCallable().futureCall(request);
       // Do something.
       for (AdSpot element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdSpotsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdSpotsRequest),[ListAdSpotsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpotServiceClient.ListAdSpotsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAdSpot(AdSpot adSpot, FieldMask updateMask)
    
    
    public final AdSpot updateAdSpot(AdSpot adSpot, FieldMask updateMask)

Updates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       AdSpot adSpot = AdSpot.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AdSpot response = adSpotServiceClient.updateAdSpot(adSpot, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`adSpot` | `[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)`  
Required. The `AdSpot` to update. The `AdSpot`'s `name` is used to identify the `AdSpot` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### updateAdSpot(UpdateAdSpotRequest request)
    
    
    public final AdSpot updateAdSpot(UpdateAdSpotRequest request)

Updates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       UpdateAdSpotRequest request =
           UpdateAdSpotRequest.newBuilder()
               .setAdSpot(AdSpot.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AdSpot response = adSpotServiceClient.updateAdSpot(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdSpotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)` |   
  
### updateAdSpotCallable()
    
    
    public final UnaryCallable<UpdateAdSpotRequest,AdSpot> updateAdSpotCallable()

Updates an `AdSpot` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdSpotServiceClient adSpotServiceClient = AdSpotServiceClient.create()) {
       UpdateAdSpotRequest request =
           UpdateAdSpotRequest.newBuilder()
               .setAdSpot(AdSpot.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AdSpot> future = adSpotServiceClient.updateAdSpotCallable().futureCall(request);
       // Do something.
       AdSpot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdSpotRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdSpotRequest),[AdSpot](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdSpot)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
