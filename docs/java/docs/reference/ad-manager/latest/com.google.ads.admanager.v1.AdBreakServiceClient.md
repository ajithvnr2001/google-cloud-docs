---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient
title: Class AdBreakServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:17.752930+00:00
---

# Class AdBreakServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AdBreakServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/AdBreakServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `AdBreak` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       AdBreakName name = AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]");
       AdBreak response = adBreakServiceClient.getAdBreak(name);
     }
     

Note: close() needs to be called on the AdBreakServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetAdBreak |  Retrieves an `AdBreak` object.  Query an ad break by its resource name or custom asset key. Check the resource's `breakState` field to determine its state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAdBreak(GetAdBreakRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAdBreak(AdBreakName name) 
  * getAdBreak(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAdBreakCallable() 

  
ListAdBreaks |  Lists `AdBreak` objects.  By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAdBreaks(ListAdBreaksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAdBreaks(LiveStreamEventName parent) 
  * listAdBreaks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAdBreaksPagedCallable() 
  * listAdBreaksCallable() 

  
CreateAdBreak |  Creates an `AdBreak` object.  Informs DAI of an upcoming ad break for a live stream event, with an optional expected start time. DAI will begin decisioning ads for the break shortly before the expected start time, if provided. Each live stream event can only have one incomplete ad break at any given time. The next ad break can be scheduled after the previous ad break has started serving, indicated by its state being `COMPLETE`, or it has been deleted.  This method cannot be used if the `LiveStreamEvent` has [prefetching ad breaks enabled](https://developers.google.com/ad-manager/api/reference/latest/LiveStreamEventService.LiveStreamEvent#prefetchenabled) or the event is not active. If a `LiveStreamEvent` is deactivated after creating an ad break and before the ad break is complete, the ad break is discarded.  An ad break's state is complete when the following occurs: - Full service DAI: after a matching ad break shows in the `LiveStreamEvent` manifest only when the ad break has started decisioning. - Pod Serving: after the ad break is requested using the ad break ID or break sequence. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAdBreak(CreateAdBreakRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createAdBreak(LiveStreamEventName parent, AdBreak adBreak) 
  * createAdBreak(String parent, AdBreak adBreak) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAdBreakCallable() 

  
UpdateAdBreak |  Updates an `AdBreak` object.  Modify an ad break when its state is `SCHEDULED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAdBreak(UpdateAdBreakRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAdBreak(AdBreak adBreak, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAdBreakCallable() 

  
DeleteAdBreak |  Deletes an `AdBreak` object.  Deletes and cancels an incomplete ad break, mitigating the need to wait for the current break to serve before recreating an ad break. You can delete an ad break that has not started serving or seen in manifests, indicated by its state being `SCHEDULED` or `DECISIONED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAdBreak(DeleteAdBreakRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteAdBreak(AdBreakName name) 
  * deleteAdBreak(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAdBreakCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AdBreakServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdBreakServiceSettings adBreakServiceSettings =
         AdBreakServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create(adBreakServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AdBreakServiceSettings adBreakServiceSettings =
         AdBreakServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create(adBreakServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AdBreakServiceClient

## Static Methods 

### create()
    
    
    public static final AdBreakServiceClient create()

Constructs an instance of AdBreakServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdBreakServiceSettings settings)
    
    
    public static final AdBreakServiceClient create(AdBreakServiceSettings settings)

Constructs an instance of AdBreakServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdBreakServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AdBreakServiceStub stub)
    
    
    public static final AdBreakServiceClient create(AdBreakServiceStub stub)

Constructs an instance of AdBreakServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(AdBreakServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdBreakServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdBreakServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient)` |   
  
## Constructors 

### AdBreakServiceClient(AdBreakServiceSettings settings)
    
    
    protected AdBreakServiceClient(AdBreakServiceSettings settings)

Constructs an instance of AdBreakServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AdBreakServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceSettings)`  
  
  
### AdBreakServiceClient(AdBreakServiceStub stub)
    
    
    protected AdBreakServiceClient(AdBreakServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AdBreakServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdBreakServiceStub)`  
  
  
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

### createAdBreak(@Nullable LiveStreamEventName parent, AdBreak adBreak)
    
    
    public final AdBreak createAdBreak(@Nullable LiveStreamEventName parent, AdBreak adBreak)

Creates an `AdBreak` object.

Informs DAI of an upcoming ad break for a live stream event, with an optional expected start time. DAI will begin decisioning ads for the break shortly before the expected start time, if provided. Each live stream event can only have one incomplete ad break at any given time. The next ad break can be scheduled after the previous ad break has started serving, indicated by its state being `COMPLETE`, or it has been deleted.

This method cannot be used if the `LiveStreamEvent` has [prefetching ad breaks enabled](https://developers.google.com/ad-manager/api/reference/latest/LiveStreamEventService.LiveStreamEvent#prefetchenabled) or the event is not active. If a `LiveStreamEvent` is deactivated after creating an ad break and before the ad break is complete, the ad break is discarded.

An ad break's state is complete when the following occurs: - Full service DAI: after a matching ad break shows in the `LiveStreamEvent` manifest only when the ad break has started decisioning. - Pod Serving: after the ad break is requested using the ad break ID or break sequence.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       LiveStreamEventName parent = LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]");
       AdBreak adBreak = AdBreak.newBuilder().build();
       AdBreak response = adBreakServiceClient.createAdBreak(parent, adBreak);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LiveStreamEventName`  
Required. The parent resource where this `AdBreak` will be created identified by an asset key or custom asset key. Formats: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}`  
`adBreak` | `[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)`  
Required. The `AdBreak` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### createAdBreak(CreateAdBreakRequest request)
    
    
    public final AdBreak createAdBreak(CreateAdBreakRequest request)

Creates an `AdBreak` object.

Informs DAI of an upcoming ad break for a live stream event, with an optional expected start time. DAI will begin decisioning ads for the break shortly before the expected start time, if provided. Each live stream event can only have one incomplete ad break at any given time. The next ad break can be scheduled after the previous ad break has started serving, indicated by its state being `COMPLETE`, or it has been deleted.

This method cannot be used if the `LiveStreamEvent` has [prefetching ad breaks enabled](https://developers.google.com/ad-manager/api/reference/latest/LiveStreamEventService.LiveStreamEvent#prefetchenabled) or the event is not active. If a `LiveStreamEvent` is deactivated after creating an ad break and before the ad break is complete, the ad break is discarded.

An ad break's state is complete when the following occurs: - Full service DAI: after a matching ad break shows in the `LiveStreamEvent` manifest only when the ad break has started decisioning. - Pod Serving: after the ad break is requested using the ad break ID or break sequence.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       CreateAdBreakRequest request =
           CreateAdBreakRequest.newBuilder()
               .setParent(LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString())
               .setAdBreak(AdBreak.newBuilder().build())
               .build();
       AdBreak response = adBreakServiceClient.createAdBreak(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdBreakRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### createAdBreak(String parent, AdBreak adBreak)
    
    
    public final AdBreak createAdBreak(String parent, AdBreak adBreak)

Creates an `AdBreak` object.

Informs DAI of an upcoming ad break for a live stream event, with an optional expected start time. DAI will begin decisioning ads for the break shortly before the expected start time, if provided. Each live stream event can only have one incomplete ad break at any given time. The next ad break can be scheduled after the previous ad break has started serving, indicated by its state being `COMPLETE`, or it has been deleted.

This method cannot be used if the `LiveStreamEvent` has [prefetching ad breaks enabled](https://developers.google.com/ad-manager/api/reference/latest/LiveStreamEventService.LiveStreamEvent#prefetchenabled) or the event is not active. If a `LiveStreamEvent` is deactivated after creating an ad break and before the ad break is complete, the ad break is discarded.

An ad break's state is complete when the following occurs: - Full service DAI: after a matching ad break shows in the `LiveStreamEvent` manifest only when the ad break has started decisioning. - Pod Serving: after the ad break is requested using the ad break ID or break sequence.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       String parent = LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString();
       AdBreak adBreak = AdBreak.newBuilder().build();
       AdBreak response = adBreakServiceClient.createAdBreak(parent, adBreak);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `AdBreak` will be created identified by an asset key or custom asset key. Formats: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}`  
`adBreak` | `[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)`  
Required. The `AdBreak` to create.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### createAdBreakCallable()
    
    
    public final UnaryCallable<CreateAdBreakRequest,AdBreak> createAdBreakCallable()

Creates an `AdBreak` object.

Informs DAI of an upcoming ad break for a live stream event, with an optional expected start time. DAI will begin decisioning ads for the break shortly before the expected start time, if provided. Each live stream event can only have one incomplete ad break at any given time. The next ad break can be scheduled after the previous ad break has started serving, indicated by its state being `COMPLETE`, or it has been deleted.

This method cannot be used if the `LiveStreamEvent` has [prefetching ad breaks enabled](https://developers.google.com/ad-manager/api/reference/latest/LiveStreamEventService.LiveStreamEvent#prefetchenabled) or the event is not active. If a `LiveStreamEvent` is deactivated after creating an ad break and before the ad break is complete, the ad break is discarded.

An ad break's state is complete when the following occurs: - Full service DAI: after a matching ad break shows in the `LiveStreamEvent` manifest only when the ad break has started decisioning. - Pod Serving: after the ad break is requested using the ad break ID or break sequence.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       CreateAdBreakRequest request =
           CreateAdBreakRequest.newBuilder()
               .setParent(LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString())
               .setAdBreak(AdBreak.newBuilder().build())
               .build();
       ApiFuture<AdBreak> future = adBreakServiceClient.createAdBreakCallable().futureCall(request);
       // Do something.
       AdBreak response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateAdBreakRequest),[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)>` |   
  
### deleteAdBreak(@Nullable AdBreakName name)
    
    
    public final void deleteAdBreak(@Nullable AdBreakName name)

Deletes an `AdBreak` object.

Deletes and cancels an incomplete ad break, mitigating the need to wait for the current break to serve before recreating an ad break. You can delete an ad break that has not started serving or seen in manifests, indicated by its state being `SCHEDULED` or `DECISIONED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       AdBreakName name = AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]");
       adBreakServiceClient.deleteAdBreak(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdBreakName`  
Required. The name of the ad break to delete. Format: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break}`  
  
### deleteAdBreak(DeleteAdBreakRequest request)
    
    
    public final void deleteAdBreak(DeleteAdBreakRequest request)

Deletes an `AdBreak` object.

Deletes and cancels an incomplete ad break, mitigating the need to wait for the current break to serve before recreating an ad break. You can delete an ad break that has not started serving or seen in manifests, indicated by its state being `SCHEDULED` or `DECISIONED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       DeleteAdBreakRequest request =
           DeleteAdBreakRequest.newBuilder()
               .setName(AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString())
               .build();
       adBreakServiceClient.deleteAdBreak(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeleteAdBreakRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteAdBreak(String name)
    
    
    public final void deleteAdBreak(String name)

Deletes an `AdBreak` object.

Deletes and cancels an incomplete ad break, mitigating the need to wait for the current break to serve before recreating an ad break. You can delete an ad break that has not started serving or seen in manifests, indicated by its state being `SCHEDULED` or `DECISIONED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       String name = AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString();
       adBreakServiceClient.deleteAdBreak(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ad break to delete. Format: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break}`  
  
### deleteAdBreakCallable()
    
    
    public final UnaryCallable<DeleteAdBreakRequest,Empty> deleteAdBreakCallable()

Deletes an `AdBreak` object.

Deletes and cancels an incomplete ad break, mitigating the need to wait for the current break to serve before recreating an ad break. You can delete an ad break that has not started serving or seen in manifests, indicated by its state being `SCHEDULED` or `DECISIONED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       DeleteAdBreakRequest request =
           DeleteAdBreakRequest.newBuilder()
               .setName(AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString())
               .build();
       ApiFuture<Empty> future = adBreakServiceClient.deleteAdBreakCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DeleteAdBreakRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getAdBreak(@Nullable AdBreakName name)
    
    
    public final AdBreak getAdBreak(@Nullable AdBreakName name)

Retrieves an `AdBreak` object.

Query an ad break by its resource name or custom asset key. Check the resource's `breakState` field to determine its state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       AdBreakName name = AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]");
       AdBreak response = adBreakServiceClient.getAdBreak(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdBreakName`  
Required. The resource name of the AdBreak using the asset key or custom asset key. Format: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break_id}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}/adBreaks/{ad_break_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### getAdBreak(GetAdBreakRequest request)
    
    
    public final AdBreak getAdBreak(GetAdBreakRequest request)

Retrieves an `AdBreak` object.

Query an ad break by its resource name or custom asset key. Check the resource's `breakState` field to determine its state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       GetAdBreakRequest request =
           GetAdBreakRequest.newBuilder()
               .setName(AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString())
               .build();
       AdBreak response = adBreakServiceClient.getAdBreak(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdBreakRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### getAdBreak(String name)
    
    
    public final AdBreak getAdBreak(String name)

Retrieves an `AdBreak` object.

Query an ad break by its resource name or custom asset key. Check the resource's `breakState` field to determine its state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       String name = AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString();
       AdBreak response = adBreakServiceClient.getAdBreak(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the AdBreak using the asset key or custom asset key. Format: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break_id}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}/adBreaks/{ad_break_id}`  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### getAdBreakCallable()
    
    
    public final UnaryCallable<GetAdBreakRequest,AdBreak> getAdBreakCallable()

Retrieves an `AdBreak` object.

Query an ad break by its resource name or custom asset key. Check the resource's `breakState` field to determine its state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       GetAdBreakRequest request =
           GetAdBreakRequest.newBuilder()
               .setName(AdBreakName.of("[NETWORK_CODE]", "[ASSET_KEY]", "[AD_BREAK]").toString())
               .build();
       ApiFuture<AdBreak> future = adBreakServiceClient.getAdBreakCallable().futureCall(request);
       // Do something.
       AdBreak response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetAdBreakRequest),[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)>` |   
  
### getSettings()
    
    
    public final @Nullable AdBreakServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.AdBreakServiceSettings` |   
  
### getStub()
    
    
    public AdBreakServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.AdBreakServiceStub)` |   
  
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
  
### listAdBreaks(@Nullable LiveStreamEventName parent)
    
    
    public final AdBreakServiceClient.ListAdBreaksPagedResponse listAdBreaks(@Nullable LiveStreamEventName parent)

Lists `AdBreak` objects.

By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       LiveStreamEventName parent = LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]");
       for (AdBreak element : adBreakServiceClient.listAdBreaks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LiveStreamEventName`  
Required. The parent, which owns this collection of AdBreaks. Formats: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}`  
**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient.ListAdBreaksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient.ListAdBreaksPagedResponse)` |   
  
### listAdBreaks(ListAdBreaksRequest request)
    
    
    public final AdBreakServiceClient.ListAdBreaksPagedResponse listAdBreaks(ListAdBreaksRequest request)

Lists `AdBreak` objects.

By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       ListAdBreaksRequest request =
           ListAdBreaksRequest.newBuilder()
               .setParent(LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (AdBreak element : adBreakServiceClient.listAdBreaks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAdBreaksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdBreaksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient.ListAdBreaksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient.ListAdBreaksPagedResponse)` |   
  
### listAdBreaks(String parent)
    
    
    public final AdBreakServiceClient.ListAdBreaksPagedResponse listAdBreaks(String parent)

Lists `AdBreak` objects.

By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       String parent = LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString();
       for (AdBreak element : adBreakServiceClient.listAdBreaks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of AdBreaks. Formats: `networks/{network_code}/liveStreamEventsByAssetKey/{asset_key}` `networks/{network_code}/liveStreamEventsByCustomAssetKey/{custom_asset_key}`  
**Returns**  
---  
**Type** | **Description**  
`[AdBreakServiceClient.ListAdBreaksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient.ListAdBreaksPagedResponse)` |   
  
### listAdBreaksCallable()
    
    
    public final UnaryCallable<ListAdBreaksRequest,ListAdBreaksResponse> listAdBreaksCallable()

Lists `AdBreak` objects.

By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       ListAdBreaksRequest request =
           ListAdBreaksRequest.newBuilder()
               .setParent(LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListAdBreaksResponse response = adBreakServiceClient.listAdBreaksCallable().call(request);
         for (AdBreak element : response.getAdBreaksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdBreaksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdBreaksRequest),[ListAdBreaksResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdBreaksResponse)>` |   
  
### listAdBreaksPagedCallable()
    
    
    public final UnaryCallable<ListAdBreaksRequest,AdBreakServiceClient.ListAdBreaksPagedResponse> listAdBreaksPagedCallable()

Lists `AdBreak` objects.

By default, when no `orderBy` query parameter is specified, ad breaks are ordered reverse chronologically. However, ad breaks with a 'breakState' of 'SCHEDULED' or 'DECISIONED' are prioritized and appear first.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       ListAdBreaksRequest request =
           ListAdBreaksRequest.newBuilder()
               .setParent(LiveStreamEventName.of("[NETWORK_CODE]", "[LIVE_STREAM_EVENT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<AdBreak> future =
           adBreakServiceClient.listAdBreaksPagedCallable().futureCall(request);
       // Do something.
       for (AdBreak element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAdBreaksRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListAdBreaksRequest),[ListAdBreaksPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreakServiceClient.ListAdBreaksPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAdBreak(AdBreak adBreak, FieldMask updateMask)
    
    
    public final AdBreak updateAdBreak(AdBreak adBreak, FieldMask updateMask)

Updates an `AdBreak` object.

Modify an ad break when its state is `SCHEDULED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       AdBreak adBreak = AdBreak.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       AdBreak response = adBreakServiceClient.updateAdBreak(adBreak, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`adBreak` | `[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)`  
Required. The `AdBreak` to update. The `AdBreak`'s `name` is used to identify the `AdBreak` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### updateAdBreak(UpdateAdBreakRequest request)
    
    
    public final AdBreak updateAdBreak(UpdateAdBreakRequest request)

Updates an `AdBreak` object.

Modify an ad break when its state is `SCHEDULED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       UpdateAdBreakRequest request =
           UpdateAdBreakRequest.newBuilder()
               .setAdBreak(AdBreak.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       AdBreak response = adBreakServiceClient.updateAdBreak(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdBreakRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)` |   
  
### updateAdBreakCallable()
    
    
    public final UnaryCallable<UpdateAdBreakRequest,AdBreak> updateAdBreakCallable()

Updates an `AdBreak` object.

Modify an ad break when its state is `SCHEDULED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AdBreakServiceClient adBreakServiceClient = AdBreakServiceClient.create()) {
       UpdateAdBreakRequest request =
           UpdateAdBreakRequest.newBuilder()
               .setAdBreak(AdBreak.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<AdBreak> future = adBreakServiceClient.updateAdBreakCallable().futureCall(request);
       // Do something.
       AdBreak response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAdBreakRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateAdBreakRequest),[AdBreak](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdBreak)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
