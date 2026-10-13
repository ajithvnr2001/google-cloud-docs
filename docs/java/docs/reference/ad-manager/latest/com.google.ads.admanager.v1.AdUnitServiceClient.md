---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient
title: Class AdUnitServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:19.760266+00:00
---

# Class AdUnitServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdUnitServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AdUnitServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling AdUnit objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       AdUnitName name = AdUnitName.of("[NETWORK_CODE]", "[AD_UNIT]");
       AdUnit response = adUnitServiceClient.getAdUnit(name);
     }
     

Note: close() needs to be called on the AdUnitServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetAdUnit |  Retrieves an `AdUnit` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAdUnit(GetAdUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAdUnit(AdUnitName name) 
  * getAdUnit(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAdUnitCallable() 

  
ListAdUnits |  Lists `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdUnits(ListAdUnitsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdUnits(NetworkName parent) 
  * listAdUnits(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdUnitsPagedCallable() 
  * listAdUnitsCallable() 

  
ListAdUnitSizes |  Lists `AdUnitSize` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdUnitSizes(ListAdUnitSizesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdUnitSizes(NetworkName parent) 
  * listAdUnitSizes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdUnitSizesPagedCallable() 
  * listAdUnitSizesCallable() 

  
CreateAdUnit |  Creates an `AdUnit` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAdUnit(CreateAdUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAdUnit(NetworkName parent, AdUnit adUnit) 
  * createAdUnit(String parent, AdUnit adUnit) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAdUnitCallable() 

  
UpdateAdUnit |  Updates an `AdUnit` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAdUnit(UpdateAdUnitRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAdUnit(AdUnit adUnit, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAdUnitCallable() 

  
BatchCreateAdUnits |  Creates `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateAdUnits(NetworkName parent, List<CreateAdUnitRequest> requests) 
  * batchCreateAdUnits(String parent, List<CreateAdUnitRequest> requests) 
  * batchCreateAdUnits(BatchCreateAdUnitsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateAdUnitsCallable() 

  
BatchUpdateAdUnits |  Batch updates `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateAdUnits(NetworkName parent, List<UpdateAdUnitRequest> requests) 
  * batchUpdateAdUnits(String parent, List<UpdateAdUnitRequest> requests) 
  * batchUpdateAdUnits(BatchUpdateAdUnitsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateAdUnitsCallable() 

  
BatchActivateAdUnits |  Batch activates `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateAdUnits(BatchActivateAdUnitsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateAdUnits(NetworkName parent, List<String> names) 
  * batchActivateAdUnits(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateAdUnitsCallable() 

  
BatchDeactivateAdUnits |  Deactivates a list of `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeactivateAdUnits(BatchDeactivateAdUnitsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchDeactivateAdUnits(NetworkName parent, List<String> names) 
  * batchDeactivateAdUnits(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeactivateAdUnitsCallable() 

  
BatchArchiveAdUnits |  Archives a list of `AdUnit` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveAdUnits(BatchArchiveAdUnitsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveAdUnits(NetworkName parent, List<String> names) 
  * batchArchiveAdUnits(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveAdUnitsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdUnitServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdUnitServiceSettings adUnitServiceSettings =
         AdUnitServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create(adUnitServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdUnitServiceSettings adUnitServiceSettings =
         AdUnitServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create(adUnitServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdUnitServiceClient

## Static Methods 

### create()
    
    
    public static final AdUnitServiceClient create()

Constructs an instance of AdUnitServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdUnitServiceSettings settings)
    
    
    public static final AdUnitServiceClient create(AdUnitServiceSettings settings)

Constructs an instance of AdUnitServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdUnitServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdUnitServiceStub stub)
    
    
    public static final AdUnitServiceClient create(AdUnitServiceStub stub)

Constructs an instance of AdUnitServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdUnitServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdUnitServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdUnitServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient)` |   
  
## Constructors 

### AdUnitServiceClient(AdUnitServiceSettings settings)
    
    
    protected AdUnitServiceClient(AdUnitServiceSettings settings)

Constructs an instance of AdUnitServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdUnitServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceSettings)`  
  
  
### AdUnitServiceClient(AdUnitServiceStub stub)
    
    
    protected AdUnitServiceClient(AdUnitServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdUnitServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdUnitServiceStub)`  
  
  
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
  
### batchActivateAdUnits(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateAdUnitsResponse batchActivateAdUnits(@Nullable NetworkName parent, List<String> names)

Batch activates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateAdUnitsResponse response =
           adUnitServiceClient.batchActivateAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to activate. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsResponse)` |   
  
### batchActivateAdUnits(BatchActivateAdUnitsRequest request)
    
    
    public final BatchActivateAdUnitsResponse batchActivateAdUnits(BatchActivateAdUnitsRequest request)

Batch activates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchActivateAdUnitsRequest request =
           BatchActivateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateAdUnitsResponse response = adUnitServiceClient.batchActivateAdUnits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsResponse)` |   
  
### batchActivateAdUnits(String parent, List<String> names)
    
    
    public final BatchActivateAdUnitsResponse batchActivateAdUnits(String parent, List<String> names)

Batch activates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateAdUnitsResponse response =
           adUnitServiceClient.batchActivateAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to activate. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsResponse)` |   
  
### batchActivateAdUnitsCallable()
    
    
    public final UnaryCallable<BatchActivateAdUnitsRequest,BatchActivateAdUnitsResponse> batchActivateAdUnitsCallable()

Batch activates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchActivateAdUnitsRequest request =
           BatchActivateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateAdUnitsResponse> future =
           adUnitServiceClient.batchActivateAdUnitsCallable().futureCall(request);
       // Do something.
       BatchActivateAdUnitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsRequest),[BatchActivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateAdUnitsResponse)>` |   
  
### batchArchiveAdUnits(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveAdUnitsResponse batchArchiveAdUnits(@Nullable NetworkName parent, List<String> names)

Archives a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveAdUnitsResponse response = adUnitServiceClient.batchArchiveAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to archive. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsResponse)` |   
  
### batchArchiveAdUnits(BatchArchiveAdUnitsRequest request)
    
    
    public final BatchArchiveAdUnitsResponse batchArchiveAdUnits(BatchArchiveAdUnitsRequest request)

Archives a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchArchiveAdUnitsRequest request =
           BatchArchiveAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveAdUnitsResponse response = adUnitServiceClient.batchArchiveAdUnits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsResponse)` |   
  
### batchArchiveAdUnits(String parent, List<String> names)
    
    
    public final BatchArchiveAdUnitsResponse batchArchiveAdUnits(String parent, List<String> names)

Archives a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveAdUnitsResponse response = adUnitServiceClient.batchArchiveAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to archive. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsResponse)` |   
  
### batchArchiveAdUnitsCallable()
    
    
    public final UnaryCallable<BatchArchiveAdUnitsRequest,BatchArchiveAdUnitsResponse> batchArchiveAdUnitsCallable()

Archives a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchArchiveAdUnitsRequest request =
           BatchArchiveAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveAdUnitsResponse> future =
           adUnitServiceClient.batchArchiveAdUnitsCallable().futureCall(request);
       // Do something.
       BatchArchiveAdUnitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsRequest),[BatchArchiveAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveAdUnitsResponse)>` |   
  
### batchCreateAdUnits(@Nullable NetworkName parent, List<CreateAdUnitRequest> requests)
    
    
    public final BatchCreateAdUnitsResponse batchCreateAdUnits(@Nullable NetworkName parent, List<CreateAdUnitRequest> requests)

Creates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateAdUnitRequest> requests = new ArrayList<>();
       BatchCreateAdUnitsResponse response =
           adUnitServiceClient.batchCreateAdUnits(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdUnits` will be created. Format: `networks/{network_code}` The parent field in the CreateAdUnitRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdUnitRequest)>`  
Required. The `AdUnit` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsResponse)` |   
  
### batchCreateAdUnits(BatchCreateAdUnitsRequest request)
    
    
    public final BatchCreateAdUnitsResponse batchCreateAdUnits(BatchCreateAdUnitsRequest request)

Creates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchCreateAdUnitsRequest request =
           BatchCreateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdUnitRequest>())
               .build();
       BatchCreateAdUnitsResponse response = adUnitServiceClient.batchCreateAdUnits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsResponse)` |   
  
### batchCreateAdUnits(String parent, List<CreateAdUnitRequest> requests)
    
    
    public final BatchCreateAdUnitsResponse batchCreateAdUnits(String parent, List<CreateAdUnitRequest> requests)

Creates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateAdUnitRequest> requests = new ArrayList<>();
       BatchCreateAdUnitsResponse response =
           adUnitServiceClient.batchCreateAdUnits(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdUnits` will be created. Format: `networks/{network_code}` The parent field in the CreateAdUnitRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdUnitRequest)>`  
Required. The `AdUnit` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsResponse)` |   
  
### batchCreateAdUnitsCallable()
    
    
    public final UnaryCallable<BatchCreateAdUnitsRequest,BatchCreateAdUnitsResponse> batchCreateAdUnitsCallable()

Creates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchCreateAdUnitsRequest request =
           BatchCreateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateAdUnitRequest>())
               .build();
       ApiFuture<BatchCreateAdUnitsResponse> future =
           adUnitServiceClient.batchCreateAdUnitsCallable().futureCall(request);
       // Do something.
       BatchCreateAdUnitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsRequest),[BatchCreateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateAdUnitsResponse)>` |   
  
### batchDeactivateAdUnits(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchDeactivateAdUnitsResponse batchDeactivateAdUnits(@Nullable NetworkName parent, List<String> names)

Deactivates a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchDeactivateAdUnitsResponse response =
           adUnitServiceClient.batchDeactivateAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to deactivate. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsResponse)` |   
  
### batchDeactivateAdUnits(BatchDeactivateAdUnitsRequest request)
    
    
    public final BatchDeactivateAdUnitsResponse batchDeactivateAdUnits(BatchDeactivateAdUnitsRequest request)

Deactivates a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchDeactivateAdUnitsRequest request =
           BatchDeactivateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeactivateAdUnitsResponse response = adUnitServiceClient.batchDeactivateAdUnits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeactivateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsResponse)` |   
  
### batchDeactivateAdUnits(String parent, List<String> names)
    
    
    public final BatchDeactivateAdUnitsResponse batchDeactivateAdUnits(String parent, List<String> names)

Deactivates a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchDeactivateAdUnitsResponse response =
           adUnitServiceClient.batchDeactivateAdUnits(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `AdUnit`s to deactivate. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchDeactivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsResponse)` |   
  
### batchDeactivateAdUnitsCallable()
    
    
    public final UnaryCallable<BatchDeactivateAdUnitsRequest,BatchDeactivateAdUnitsResponse> batchDeactivateAdUnitsCallable()

Deactivates a list of `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchDeactivateAdUnitsRequest request =
           BatchDeactivateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchDeactivateAdUnitsResponse> future =
           adUnitServiceClient.batchDeactivateAdUnitsCallable().futureCall(request);
       // Do something.
       BatchDeactivateAdUnitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeactivateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsRequest),[BatchDeactivateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchDeactivateAdUnitsResponse)>` |   
  
### batchUpdateAdUnits(@Nullable NetworkName parent, List<UpdateAdUnitRequest> requests)
    
    
    public final BatchUpdateAdUnitsResponse batchUpdateAdUnits(@Nullable NetworkName parent, List<UpdateAdUnitRequest> requests)

Batch updates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateAdUnitRequest> requests = new ArrayList<>();
       BatchUpdateAdUnitsResponse response =
           adUnitServiceClient.batchUpdateAdUnits(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `AdUnits` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdUnitRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdUnitRequest)>`  
Required. The `AdUnit` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsResponse)` |   
  
### batchUpdateAdUnits(BatchUpdateAdUnitsRequest request)
    
    
    public final BatchUpdateAdUnitsResponse batchUpdateAdUnits(BatchUpdateAdUnitsRequest request)

Batch updates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchUpdateAdUnitsRequest request =
           BatchUpdateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdUnitRequest>())
               .build();
       BatchUpdateAdUnitsResponse response = adUnitServiceClient.batchUpdateAdUnits(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsResponse)` |   
  
### batchUpdateAdUnits(String parent, List<UpdateAdUnitRequest> requests)
    
    
    public final BatchUpdateAdUnitsResponse batchUpdateAdUnits(String parent, List<UpdateAdUnitRequest> requests)

Batch updates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateAdUnitRequest> requests = new ArrayList<>();
       BatchUpdateAdUnitsResponse response =
           adUnitServiceClient.batchUpdateAdUnits(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `AdUnits` will be updated. Format: `networks/{network_code}` The parent field in the UpdateAdUnitRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdUnitRequest)>`  
Required. The `AdUnit` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsResponse)` |   
  
### batchUpdateAdUnitsCallable()
    
    
    public final UnaryCallable<BatchUpdateAdUnitsRequest,BatchUpdateAdUnitsResponse> batchUpdateAdUnitsCallable()

Batch updates `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       BatchUpdateAdUnitsRequest request =
           BatchUpdateAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateAdUnitRequest>())
               .build();
       ApiFuture<BatchUpdateAdUnitsResponse> future =
           adUnitServiceClient.batchUpdateAdUnitsCallable().futureCall(request);
       // Do something.
       BatchUpdateAdUnitsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsRequest),[BatchUpdateAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateAdUnitsResponse)>` |   
  
### close()
    
    
    public final void close()

### createAdUnit(@Nullable NetworkName parent, AdUnit adUnit)
    
    
    public final AdUnit createAdUnit(@Nullable NetworkName parent, AdUnit adUnit)

Creates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       AdUnit adUnit = AdUnit.newBuilder().build();
       AdUnit response = adUnitServiceClient.createAdUnit(parent, adUnit);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `AdUnit` will be created. Format: `networks/{network_code}`  
`adUnit` | `[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)`  
Required. The `AdUnit` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### createAdUnit(CreateAdUnitRequest request)
    
    
    public final AdUnit createAdUnit(CreateAdUnitRequest request)

Creates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       CreateAdUnitRequest request =
           CreateAdUnitRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdUnit(AdUnit.newBuilder().build())
               .build();
       AdUnit response = adUnitServiceClient.createAdUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### createAdUnit(String parent, AdUnit adUnit)
    
    
    public final AdUnit createAdUnit(String parent, AdUnit adUnit)

Creates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       AdUnit adUnit = AdUnit.newBuilder().build();
       AdUnit response = adUnitServiceClient.createAdUnit(parent, adUnit);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `AdUnit` will be created. Format: `networks/{network_code}`  
`adUnit` | `[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)`  
Required. The `AdUnit` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### createAdUnitCallable()
    
    
    public final UnaryCallable<CreateAdUnitRequest,AdUnit> createAdUnitCallable()

Creates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       CreateAdUnitRequest request =
           CreateAdUnitRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setAdUnit(AdUnit.newBuilder().build())
               .build();
       ApiFuture<AdUnit> future = adUnitServiceClient.createAdUnitCallable().futureCall(request);
       // Do something.
       AdUnit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdUnitRequest),[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)>` |   
  
### getAdUnit(@Nullable AdUnitName name)
    
    
    public final AdUnit getAdUnit(@Nullable AdUnitName name)

Retrieves an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       AdUnitName name = AdUnitName.of("[NETWORK_CODE]", "[AD_UNIT]");
       AdUnit response = adUnitServiceClient.getAdUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdUnitName`  
Required. The resource name of the AdUnit. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### getAdUnit(GetAdUnitRequest request)
    
    
    public final AdUnit getAdUnit(GetAdUnitRequest request)

Retrieves an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       GetAdUnitRequest request =
           GetAdUnitRequest.newBuilder()
               .setName(AdUnitName.of("[NETWORK_CODE]", "[AD_UNIT]").toString())
               .build();
       AdUnit response = adUnitServiceClient.getAdUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### getAdUnit(String name)
    
    
    public final AdUnit getAdUnit(String name)

Retrieves an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String name = AdUnitName.of("[NETWORK_CODE]", "[AD_UNIT]").toString();
       AdUnit response = adUnitServiceClient.getAdUnit(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AdUnit. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### getAdUnitCallable()
    
    
    public final UnaryCallable<GetAdUnitRequest,AdUnit> getAdUnitCallable()

Retrieves an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       GetAdUnitRequest request =
           GetAdUnitRequest.newBuilder()
               .setName(AdUnitName.of("[NETWORK_CODE]", "[AD_UNIT]").toString())
               .build();
       ApiFuture<AdUnit> future = adUnitServiceClient.getAdUnitCallable().futureCall(request);
       // Do something.
       AdUnit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdUnitRequest),[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)>` |   
  
### getSettings()
    
    
    public final @Nullable AdUnitServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdUnitServiceSettings` |   
  
### getStub()
    
    
    public AdUnitServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdUnitServiceStub)` |   
  
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
  
### listAdUnitSizes(@Nullable NetworkName parent)
    
    
    public final AdUnitServiceClient.ListAdUnitSizesPagedResponse listAdUnitSizes(@Nullable NetworkName parent)

Lists `AdUnitSize` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (AdUnitSize element : adUnitServiceClient.listAdUnitSizes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of AdUnitSizes. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitSizesPagedResponse)` |   
  
### listAdUnitSizes(ListAdUnitSizesRequest request)
    
    
    public final AdUnitServiceClient.ListAdUnitSizesPagedResponse listAdUnitSizes(ListAdUnitSizesRequest request)

Lists `AdUnitSize` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitSizesRequest request =
           ListAdUnitSizesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AdUnitSize element : adUnitServiceClient.listAdUnitSizes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdUnitSizesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitSizesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitSizesPagedResponse)` |   
  
### listAdUnitSizes(String parent)
    
    
    public final AdUnitServiceClient.ListAdUnitSizesPagedResponse listAdUnitSizes(String parent)

Lists `AdUnitSize` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (AdUnitSize element : adUnitServiceClient.listAdUnitSizes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdUnitSizes. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitSizesPagedResponse)` |   
  
### listAdUnitSizesCallable()
    
    
    public final UnaryCallable<ListAdUnitSizesRequest,ListAdUnitSizesResponse> listAdUnitSizesCallable()

Lists `AdUnitSize` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitSizesRequest request =
           ListAdUnitSizesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAdUnitSizesResponse response =
             adUnitServiceClient.listAdUnitSizesCallable().call(request);
         for (AdUnitSize element : response.getAdUnitSizesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdUnitSizesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitSizesRequest),[ListAdUnitSizesResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitSizesResponse)>` |   
  
### listAdUnitSizesPagedCallable()
    
    
    public final UnaryCallable<ListAdUnitSizesRequest,AdUnitServiceClient.ListAdUnitSizesPagedResponse> listAdUnitSizesPagedCallable()

Lists `AdUnitSize` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitSizesRequest request =
           ListAdUnitSizesRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AdUnitSize> future =
           adUnitServiceClient.listAdUnitSizesPagedCallable().futureCall(request);
       // Do something.
       for (AdUnitSize element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdUnitSizesRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitSizesRequest),[ListAdUnitSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitSizesPagedResponse)>` |   
  
### listAdUnits(@Nullable NetworkName parent)
    
    
    public final AdUnitServiceClient.ListAdUnitsPagedResponse listAdUnits(@Nullable NetworkName parent)

Lists `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (AdUnit element : adUnitServiceClient.listAdUnits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of AdUnits. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitsPagedResponse)` |   
  
### listAdUnits(ListAdUnitsRequest request)
    
    
    public final AdUnitServiceClient.ListAdUnitsPagedResponse listAdUnits(ListAdUnitsRequest request)

Lists `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitsRequest request =
           ListAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AdUnit element : adUnitServiceClient.listAdUnits(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitsPagedResponse)` |   
  
### listAdUnits(String parent)
    
    
    public final AdUnitServiceClient.ListAdUnitsPagedResponse listAdUnits(String parent)

Lists `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (AdUnit element : adUnitServiceClient.listAdUnits(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdUnits. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[AdUnitServiceClient.ListAdUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitsPagedResponse)` |   
  
### listAdUnitsCallable()
    
    
    public final UnaryCallable<ListAdUnitsRequest,ListAdUnitsResponse> listAdUnitsCallable()

Lists `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitsRequest request =
           ListAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAdUnitsResponse response = adUnitServiceClient.listAdUnitsCallable().call(request);
         for (AdUnit element : response.getAdUnitsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitsRequest),[ListAdUnitsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitsResponse)>` |   
  
### listAdUnitsPagedCallable()
    
    
    public final UnaryCallable<ListAdUnitsRequest,AdUnitServiceClient.ListAdUnitsPagedResponse> listAdUnitsPagedCallable()

Lists `AdUnit` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       ListAdUnitsRequest request =
           ListAdUnitsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AdUnit> future = adUnitServiceClient.listAdUnitsPagedCallable().futureCall(request);
       // Do something.
       for (AdUnit element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdUnitsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdUnitsRequest),[ListAdUnitsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnitServiceClient.ListAdUnitsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAdUnit(AdUnit adUnit, FieldMask updateMask)
    
    
    public final AdUnit updateAdUnit(AdUnit adUnit, FieldMask updateMask)

Updates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       AdUnit adUnit = AdUnit.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AdUnit response = adUnitServiceClient.updateAdUnit(adUnit, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`adUnit` | `[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)`  
Required. The `AdUnit` to update. The `AdUnit`'s name is used to identify the `AdUnit` to update. Format: `networks/{network_code}/adUnits/{ad_unit_id}`  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### updateAdUnit(UpdateAdUnitRequest request)
    
    
    public final AdUnit updateAdUnit(UpdateAdUnitRequest request)

Updates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       UpdateAdUnitRequest request =
           UpdateAdUnitRequest.newBuilder()
               .setAdUnit(AdUnit.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AdUnit response = adUnitServiceClient.updateAdUnit(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdUnitRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)` |   
  
### updateAdUnitCallable()
    
    
    public final UnaryCallable<UpdateAdUnitRequest,AdUnit> updateAdUnitCallable()

Updates an `AdUnit` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdUnitServiceClient adUnitServiceClient = AdUnitServiceClient.create()) {
       UpdateAdUnitRequest request =
           UpdateAdUnitRequest.newBuilder()
               .setAdUnit(AdUnit.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AdUnit> future = adUnitServiceClient.updateAdUnitCallable().futureCall(request);
       // Do something.
       AdUnit response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdUnitRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdUnitRequest),[AdUnit](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdUnit)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
