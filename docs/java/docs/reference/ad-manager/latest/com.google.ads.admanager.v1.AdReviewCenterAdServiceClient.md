---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient
title: Class AdReviewCenterAdServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:18.826163+00:00
---

# Class AdReviewCenterAdServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdReviewCenterAdServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AdReviewCenterAdServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling AdReviewCenterAd objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       WebPropertyName parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]");
       for (AdReviewCenterAd element :
           adReviewCenterAdServiceClient.searchAdReviewCenterAds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

Note: close() needs to be called on the AdReviewCenterAdServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
SearchAdReviewCenterAds |  Searches for AdReviewCenterAds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchAdReviewCenterAds(SearchAdReviewCenterAdsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchAdReviewCenterAds(WebPropertyName parent) 
  * searchAdReviewCenterAds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchAdReviewCenterAdsPagedCallable() 
  * searchAdReviewCenterAdsCallable() 

  
BatchAllowAdReviewCenterAds |  Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchAllowAdReviewCenterAdsAsync(BatchAllowAdReviewCenterAdsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchAllowAdReviewCenterAdsAsync(WebPropertyName parent) 
  * batchAllowAdReviewCenterAdsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchAllowAdReviewCenterAdsOperationCallable() 
  * batchAllowAdReviewCenterAdsCallable() 

  
BatchBlockAdReviewCenterAds |  Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchBlockAdReviewCenterAdsAsync(BatchBlockAdReviewCenterAdsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchBlockAdReviewCenterAdsAsync(WebPropertyName parent) 
  * batchBlockAdReviewCenterAdsAsync(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchBlockAdReviewCenterAdsOperationCallable() 
  * batchBlockAdReviewCenterAdsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdReviewCenterAdServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdReviewCenterAdServiceSettings adReviewCenterAdServiceSettings =
         AdReviewCenterAdServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create(adReviewCenterAdServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdReviewCenterAdServiceSettings adReviewCenterAdServiceSettings =
         AdReviewCenterAdServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create(adReviewCenterAdServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdReviewCenterAdServiceClient

## Static Methods 

### create()
    
    
    public static final AdReviewCenterAdServiceClient create()

Constructs an instance of AdReviewCenterAdServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdReviewCenterAdServiceSettings settings)
    
    
    public static final AdReviewCenterAdServiceClient create(AdReviewCenterAdServiceSettings settings)

Constructs an instance of AdReviewCenterAdServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdReviewCenterAdServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdReviewCenterAdServiceStub stub)
    
    
    public static final AdReviewCenterAdServiceClient create(AdReviewCenterAdServiceStub stub)

Constructs an instance of AdReviewCenterAdServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdReviewCenterAdServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdReviewCenterAdServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdReviewCenterAdServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient)` |   
  
## Constructors 

### AdReviewCenterAdServiceClient(AdReviewCenterAdServiceSettings settings)
    
    
    protected AdReviewCenterAdServiceClient(AdReviewCenterAdServiceSettings settings)

Constructs an instance of AdReviewCenterAdServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdReviewCenterAdServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceSettings)`  
  
  
### AdReviewCenterAdServiceClient(AdReviewCenterAdServiceStub stub)
    
    
    protected AdReviewCenterAdServiceClient(AdReviewCenterAdServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdReviewCenterAdServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdReviewCenterAdServiceStub)`  
  
  
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
  
### batchAllowAdReviewCenterAdsAsync(@Nullable WebPropertyName parent)
    
    
    public final OperationFuture<BatchAllowAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchAllowAdReviewCenterAdsAsync(@Nullable WebPropertyName parent)

Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       WebPropertyName parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]");
       BatchAllowAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchAllowAdReviewCenterAdsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.WebPropertyName`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchAllowAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchAllowAdReviewCenterAdsAsync(BatchAllowAdReviewCenterAdsRequest request)
    
    
    public final OperationFuture<BatchAllowAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchAllowAdReviewCenterAdsAsync(BatchAllowAdReviewCenterAdsRequest request)

Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchAllowAdReviewCenterAdsRequest request =
           BatchAllowAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchAllowAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchAllowAdReviewCenterAdsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchAllowAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchAllowAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchAllowAdReviewCenterAdsAsync(String parent)
    
    
    public final OperationFuture<BatchAllowAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchAllowAdReviewCenterAdsAsync(String parent)

Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       String parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString();
       BatchAllowAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchAllowAdReviewCenterAdsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchAllowAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchAllowAdReviewCenterAdsCallable()
    
    
    public final UnaryCallable<BatchAllowAdReviewCenterAdsRequest,Operation> batchAllowAdReviewCenterAdsCallable()

Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchAllowAdReviewCenterAdsRequest request =
           BatchAllowAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           adReviewCenterAdServiceClient.batchAllowAdReviewCenterAdsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchAllowAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchAllowAdReviewCenterAdsOperationCallable()
    
    
    public final OperationCallable<BatchAllowAdReviewCenterAdsRequest,BatchAllowAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchAllowAdReviewCenterAdsOperationCallable()

Batch allows AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchAllowAdReviewCenterAdsRequest request =
           BatchAllowAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       OperationFuture<BatchAllowAdReviewCenterAdsResponse, BatchAdReviewCenterAdsOperationMetadata>
           future =
               adReviewCenterAdServiceClient
                   .batchAllowAdReviewCenterAdsOperationCallable()
                   .futureCall(request);
       // Do something.
       BatchAllowAdReviewCenterAdsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchAllowAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsRequest),[BatchAllowAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAllowAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchBlockAdReviewCenterAdsAsync(@Nullable WebPropertyName parent)
    
    
    public final OperationFuture<BatchBlockAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchBlockAdReviewCenterAdsAsync(@Nullable WebPropertyName parent)

Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       WebPropertyName parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]");
       BatchBlockAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchBlockAdReviewCenterAdsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.WebPropertyName`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchBlockAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchBlockAdReviewCenterAdsAsync(BatchBlockAdReviewCenterAdsRequest request)
    
    
    public final OperationFuture<BatchBlockAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchBlockAdReviewCenterAdsAsync(BatchBlockAdReviewCenterAdsRequest request)

Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchBlockAdReviewCenterAdsRequest request =
           BatchBlockAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchBlockAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchBlockAdReviewCenterAdsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchBlockAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchBlockAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchBlockAdReviewCenterAdsAsync(String parent)
    
    
    public final OperationFuture<BatchBlockAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchBlockAdReviewCenterAdsAsync(String parent)

Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       String parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString();
       BatchBlockAdReviewCenterAdsResponse response =
           adReviewCenterAdServiceClient.batchBlockAdReviewCenterAdsAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchBlockAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### batchBlockAdReviewCenterAdsCallable()
    
    
    public final UnaryCallable<BatchBlockAdReviewCenterAdsRequest,Operation> batchBlockAdReviewCenterAdsCallable()

Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchBlockAdReviewCenterAdsRequest request =
           BatchBlockAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           adReviewCenterAdServiceClient.batchBlockAdReviewCenterAdsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchBlockAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchBlockAdReviewCenterAdsOperationCallable()
    
    
    public final OperationCallable<BatchBlockAdReviewCenterAdsRequest,BatchBlockAdReviewCenterAdsResponse,BatchAdReviewCenterAdsOperationMetadata> batchBlockAdReviewCenterAdsOperationCallable()

Batch blocks AdReviewCenterAds. This method supports partial success. Some operations may succeed while others fail. Callers should check the failedRequests field in the response to determine which operations failed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       BatchBlockAdReviewCenterAdsRequest request =
           BatchBlockAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       OperationFuture<BatchBlockAdReviewCenterAdsResponse, BatchAdReviewCenterAdsOperationMetadata>
           future =
               adReviewCenterAdServiceClient
                   .batchBlockAdReviewCenterAdsOperationCallable()
                   .futureCall(request);
       // Do something.
       BatchBlockAdReviewCenterAdsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchBlockAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsRequest),[BatchBlockAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchBlockAdReviewCenterAdsResponse),[BatchAdReviewCenterAdsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchAdReviewCenterAdsOperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable AdReviewCenterAdServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdReviewCenterAdServiceSettings` |   
  
### getStub()
    
    
    public AdReviewCenterAdServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdReviewCenterAdServiceStub)` |   
  
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
  
### searchAdReviewCenterAds(@Nullable WebPropertyName parent)
    
    
    public final AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse searchAdReviewCenterAds(@Nullable WebPropertyName parent)

Searches for AdReviewCenterAds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       WebPropertyName parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]");
       for (AdReviewCenterAd element :
           adReviewCenterAdServiceClient.searchAdReviewCenterAds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.WebPropertyName`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse)` |   
  
### searchAdReviewCenterAds(SearchAdReviewCenterAdsRequest request)
    
    
    public final AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse searchAdReviewCenterAds(SearchAdReviewCenterAdsRequest request)

Searches for AdReviewCenterAds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       SearchAdReviewCenterAdsRequest request =
           SearchAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllAdReviewCenterAdId(new ArrayList<String>())
               .setDateTimeRange(Interval.newBuilder().build())
               .addAllSearchText(new ArrayList<String>())
               .addAllBuyerAccountId(new ArrayList<Long>())
               .build();
       for (AdReviewCenterAd element :
           adReviewCenterAdServiceClient.searchAdReviewCenterAds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SearchAdReviewCenterAdsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse)` |   
  
### searchAdReviewCenterAds(String parent)
    
    
    public final AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse searchAdReviewCenterAds(String parent)

Searches for AdReviewCenterAds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       String parent = WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString();
       for (AdReviewCenterAd element :
           adReviewCenterAdServiceClient.searchAdReviewCenterAds(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdReviewCenterAds. Format: networks/{network_code}/webProperties/{web_property_code} Since a network can only have a single web property of each `ExchangeSyndicationProduct`, you can use the `ExchangeSyndicationProduct` as an alias for the web property code: `networks/{network_code}/webProperties/display` `networks/{network_code}/webProperties/videoAndAudio` `networks/{network_code}/webProperties/mobileApp` `networks/{network_code}/webProperties/games`  
**Returns**  
---  
**Type** | **Description**  
`[AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse)` |   
  
### searchAdReviewCenterAdsCallable()
    
    
    public final UnaryCallable<SearchAdReviewCenterAdsRequest,SearchAdReviewCenterAdsResponse> searchAdReviewCenterAdsCallable()

Searches for AdReviewCenterAds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       SearchAdReviewCenterAdsRequest request =
           SearchAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllAdReviewCenterAdId(new ArrayList<String>())
               .setDateTimeRange(Interval.newBuilder().build())
               .addAllSearchText(new ArrayList<String>())
               .addAllBuyerAccountId(new ArrayList<Long>())
               .build();
       while (true) {
         SearchAdReviewCenterAdsResponse response =
             adReviewCenterAdServiceClient.searchAdReviewCenterAdsCallable().call(request);
         for (AdReviewCenterAd element : response.getAdReviewCenterAdsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SearchAdReviewCenterAdsRequest),[SearchAdReviewCenterAdsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SearchAdReviewCenterAdsResponse)>` |   
  
### searchAdReviewCenterAdsPagedCallable()
    
    
    public final UnaryCallable<SearchAdReviewCenterAdsRequest,AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse> searchAdReviewCenterAdsPagedCallable()

Searches for AdReviewCenterAds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdReviewCenterAdServiceClient adReviewCenterAdServiceClient =
         AdReviewCenterAdServiceClient.create()) {
       SearchAdReviewCenterAdsRequest request =
           SearchAdReviewCenterAdsRequest.newBuilder()
               .setParent(WebPropertyName.of("[NETWORK_CODE]", "[WEB_PROPERTY]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .addAllAdReviewCenterAdId(new ArrayList<String>())
               .setDateTimeRange(Interval.newBuilder().build())
               .addAllSearchText(new ArrayList<String>())
               .addAllBuyerAccountId(new ArrayList<Long>())
               .build();
       ApiFuture<AdReviewCenterAd> future =
           adReviewCenterAdServiceClient.searchAdReviewCenterAdsPagedCallable().futureCall(request);
       // Do something.
       for (AdReviewCenterAd element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchAdReviewCenterAdsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.SearchAdReviewCenterAdsRequest),[SearchAdReviewCenterAdsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdReviewCenterAdServiceClient.SearchAdReviewCenterAdsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
