---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient
title: Class LiveStreamServiceClient (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:08:51.162837+00:00
---

# Class LiveStreamServiceClient (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LiveStreamServiceClient (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-admanager/ad-manager/src/main/java/com/google/ads/admanager/v1/LiveStreamServiceClient.java)| [Product Reference](https://developers.google.com/ad-manager/api/beta)  
---|---  
  
Service Description: Provides methods for handling `LiveStream` objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       LiveStreamName name = LiveStreamName.of("[NETWORK_CODE]", "[LIVE_STREAM]");
       LiveStream response = liveStreamServiceClient.getLiveStream(name);
     }
     

Note: close() needs to be called on the LiveStreamServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetLiveStream |  Retrieves a `LiveStream` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLiveStream(GetLiveStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLiveStream(LiveStreamName name) 
  * getLiveStream(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLiveStreamCallable() 

  
ListLiveStreams |  Lists `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLiveStreams(ListLiveStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLiveStreams(NetworkName parent) 
  * listLiveStreams(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLiveStreamsPagedCallable() 
  * listLiveStreamsCallable() 

  
CreateLiveStream |  Creates a `LiveStream` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLiveStream(CreateLiveStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createLiveStream(NetworkName parent, LiveStream liveStream) 
  * createLiveStream(String parent, LiveStream liveStream) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLiveStreamCallable() 

  
BatchCreateLiveStreams |  Batch creates `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateLiveStreams(NetworkName parent, List<CreateLiveStreamRequest> requests) 
  * batchCreateLiveStreams(String parent, List<CreateLiveStreamRequest> requests) 
  * batchCreateLiveStreams(BatchCreateLiveStreamsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateLiveStreamsCallable() 

  
UpdateLiveStream |  Updates a `LiveStream` object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLiveStream(UpdateLiveStreamRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateLiveStream(LiveStream liveStream, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLiveStreamCallable() 

  
BatchUpdateLiveStreams |  Batch updates `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateLiveStreams(NetworkName parent, List<UpdateLiveStreamRequest> requests) 
  * batchUpdateLiveStreams(String parent, List<UpdateLiveStreamRequest> requests) 
  * batchUpdateLiveStreams(BatchUpdateLiveStreamsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateLiveStreamsCallable() 

  
BatchActivateLiveStreams |  Batch activates `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchActivateLiveStreams(BatchActivateLiveStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchActivateLiveStreams(NetworkName parent, List<String> names) 
  * batchActivateLiveStreams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchActivateLiveStreamsCallable() 

  
BatchPauseLiveStreams |  Batch pauses `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchPauseLiveStreams(BatchPauseLiveStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchPauseLiveStreams(NetworkName parent, List<String> names) 
  * batchPauseLiveStreams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchPauseLiveStreamsCallable() 

  
BatchArchiveLiveStreams |  Batch archives `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchArchiveLiveStreams(BatchArchiveLiveStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchArchiveLiveStreams(NetworkName parent, List<String> names) 
  * batchArchiveLiveStreams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchArchiveLiveStreamsCallable() 

  
BatchPauseAdsLiveStreams |  Batch pauses ads on `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchPauseAdsLiveStreams(BatchPauseAdsLiveStreamsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchPauseAdsLiveStreams(NetworkName parent, List<String> names) 
  * batchPauseAdsLiveStreams(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchPauseAdsLiveStreamsCallable() 

  
BatchRefreshMasterPlaylists |  Batch refreshes master playlists on `LiveStream` objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchRefreshMasterPlaylists(BatchRefreshMasterPlaylistsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * batchRefreshMasterPlaylists(NetworkName parent, List<String> names) 
  * batchRefreshMasterPlaylists(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchRefreshMasterPlaylistsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of LiveStreamServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LiveStreamServiceSettings liveStreamServiceSettings =
         LiveStreamServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     LiveStreamServiceClient liveStreamServiceClient =
         LiveStreamServiceClient.create(liveStreamServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LiveStreamServiceSettings liveStreamServiceSettings =
         LiveStreamServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     LiveStreamServiceClient liveStreamServiceClient =
         LiveStreamServiceClient.create(liveStreamServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LiveStreamServiceClient

## Static Methods 

### create()
    
    
    public static final LiveStreamServiceClient create()

Constructs an instance of LiveStreamServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LiveStreamServiceSettings settings)
    
    
    public static final LiveStreamServiceClient create(LiveStreamServiceSettings settings)

Constructs an instance of LiveStreamServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LiveStreamServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(LiveStreamServiceStub stub)
    
    
    public static final LiveStreamServiceClient create(LiveStreamServiceStub stub)

Constructs an instance of LiveStreamServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(LiveStreamServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LiveStreamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LiveStreamServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient)` |   
  
## Constructors 

### LiveStreamServiceClient(LiveStreamServiceSettings settings)
    
    
    protected LiveStreamServiceClient(LiveStreamServiceSettings settings)

Constructs an instance of LiveStreamServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[LiveStreamServiceSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceSettings)`  
  
  
### LiveStreamServiceClient(LiveStreamServiceStub stub)
    
    
    protected LiveStreamServiceClient(LiveStreamServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LiveStreamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LiveStreamServiceStub)`  
  
  
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
  
### batchActivateLiveStreams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchActivateLiveStreamsResponse batchActivateLiveStreams(@Nullable NetworkName parent, List<String> names)

Batch activates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchActivateLiveStreamsResponse response =
           liveStreamServiceClient.batchActivateLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to activate. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsResponse)` |   
  
### batchActivateLiveStreams(BatchActivateLiveStreamsRequest request)
    
    
    public final BatchActivateLiveStreamsResponse batchActivateLiveStreams(BatchActivateLiveStreamsRequest request)

Batch activates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchActivateLiveStreamsRequest request =
           BatchActivateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchActivateLiveStreamsResponse response =
           liveStreamServiceClient.batchActivateLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchActivateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsResponse)` |   
  
### batchActivateLiveStreams(String parent, List<String> names)
    
    
    public final BatchActivateLiveStreamsResponse batchActivateLiveStreams(String parent, List<String> names)

Batch activates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchActivateLiveStreamsResponse response =
           liveStreamServiceClient.batchActivateLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to activate. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsResponse)` |   
  
### batchActivateLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchActivateLiveStreamsRequest,BatchActivateLiveStreamsResponse> batchActivateLiveStreamsCallable()

Batch activates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchActivateLiveStreamsRequest request =
           BatchActivateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchActivateLiveStreamsResponse> future =
           liveStreamServiceClient.batchActivateLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchActivateLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchActivateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsRequest),[BatchActivateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchActivateLiveStreamsResponse)>` |   
  
### batchArchiveLiveStreams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchArchiveLiveStreamsResponse batchArchiveLiveStreams(@Nullable NetworkName parent, List<String> names)

Batch archives `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchArchiveLiveStreamsResponse response =
           liveStreamServiceClient.batchArchiveLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to archive. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsResponse)` |   
  
### batchArchiveLiveStreams(BatchArchiveLiveStreamsRequest request)
    
    
    public final BatchArchiveLiveStreamsResponse batchArchiveLiveStreams(BatchArchiveLiveStreamsRequest request)

Batch archives `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchArchiveLiveStreamsRequest request =
           BatchArchiveLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchArchiveLiveStreamsResponse response =
           liveStreamServiceClient.batchArchiveLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchArchiveLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsResponse)` |   
  
### batchArchiveLiveStreams(String parent, List<String> names)
    
    
    public final BatchArchiveLiveStreamsResponse batchArchiveLiveStreams(String parent, List<String> names)

Batch archives `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchArchiveLiveStreamsResponse response =
           liveStreamServiceClient.batchArchiveLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to archive. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchArchiveLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsResponse)` |   
  
### batchArchiveLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchArchiveLiveStreamsRequest,BatchArchiveLiveStreamsResponse> batchArchiveLiveStreamsCallable()

Batch archives `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchArchiveLiveStreamsRequest request =
           BatchArchiveLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchArchiveLiveStreamsResponse> future =
           liveStreamServiceClient.batchArchiveLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchArchiveLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchArchiveLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsRequest),[BatchArchiveLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchArchiveLiveStreamsResponse)>` |   
  
### batchCreateLiveStreams(@Nullable NetworkName parent, List<CreateLiveStreamRequest> requests)
    
    
    public final BatchCreateLiveStreamsResponse batchCreateLiveStreams(@Nullable NetworkName parent, List<CreateLiveStreamRequest> requests)

Batch creates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<CreateLiveStreamRequest> requests = new ArrayList<>();
       BatchCreateLiveStreamsResponse response =
           liveStreamServiceClient.batchCreateLiveStreams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `LiveStreams` will be created. Format: `networks/{network_code}` The parent field in the CreateLiveStreamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLiveStreamRequest)>`  
Required. The `LiveStream` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsResponse)` |   
  
### batchCreateLiveStreams(BatchCreateLiveStreamsRequest request)
    
    
    public final BatchCreateLiveStreamsResponse batchCreateLiveStreams(BatchCreateLiveStreamsRequest request)

Batch creates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchCreateLiveStreamsRequest request =
           BatchCreateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateLiveStreamRequest>())
               .build();
       BatchCreateLiveStreamsResponse response =
           liveStreamServiceClient.batchCreateLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsResponse)` |   
  
### batchCreateLiveStreams(String parent, List<CreateLiveStreamRequest> requests)
    
    
    public final BatchCreateLiveStreamsResponse batchCreateLiveStreams(String parent, List<CreateLiveStreamRequest> requests)

Batch creates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<CreateLiveStreamRequest> requests = new ArrayList<>();
       BatchCreateLiveStreamsResponse response =
           liveStreamServiceClient.batchCreateLiveStreams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `LiveStreams` will be created. Format: `networks/{network_code}` The parent field in the CreateLiveStreamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CreateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLiveStreamRequest)>`  
Required. The `LiveStream` objects to create. A maximum of 100 objects can be created in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsResponse)` |   
  
### batchCreateLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchCreateLiveStreamsRequest,BatchCreateLiveStreamsResponse> batchCreateLiveStreamsCallable()

Batch creates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchCreateLiveStreamsRequest request =
           BatchCreateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<CreateLiveStreamRequest>())
               .build();
       ApiFuture<BatchCreateLiveStreamsResponse> future =
           liveStreamServiceClient.batchCreateLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchCreateLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsRequest),[BatchCreateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchCreateLiveStreamsResponse)>` |   
  
### batchPauseAdsLiveStreams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchPauseAdsLiveStreamsResponse batchPauseAdsLiveStreams(@Nullable NetworkName parent, List<String> names)

Batch pauses ads on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchPauseAdsLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseAdsLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to pause ads on. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseAdsLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsResponse)` |   
  
### batchPauseAdsLiveStreams(BatchPauseAdsLiveStreamsRequest request)
    
    
    public final BatchPauseAdsLiveStreamsResponse batchPauseAdsLiveStreams(BatchPauseAdsLiveStreamsRequest request)

Batch pauses ads on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchPauseAdsLiveStreamsRequest request =
           BatchPauseAdsLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchPauseAdsLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseAdsLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchPauseAdsLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseAdsLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsResponse)` |   
  
### batchPauseAdsLiveStreams(String parent, List<String> names)
    
    
    public final BatchPauseAdsLiveStreamsResponse batchPauseAdsLiveStreams(String parent, List<String> names)

Batch pauses ads on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchPauseAdsLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseAdsLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to pause ads on. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseAdsLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsResponse)` |   
  
### batchPauseAdsLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchPauseAdsLiveStreamsRequest,BatchPauseAdsLiveStreamsResponse> batchPauseAdsLiveStreamsCallable()

Batch pauses ads on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchPauseAdsLiveStreamsRequest request =
           BatchPauseAdsLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchPauseAdsLiveStreamsResponse> future =
           liveStreamServiceClient.batchPauseAdsLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchPauseAdsLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPauseAdsLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsRequest),[BatchPauseAdsLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseAdsLiveStreamsResponse)>` |   
  
### batchPauseLiveStreams(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchPauseLiveStreamsResponse batchPauseLiveStreams(@Nullable NetworkName parent, List<String> names)

Batch pauses `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchPauseLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to pause. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsResponse)` |   
  
### batchPauseLiveStreams(BatchPauseLiveStreamsRequest request)
    
    
    public final BatchPauseLiveStreamsResponse batchPauseLiveStreams(BatchPauseLiveStreamsRequest request)

Batch pauses `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchPauseLiveStreamsRequest request =
           BatchPauseLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchPauseLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchPauseLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsResponse)` |   
  
### batchPauseLiveStreams(String parent, List<String> names)
    
    
    public final BatchPauseLiveStreamsResponse batchPauseLiveStreams(String parent, List<String> names)

Batch pauses `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchPauseLiveStreamsResponse response =
           liveStreamServiceClient.batchPauseLiveStreams(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to pause. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchPauseLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsResponse)` |   
  
### batchPauseLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchPauseLiveStreamsRequest,BatchPauseLiveStreamsResponse> batchPauseLiveStreamsCallable()

Batch pauses `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchPauseLiveStreamsRequest request =
           BatchPauseLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchPauseLiveStreamsResponse> future =
           liveStreamServiceClient.batchPauseLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchPauseLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchPauseLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsRequest),[BatchPauseLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchPauseLiveStreamsResponse)>` |   
  
### batchRefreshMasterPlaylists(@Nullable NetworkName parent, List<String> names)
    
    
    public final BatchRefreshMasterPlaylistsResponse batchRefreshMasterPlaylists(@Nullable NetworkName parent, List<String> names)

Batch refreshes master playlists on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<String> names = new ArrayList<>();
       BatchRefreshMasterPlaylistsResponse response =
           liveStreamServiceClient.batchRefreshMasterPlaylists(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to refresh master playlists on. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRefreshMasterPlaylistsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsResponse)` |   
  
### batchRefreshMasterPlaylists(BatchRefreshMasterPlaylistsRequest request)
    
    
    public final BatchRefreshMasterPlaylistsResponse batchRefreshMasterPlaylists(BatchRefreshMasterPlaylistsRequest request)

Batch refreshes master playlists on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchRefreshMasterPlaylistsRequest request =
           BatchRefreshMasterPlaylistsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchRefreshMasterPlaylistsResponse response =
           liveStreamServiceClient.batchRefreshMasterPlaylists(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchRefreshMasterPlaylistsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchRefreshMasterPlaylistsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsResponse)` |   
  
### batchRefreshMasterPlaylists(String parent, List<String> names)
    
    
    public final BatchRefreshMasterPlaylistsResponse batchRefreshMasterPlaylists(String parent, List<String> names)

Batch refreshes master playlists on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<String> names = new ArrayList<>();
       BatchRefreshMasterPlaylistsResponse response =
           liveStreamServiceClient.batchRefreshMasterPlaylists(parent, names);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: `networks/{network_code}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The resource names of the `LiveStream`s to refresh master playlists on. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[BatchRefreshMasterPlaylistsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsResponse)` |   
  
### batchRefreshMasterPlaylistsCallable()
    
    
    public final UnaryCallable<BatchRefreshMasterPlaylistsRequest,BatchRefreshMasterPlaylistsResponse> batchRefreshMasterPlaylistsCallable()

Batch refreshes master playlists on `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchRefreshMasterPlaylistsRequest request =
           BatchRefreshMasterPlaylistsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<BatchRefreshMasterPlaylistsResponse> future =
           liveStreamServiceClient.batchRefreshMasterPlaylistsCallable().futureCall(request);
       // Do something.
       BatchRefreshMasterPlaylistsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchRefreshMasterPlaylistsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsRequest),[BatchRefreshMasterPlaylistsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchRefreshMasterPlaylistsResponse)>` |   
  
### batchUpdateLiveStreams(@Nullable NetworkName parent, List<UpdateLiveStreamRequest> requests)
    
    
    public final BatchUpdateLiveStreamsResponse batchUpdateLiveStreams(@Nullable NetworkName parent, List<UpdateLiveStreamRequest> requests)

Batch updates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       List<UpdateLiveStreamRequest> requests = new ArrayList<>();
       BatchUpdateLiveStreamsResponse response =
           liveStreamServiceClient.batchUpdateLiveStreams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where `LiveStreams` will be updated. Format: `networks/{network_code}` The parent field in the UpdateLiveStreamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLiveStreamRequest)>`  
Required. The `LiveStream` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsResponse)` |   
  
### batchUpdateLiveStreams(BatchUpdateLiveStreamsRequest request)
    
    
    public final BatchUpdateLiveStreamsResponse batchUpdateLiveStreams(BatchUpdateLiveStreamsRequest request)

Batch updates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchUpdateLiveStreamsRequest request =
           BatchUpdateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateLiveStreamRequest>())
               .build();
       BatchUpdateLiveStreamsResponse response =
           liveStreamServiceClient.batchUpdateLiveStreams(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsResponse)` |   
  
### batchUpdateLiveStreams(String parent, List<UpdateLiveStreamRequest> requests)
    
    
    public final BatchUpdateLiveStreamsResponse batchUpdateLiveStreams(String parent, List<UpdateLiveStreamRequest> requests)

Batch updates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       List<UpdateLiveStreamRequest> requests = new ArrayList<>();
       BatchUpdateLiveStreamsResponse response =
           liveStreamServiceClient.batchUpdateLiveStreams(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where `LiveStreams` will be updated. Format: `networks/{network_code}` The parent field in the UpdateLiveStreamRequest must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLiveStreamRequest)>`  
Required. The `LiveStream` objects to update. A maximum of 100 objects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsResponse)` |   
  
### batchUpdateLiveStreamsCallable()
    
    
    public final UnaryCallable<BatchUpdateLiveStreamsRequest,BatchUpdateLiveStreamsResponse> batchUpdateLiveStreamsCallable()

Batch updates `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       BatchUpdateLiveStreamsRequest request =
           BatchUpdateLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .addAllRequests(new ArrayList<UpdateLiveStreamRequest>())
               .build();
       ApiFuture<BatchUpdateLiveStreamsResponse> future =
           liveStreamServiceClient.batchUpdateLiveStreamsCallable().futureCall(request);
       // Do something.
       BatchUpdateLiveStreamsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsRequest),[BatchUpdateLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.BatchUpdateLiveStreamsResponse)>` |   
  
### close()
    
    
    public final void close()

### createLiveStream(@Nullable NetworkName parent, LiveStream liveStream)
    
    
    public final LiveStream createLiveStream(@Nullable NetworkName parent, LiveStream liveStream)

Creates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       LiveStream liveStream = LiveStream.newBuilder().build();
       LiveStream response = liveStreamServiceClient.createLiveStream(parent, liveStream);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent resource where this `LiveStream` will be created. Format: `networks/{network_code}`  
`liveStream` | `[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)`  
Required. The `LiveStream` to create.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### createLiveStream(CreateLiveStreamRequest request)
    
    
    public final LiveStream createLiveStream(CreateLiveStreamRequest request)

Creates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       CreateLiveStreamRequest request =
           CreateLiveStreamRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setLiveStream(LiveStream.newBuilder().build())
               .build();
       LiveStream response = liveStreamServiceClient.createLiveStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLiveStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### createLiveStream(String parent, LiveStream liveStream)
    
    
    public final LiveStream createLiveStream(String parent, LiveStream liveStream)

Creates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       LiveStream liveStream = LiveStream.newBuilder().build();
       LiveStream response = liveStreamServiceClient.createLiveStream(parent, liveStream);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this `LiveStream` will be created. Format: `networks/{network_code}`  
`liveStream` | `[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)`  
Required. The `LiveStream` to create.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### createLiveStreamCallable()
    
    
    public final UnaryCallable<CreateLiveStreamRequest,LiveStream> createLiveStreamCallable()

Creates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       CreateLiveStreamRequest request =
           CreateLiveStreamRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setLiveStream(LiveStream.newBuilder().build())
               .build();
       ApiFuture<LiveStream> future =
           liveStreamServiceClient.createLiveStreamCallable().futureCall(request);
       // Do something.
       LiveStream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CreateLiveStreamRequest),[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)>` |   
  
### getLiveStream(@Nullable LiveStreamName name)
    
    
    public final LiveStream getLiveStream(@Nullable LiveStreamName name)

Retrieves a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       LiveStreamName name = LiveStreamName.of("[NETWORK_CODE]", "[LIVE_STREAM]");
       LiveStream response = liveStreamServiceClient.getLiveStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LiveStreamName`  
Required. The resource name of the LiveStream. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### getLiveStream(GetLiveStreamRequest request)
    
    
    public final LiveStream getLiveStream(GetLiveStreamRequest request)

Retrieves a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       GetLiveStreamRequest request =
           GetLiveStreamRequest.newBuilder()
               .setName(LiveStreamName.of("[NETWORK_CODE]", "[LIVE_STREAM]").toString())
               .build();
       LiveStream response = liveStreamServiceClient.getLiveStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLiveStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### getLiveStream(String name)
    
    
    public final LiveStream getLiveStream(String name)

Retrieves a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String name = LiveStreamName.of("[NETWORK_CODE]", "[LIVE_STREAM]").toString();
       LiveStream response = liveStreamServiceClient.getLiveStream(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the LiveStream. Format: `networks/{network_code}/liveStreams/{live_stream_id}`  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### getLiveStreamCallable()
    
    
    public final UnaryCallable<GetLiveStreamRequest,LiveStream> getLiveStreamCallable()

Retrieves a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       GetLiveStreamRequest request =
           GetLiveStreamRequest.newBuilder()
               .setName(LiveStreamName.of("[NETWORK_CODE]", "[LIVE_STREAM]").toString())
               .build();
       ApiFuture<LiveStream> future =
           liveStreamServiceClient.getLiveStreamCallable().futureCall(request);
       // Do something.
       LiveStream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.GetLiveStreamRequest),[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)>` |   
  
### getSettings()
    
    
    public final @Nullable LiveStreamServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.LiveStreamServiceSettings` |   
  
### getStub()
    
    
    public LiveStreamServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceStub](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.stub.LiveStreamServiceStub)` |   
  
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
  
### listLiveStreams(@Nullable NetworkName parent)
    
    
    public final LiveStreamServiceClient.ListLiveStreamsPagedResponse listLiveStreams(@Nullable NetworkName parent)

Lists `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       NetworkName parent = NetworkName.of("[NETWORK_CODE]");
       for (LiveStream element : liveStreamServiceClient.listLiveStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.ads.admanager.v1.NetworkName`  
Required. The parent, which owns this collection of LiveStreams. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient.ListLiveStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient.ListLiveStreamsPagedResponse)` |   
  
### listLiveStreams(ListLiveStreamsRequest request)
    
    
    public final LiveStreamServiceClient.ListLiveStreamsPagedResponse listLiveStreams(ListLiveStreamsRequest request)

Lists `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       ListLiveStreamsRequest request =
           ListLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       for (LiveStream element : liveStreamServiceClient.listLiveStreams(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLiveStreamsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient.ListLiveStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient.ListLiveStreamsPagedResponse)` |   
  
### listLiveStreams(String parent)
    
    
    public final LiveStreamServiceClient.ListLiveStreamsPagedResponse listLiveStreams(String parent)

Lists `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       String parent = NetworkName.of("[NETWORK_CODE]").toString();
       for (LiveStream element : liveStreamServiceClient.listLiveStreams(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which owns this collection of LiveStreams. Format: `networks/{network_code}`  
**Returns**  
---  
**Type** | **Description**  
`[LiveStreamServiceClient.ListLiveStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient.ListLiveStreamsPagedResponse)` |   
  
### listLiveStreamsCallable()
    
    
    public final UnaryCallable<ListLiveStreamsRequest,ListLiveStreamsResponse> listLiveStreamsCallable()

Lists `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       ListLiveStreamsRequest request =
           ListLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       while (true) {
         ListLiveStreamsResponse response =
             liveStreamServiceClient.listLiveStreamsCallable().call(request);
         for (LiveStream element : response.getLiveStreamsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLiveStreamsRequest),[ListLiveStreamsResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLiveStreamsResponse)>` |   
  
### listLiveStreamsPagedCallable()
    
    
    public final UnaryCallable<ListLiveStreamsRequest,LiveStreamServiceClient.ListLiveStreamsPagedResponse> listLiveStreamsPagedCallable()

Lists `LiveStream` objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       ListLiveStreamsRequest request =
           ListLiveStreamsRequest.newBuilder()
               .setParent(NetworkName.of("[NETWORK_CODE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setSkip(3532159)
               .build();
       ApiFuture<LiveStream> future =
           liveStreamServiceClient.listLiveStreamsPagedCallable().futureCall(request);
       // Do something.
       for (LiveStream element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveStreamsRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListLiveStreamsRequest),[ListLiveStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStreamServiceClient.ListLiveStreamsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateLiveStream(LiveStream liveStream, FieldMask updateMask)
    
    
    public final LiveStream updateLiveStream(LiveStream liveStream, FieldMask updateMask)

Updates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       LiveStream liveStream = LiveStream.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LiveStream response = liveStreamServiceClient.updateLiveStream(liveStream, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`liveStream` | `[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)`  
Required. The `LiveStream` to update. The `LiveStream`'s `name` is used to identify the `LiveStream` to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### updateLiveStream(UpdateLiveStreamRequest request)
    
    
    public final LiveStream updateLiveStream(UpdateLiveStreamRequest request)

Updates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       UpdateLiveStreamRequest request =
           UpdateLiveStreamRequest.newBuilder()
               .setLiveStream(LiveStream.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LiveStream response = liveStreamServiceClient.updateLiveStream(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLiveStreamRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)` |   
  
### updateLiveStreamCallable()
    
    
    public final UnaryCallable<UpdateLiveStreamRequest,LiveStream> updateLiveStreamCallable()

Updates a `LiveStream` object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (LiveStreamServiceClient liveStreamServiceClient = LiveStreamServiceClient.create()) {
       UpdateLiveStreamRequest request =
           UpdateLiveStreamRequest.newBuilder()
               .setLiveStream(LiveStream.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<LiveStream> future =
           liveStreamServiceClient.updateLiveStreamCallable().futureCall(request);
       // Do something.
       LiveStream response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLiveStreamRequest](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.UpdateLiveStreamRequest),[LiveStream](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.LiveStream)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
