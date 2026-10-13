---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient
title: Class VideoStitcherServiceClient (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:41.147284+00:00
---

# Class VideoStitcherServiceClient (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VideoStitcherServiceClient (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6  0.1.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-video-stitcher/google-cloud-video-stitcher/src/main/java/com/google/cloud/video/stitcher/v1/VideoStitcherServiceClient.java)| [Product Reference](https://cloud.google.com/video-stitcher/)  
---|---  
  
Service Description: Video-On-Demand content stitching API allows you to insert ads into (VoD) video on demand files. You will be able to render custom scrubber bars with highlighted ads, enforce ad policies, allow seamless playback and tracking on native players and monetize content with any standard VMAP compliant ad server.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CdnKeyName name = CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]");
       CdnKey response = videoStitcherServiceClient.getCdnKey(name);
     }
     

Note: close() needs to be called on the VideoStitcherServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateCdnKey |  Creates a new CDN key. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCdnKeyAsync(CreateCdnKeyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCdnKeyAsync(LocationName parent, CdnKey cdnKey, String cdnKeyId) 
  * createCdnKeyAsync(String parent, CdnKey cdnKey, String cdnKeyId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCdnKeyOperationCallable() 
  * createCdnKeyCallable() 

  
ListCdnKeys |  Lists all CDN keys in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCdnKeys(ListCdnKeysRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCdnKeys(LocationName parent) 
  * listCdnKeys(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCdnKeysPagedCallable() 
  * listCdnKeysCallable() 

  
GetCdnKey |  Returns the specified CDN key. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCdnKey(GetCdnKeyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCdnKey(CdnKeyName name) 
  * getCdnKey(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCdnKeyCallable() 

  
DeleteCdnKey |  Deletes the specified CDN key. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCdnKeyAsync(DeleteCdnKeyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCdnKeyAsync(CdnKeyName name) 
  * deleteCdnKeyAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCdnKeyOperationCallable() 
  * deleteCdnKeyCallable() 

  
UpdateCdnKey |  Updates the specified CDN key. Only update fields specified in the call method body. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCdnKeyAsync(UpdateCdnKeyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateCdnKeyAsync(CdnKey cdnKey, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCdnKeyOperationCallable() 
  * updateCdnKeyCallable() 

  
CreateVodSession |  Creates a client side playback VOD session and returns the full tracking and playback metadata of the session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createVodSession(CreateVodSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createVodSession(LocationName parent, VodSession vodSession) 
  * createVodSession(String parent, VodSession vodSession) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createVodSessionCallable() 

  
GetVodSession |  Returns the full tracking, playback metadata, and relevant ad-ops logs for the specified VOD session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVodSession(GetVodSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVodSession(VodSessionName name) 
  * getVodSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVodSessionCallable() 

  
ListVodStitchDetails |  Returns a list of detailed stitching information of the specified VOD session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVodStitchDetails(ListVodStitchDetailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVodStitchDetails(VodSessionName parent) 
  * listVodStitchDetails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVodStitchDetailsPagedCallable() 
  * listVodStitchDetailsCallable() 

  
GetVodStitchDetail |  Returns the specified stitching information for the specified VOD session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVodStitchDetail(GetVodStitchDetailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVodStitchDetail(VodStitchDetailName name) 
  * getVodStitchDetail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVodStitchDetailCallable() 

  
ListVodAdTagDetails |  Return the list of ad tag details for the specified VOD session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVodAdTagDetails(ListVodAdTagDetailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVodAdTagDetails(VodSessionName parent) 
  * listVodAdTagDetails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVodAdTagDetailsPagedCallable() 
  * listVodAdTagDetailsCallable() 

  
GetVodAdTagDetail |  Returns the specified ad tag detail for the specified VOD session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVodAdTagDetail(GetVodAdTagDetailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVodAdTagDetail(VodAdTagDetailName name) 
  * getVodAdTagDetail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVodAdTagDetailCallable() 

  
ListLiveAdTagDetails |  Return the list of ad tag details for the specified live session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLiveAdTagDetails(ListLiveAdTagDetailsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLiveAdTagDetails(LiveSessionName parent) 
  * listLiveAdTagDetails(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLiveAdTagDetailsPagedCallable() 
  * listLiveAdTagDetailsCallable() 

  
GetLiveAdTagDetail |  Returns the specified ad tag detail for the specified live session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLiveAdTagDetail(GetLiveAdTagDetailRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLiveAdTagDetail(LiveAdTagDetailName name) 
  * getLiveAdTagDetail(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLiveAdTagDetailCallable() 

  
CreateSlate |  Creates a slate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSlateAsync(CreateSlateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSlateAsync(LocationName parent, Slate slate, String slateId) 
  * createSlateAsync(String parent, Slate slate, String slateId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSlateOperationCallable() 
  * createSlateCallable() 

  
ListSlates |  Lists all slates in the specified project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSlates(ListSlatesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSlates(LocationName parent) 
  * listSlates(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSlatesPagedCallable() 
  * listSlatesCallable() 

  
GetSlate |  Returns the specified slate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSlate(GetSlateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSlate(SlateName name) 
  * getSlate(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSlateCallable() 

  
UpdateSlate |  Updates the specified slate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSlateAsync(UpdateSlateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSlateAsync(Slate slate, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSlateOperationCallable() 
  * updateSlateCallable() 

  
DeleteSlate |  Deletes the specified slate. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSlateAsync(DeleteSlateRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSlateAsync(SlateName name) 
  * deleteSlateAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSlateOperationCallable() 
  * deleteSlateCallable() 

  
CreateLiveSession |  Creates a new live session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLiveSession(CreateLiveSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createLiveSession(LocationName parent, LiveSession liveSession) 
  * createLiveSession(String parent, LiveSession liveSession) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLiveSessionCallable() 

  
GetLiveSession |  Returns the details for the specified live session. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLiveSession(GetLiveSessionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLiveSession(LiveSessionName name) 
  * getLiveSession(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLiveSessionCallable() 

  
CreateLiveConfig |  Registers the live config with the provided unique ID in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLiveConfigAsync(CreateLiveConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLiveConfigAsync(LocationName parent, LiveConfig liveConfig, String liveConfigId) 
  * createLiveConfigAsync(String parent, LiveConfig liveConfig, String liveConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLiveConfigOperationCallable() 
  * createLiveConfigCallable() 

  
ListLiveConfigs |  Lists all live configs managed by the Video Stitcher that belong to the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLiveConfigs(ListLiveConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLiveConfigs(LocationName parent) 
  * listLiveConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLiveConfigsPagedCallable() 
  * listLiveConfigsCallable() 

  
GetLiveConfig |  Returns the specified live config managed by the Video Stitcher service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLiveConfig(GetLiveConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLiveConfig(LiveConfigName name) 
  * getLiveConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLiveConfigCallable() 

  
DeleteLiveConfig |  Deletes the specified live config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLiveConfigAsync(DeleteLiveConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLiveConfigAsync(LiveConfigName name) 
  * deleteLiveConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLiveConfigOperationCallable() 
  * deleteLiveConfigCallable() 

  
UpdateLiveConfig |  Updates the specified LiveConfig. Only update fields specified in the call method body. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLiveConfigAsync(UpdateLiveConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLiveConfigAsync(LiveConfig liveConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLiveConfigOperationCallable() 
  * updateLiveConfigCallable() 

  
CreateVodConfig |  Registers the VOD config with the provided unique ID in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createVodConfigAsync(CreateVodConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createVodConfigAsync(LocationName parent, VodConfig vodConfig, String vodConfigId) 
  * createVodConfigAsync(String parent, VodConfig vodConfig, String vodConfigId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createVodConfigOperationCallable() 
  * createVodConfigCallable() 

  
ListVodConfigs |  Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listVodConfigs(ListVodConfigsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listVodConfigs(LocationName parent) 
  * listVodConfigs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listVodConfigsPagedCallable() 
  * listVodConfigsCallable() 

  
GetVodConfig |  Returns the specified VOD config managed by the Video Stitcher API service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVodConfig(GetVodConfigRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getVodConfig(VodConfigName name) 
  * getVodConfig(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVodConfigCallable() 

  
DeleteVodConfig |  Deletes the specified VOD config. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteVodConfigAsync(DeleteVodConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteVodConfigAsync(VodConfigName name) 
  * deleteVodConfigAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteVodConfigOperationCallable() 
  * deleteVodConfigCallable() 

  
UpdateVodConfig |  Updates the specified VOD config. Only update fields specified in the call method body. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateVodConfigAsync(UpdateVodConfigRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateVodConfigAsync(VodConfig vodConfig, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateVodConfigOperationCallable() 
  * updateVodConfigCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of VideoStitcherServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoStitcherServiceSettings videoStitcherServiceSettings =
         VideoStitcherServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create(videoStitcherServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoStitcherServiceSettings videoStitcherServiceSettings =
         VideoStitcherServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create(videoStitcherServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VideoStitcherServiceClient

## Static Methods 

### create()
    
    
    public static final VideoStitcherServiceClient create()

Constructs an instance of VideoStitcherServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VideoStitcherServiceSettings settings)
    
    
    public static final VideoStitcherServiceClient create(VideoStitcherServiceSettings settings)

Constructs an instance of VideoStitcherServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VideoStitcherServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VideoStitcherServiceStub stub)
    
    
    public static final VideoStitcherServiceClient create(VideoStitcherServiceStub stub)

Constructs an instance of VideoStitcherServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VideoStitcherServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VideoStitcherServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient)` |   
  
## Constructors 

### VideoStitcherServiceClient(VideoStitcherServiceSettings settings)
    
    
    protected VideoStitcherServiceClient(VideoStitcherServiceSettings settings)

Constructs an instance of VideoStitcherServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VideoStitcherServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings)`  
  
  
### VideoStitcherServiceClient(VideoStitcherServiceStub stub)
    
    
    protected VideoStitcherServiceClient(VideoStitcherServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VideoStitcherServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStub)`  
  
  
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

### createCdnKeyAsync(@Nullable LocationName parent, CdnKey cdnKey, String cdnKeyId)
    
    
    public final OperationFuture<CdnKey,OperationMetadata> createCdnKeyAsync(@Nullable LocationName parent, CdnKey cdnKey, String cdnKeyId)

Creates a new CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       CdnKey cdnKey = CdnKey.newBuilder().build();
       String cdnKeyId = "cdnKeyId-1777782867";
       CdnKey response =
           videoStitcherServiceClient.createCdnKeyAsync(parent, cdnKey, cdnKeyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project in which the CDN key should be created, in the form of `projects/{project_number}/locations/{location}`.  
`cdnKey` | `[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)`  
Required. The CDN key resource to create.  
`cdnKeyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the CDN key, which will become the final component of the CDN key's resource name. This value should conform to RFC-1034, which restricts to lower-case letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createCdnKeyAsync(CreateCdnKeyRequest request)
    
    
    public final OperationFuture<CdnKey,OperationMetadata> createCdnKeyAsync(CreateCdnKeyRequest request)

Creates a new CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateCdnKeyRequest request =
           CreateCdnKeyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCdnKey(CdnKey.newBuilder().build())
               .setCdnKeyId("cdnKeyId-1777782867")
               .build();
       CdnKey response = videoStitcherServiceClient.createCdnKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createCdnKeyAsync(String parent, CdnKey cdnKey, String cdnKeyId)
    
    
    public final OperationFuture<CdnKey,OperationMetadata> createCdnKeyAsync(String parent, CdnKey cdnKey, String cdnKeyId)

Creates a new CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       CdnKey cdnKey = CdnKey.newBuilder().build();
       String cdnKeyId = "cdnKeyId-1777782867";
       CdnKey response =
           videoStitcherServiceClient.createCdnKeyAsync(parent, cdnKey, cdnKeyId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the CDN key should be created, in the form of `projects/{project_number}/locations/{location}`.  
`cdnKey` | `[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)`  
Required. The CDN key resource to create.  
`cdnKeyId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the CDN key, which will become the final component of the CDN key's resource name. This value should conform to RFC-1034, which restricts to lower-case letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createCdnKeyCallable()
    
    
    public final UnaryCallable<CreateCdnKeyRequest,Operation> createCdnKeyCallable()

Creates a new CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateCdnKeyRequest request =
           CreateCdnKeyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCdnKey(CdnKey.newBuilder().build())
               .setCdnKeyId("cdnKeyId-1777782867")
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.createCdnKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCdnKeyOperationCallable()
    
    
    public final OperationCallable<CreateCdnKeyRequest,CdnKey,OperationMetadata> createCdnKeyOperationCallable()

Creates a new CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateCdnKeyRequest request =
           CreateCdnKeyRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCdnKey(CdnKey.newBuilder().build())
               .setCdnKeyId("cdnKeyId-1777782867")
               .build();
       OperationFuture<CdnKey, OperationMetadata> future =
           videoStitcherServiceClient.createCdnKeyOperationCallable().futureCall(request);
       // Do something.
       CdnKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigAsync(@Nullable LocationName parent, LiveConfig liveConfig, String liveConfigId)
    
    
    public final OperationFuture<LiveConfig,OperationMetadata> createLiveConfigAsync(@Nullable LocationName parent, LiveConfig liveConfig, String liveConfigId)

Registers the live config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       LiveConfig liveConfig = LiveConfig.newBuilder().build();
       String liveConfigId = "liveConfigId1256140041";
       LiveConfig response =
           videoStitcherServiceClient.createLiveConfigAsync(parent, liveConfig, liveConfigId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project in which the live config should be created, in the form of `projects/{project_number}/locations/{location}`.  
`liveConfig` | `[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)`  
Required. The live config resource to create.  
`liveConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier ID to use for the live config.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigAsync(CreateLiveConfigRequest request)
    
    
    public final OperationFuture<LiveConfig,OperationMetadata> createLiveConfigAsync(CreateLiveConfigRequest request)

Registers the live config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateLiveConfigRequest request =
           CreateLiveConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLiveConfigId("liveConfigId1256140041")
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       LiveConfig response = videoStitcherServiceClient.createLiveConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigAsync(String parent, LiveConfig liveConfig, String liveConfigId)
    
    
    public final OperationFuture<LiveConfig,OperationMetadata> createLiveConfigAsync(String parent, LiveConfig liveConfig, String liveConfigId)

Registers the live config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       LiveConfig liveConfig = LiveConfig.newBuilder().build();
       String liveConfigId = "liveConfigId1256140041";
       LiveConfig response =
           videoStitcherServiceClient.createLiveConfigAsync(parent, liveConfig, liveConfigId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the live config should be created, in the form of `projects/{project_number}/locations/{location}`.  
`liveConfig` | `[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)`  
Required. The live config resource to create.  
`liveConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier ID to use for the live config.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigCallable()
    
    
    public final UnaryCallable<CreateLiveConfigRequest,Operation> createLiveConfigCallable()

Registers the live config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateLiveConfigRequest request =
           CreateLiveConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLiveConfigId("liveConfigId1256140041")
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.createLiveConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLiveConfigOperationCallable()
    
    
    public final OperationCallable<CreateLiveConfigRequest,LiveConfig,OperationMetadata> createLiveConfigOperationCallable()

Registers the live config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateLiveConfigRequest request =
           CreateLiveConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLiveConfigId("liveConfigId1256140041")
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<LiveConfig, OperationMetadata> future =
           videoStitcherServiceClient.createLiveConfigOperationCallable().futureCall(request);
       // Do something.
       LiveConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveSession(@Nullable LocationName parent, LiveSession liveSession)
    
    
    public final LiveSession createLiveSession(@Nullable LocationName parent, LiveSession liveSession)

Creates a new live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       LiveSession liveSession = LiveSession.newBuilder().build();
       LiveSession response = videoStitcherServiceClient.createLiveSession(parent, liveSession);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project and location in which the live session should be created, in the form of `projects/{project_number}/locations/{location}`.  
`liveSession` | `[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)`  
Required. Parameters for creating a live session.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### createLiveSession(CreateLiveSessionRequest request)
    
    
    public final LiveSession createLiveSession(CreateLiveSessionRequest request)

Creates a new live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateLiveSessionRequest request =
           CreateLiveSessionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLiveSession(LiveSession.newBuilder().build())
               .build();
       LiveSession response = videoStitcherServiceClient.createLiveSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### createLiveSession(String parent, LiveSession liveSession)
    
    
    public final LiveSession createLiveSession(String parent, LiveSession liveSession)

Creates a new live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       LiveSession liveSession = LiveSession.newBuilder().build();
       LiveSession response = videoStitcherServiceClient.createLiveSession(parent, liveSession);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location in which the live session should be created, in the form of `projects/{project_number}/locations/{location}`.  
`liveSession` | `[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)`  
Required. Parameters for creating a live session.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### createLiveSessionCallable()
    
    
    public final UnaryCallable<CreateLiveSessionRequest,LiveSession> createLiveSessionCallable()

Creates a new live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateLiveSessionRequest request =
           CreateLiveSessionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLiveSession(LiveSession.newBuilder().build())
               .build();
       ApiFuture<LiveSession> future =
           videoStitcherServiceClient.createLiveSessionCallable().futureCall(request);
       // Do something.
       LiveSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### createSlateAsync(@Nullable LocationName parent, Slate slate, String slateId)
    
    
    public final OperationFuture<Slate,OperationMetadata> createSlateAsync(@Nullable LocationName parent, Slate slate, String slateId)

Creates a slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Slate slate = Slate.newBuilder().build();
       String slateId = "slateId-2126174060";
       Slate response = videoStitcherServiceClient.createSlateAsync(parent, slate, slateId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project in which the slate should be created, in the form of `projects/{project_number}/locations/{location}`.  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)`  
Required. The slate to create.  
`slateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier for the slate. This value should conform to RFC-1034, which restricts to lower-case letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createSlateAsync(CreateSlateRequest request)
    
    
    public final OperationFuture<Slate,OperationMetadata> createSlateAsync(CreateSlateRequest request)

Creates a slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateSlateRequest request =
           CreateSlateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSlateId("slateId-2126174060")
               .setSlate(Slate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Slate response = videoStitcherServiceClient.createSlateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createSlateAsync(String parent, Slate slate, String slateId)
    
    
    public final OperationFuture<Slate,OperationMetadata> createSlateAsync(String parent, Slate slate, String slateId)

Creates a slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Slate slate = Slate.newBuilder().build();
       String slateId = "slateId-2126174060";
       Slate response = videoStitcherServiceClient.createSlateAsync(parent, slate, slateId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the slate should be created, in the form of `projects/{project_number}/locations/{location}`.  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)`  
Required. The slate to create.  
`slateId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier for the slate. This value should conform to RFC-1034, which restricts to lower-case letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createSlateCallable()
    
    
    public final UnaryCallable<CreateSlateRequest,Operation> createSlateCallable()

Creates a slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateSlateRequest request =
           CreateSlateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSlateId("slateId-2126174060")
               .setSlate(Slate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.createSlateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSlateOperationCallable()
    
    
    public final OperationCallable<CreateSlateRequest,Slate,OperationMetadata> createSlateOperationCallable()

Creates a slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateSlateRequest request =
           CreateSlateRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSlateId("slateId-2126174060")
               .setSlate(Slate.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Slate, OperationMetadata> future =
           videoStitcherServiceClient.createSlateOperationCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigAsync(@Nullable LocationName parent, VodConfig vodConfig, String vodConfigId)
    
    
    public final OperationFuture<VodConfig,OperationMetadata> createVodConfigAsync(@Nullable LocationName parent, VodConfig vodConfig, String vodConfigId)

Registers the VOD config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       VodConfig vodConfig = VodConfig.newBuilder().build();
       String vodConfigId = "vodConfigId1497626088";
       VodConfig response =
           videoStitcherServiceClient.createVodConfigAsync(parent, vodConfig, vodConfigId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project in which the VOD config should be created, in the form of `projects/{project_number}/locations/{location}`.  
`vodConfig` | `[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)`  
Required. The VOD config resource to create.  
`vodConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier ID to use for the VOD config.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigAsync(CreateVodConfigRequest request)
    
    
    public final OperationFuture<VodConfig,OperationMetadata> createVodConfigAsync(CreateVodConfigRequest request)

Registers the VOD config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateVodConfigRequest request =
           CreateVodConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVodConfigId("vodConfigId1497626088")
               .setVodConfig(VodConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       VodConfig response = videoStitcherServiceClient.createVodConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigAsync(String parent, VodConfig vodConfig, String vodConfigId)
    
    
    public final OperationFuture<VodConfig,OperationMetadata> createVodConfigAsync(String parent, VodConfig vodConfig, String vodConfigId)

Registers the VOD config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       VodConfig vodConfig = VodConfig.newBuilder().build();
       String vodConfigId = "vodConfigId1497626088";
       VodConfig response =
           videoStitcherServiceClient.createVodConfigAsync(parent, vodConfig, vodConfigId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project in which the VOD config should be created, in the form of `projects/{project_number}/locations/{location}`.  
`vodConfig` | `[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)`  
Required. The VOD config resource to create.  
`vodConfigId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The unique identifier ID to use for the VOD config.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigCallable()
    
    
    public final UnaryCallable<CreateVodConfigRequest,Operation> createVodConfigCallable()

Registers the VOD config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateVodConfigRequest request =
           CreateVodConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVodConfigId("vodConfigId1497626088")
               .setVodConfig(VodConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.createVodConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVodConfigOperationCallable()
    
    
    public final OperationCallable<CreateVodConfigRequest,VodConfig,OperationMetadata> createVodConfigOperationCallable()

Registers the VOD config with the provided unique ID in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateVodConfigRequest request =
           CreateVodConfigRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVodConfigId("vodConfigId1497626088")
               .setVodConfig(VodConfig.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<VodConfig, OperationMetadata> future =
           videoStitcherServiceClient.createVodConfigOperationCallable().futureCall(request);
       // Do something.
       VodConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodSession(@Nullable LocationName parent, VodSession vodSession)
    
    
    public final VodSession createVodSession(@Nullable LocationName parent, VodSession vodSession)

Creates a client side playback VOD session and returns the full tracking and playback metadata of the session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       VodSession vodSession = VodSession.newBuilder().build();
       VodSession response = videoStitcherServiceClient.createVodSession(parent, vodSession);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project and location in which the VOD session should be created, in the form of `projects/{project_number}/locations/{location}`.  
`vodSession` | `[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)`  
Required. Parameters for creating a session.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### createVodSession(CreateVodSessionRequest request)
    
    
    public final VodSession createVodSession(CreateVodSessionRequest request)

Creates a client side playback VOD session and returns the full tracking and playback metadata of the session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateVodSessionRequest request =
           CreateVodSessionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVodSession(VodSession.newBuilder().build())
               .build();
       VodSession response = videoStitcherServiceClient.createVodSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### createVodSession(String parent, VodSession vodSession)
    
    
    public final VodSession createVodSession(String parent, VodSession vodSession)

Creates a client side playback VOD session and returns the full tracking and playback metadata of the session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       VodSession vodSession = VodSession.newBuilder().build();
       VodSession response = videoStitcherServiceClient.createVodSession(parent, vodSession);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project and location in which the VOD session should be created, in the form of `projects/{project_number}/locations/{location}`.  
`vodSession` | `[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)`  
Required. Parameters for creating a session.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### createVodSessionCallable()
    
    
    public final UnaryCallable<CreateVodSessionRequest,VodSession> createVodSessionCallable()

Creates a client side playback VOD session and returns the full tracking and playback metadata of the session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CreateVodSessionRequest request =
           CreateVodSessionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setVodSession(VodSession.newBuilder().build())
               .build();
       ApiFuture<VodSession> future =
           videoStitcherServiceClient.createVodSessionCallable().futureCall(request);
       // Do something.
       VodSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### deleteCdnKeyAsync(@Nullable CdnKeyName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCdnKeyAsync(@Nullable CdnKeyName name)

Deletes the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CdnKeyName name = CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]");
       videoStitcherServiceClient.deleteCdnKeyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.CdnKeyName`  
Required. The name of the CDN key to be deleted, in the form of `projects/{project_number}/locations/{location}/cdnKeys/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteCdnKeyAsync(DeleteCdnKeyRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCdnKeyAsync(DeleteCdnKeyRequest request)

Deletes the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteCdnKeyRequest request =
           DeleteCdnKeyRequest.newBuilder()
               .setName(CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString())
               .build();
       videoStitcherServiceClient.deleteCdnKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteCdnKeyAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCdnKeyAsync(String name)

Deletes the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString();
       videoStitcherServiceClient.deleteCdnKeyAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CDN key to be deleted, in the form of `projects/{project_number}/locations/{location}/cdnKeys/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteCdnKeyCallable()
    
    
    public final UnaryCallable<DeleteCdnKeyRequest,Operation> deleteCdnKeyCallable()

Deletes the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteCdnKeyRequest request =
           DeleteCdnKeyRequest.newBuilder()
               .setName(CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.deleteCdnKeyCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCdnKeyOperationCallable()
    
    
    public final OperationCallable<DeleteCdnKeyRequest,Empty,OperationMetadata> deleteCdnKeyOperationCallable()

Deletes the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteCdnKeyRequest request =
           DeleteCdnKeyRequest.newBuilder()
               .setName(CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           videoStitcherServiceClient.deleteCdnKeyOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigAsync(@Nullable LiveConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLiveConfigAsync(@Nullable LiveConfigName name)

Deletes the specified live config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveConfigName name = LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]");
       videoStitcherServiceClient.deleteLiveConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LiveConfigName`  
Required. The name of the live config to be deleted, in the form of `projects/{project_number}/locations/{location}/liveConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigAsync(DeleteLiveConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLiveConfigAsync(DeleteLiveConfigRequest request)

Deletes the specified live config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteLiveConfigRequest request =
           DeleteLiveConfigRequest.newBuilder()
               .setName(LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString())
               .build();
       videoStitcherServiceClient.deleteLiveConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLiveConfigAsync(String name)

Deletes the specified live config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString();
       videoStitcherServiceClient.deleteLiveConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the live config to be deleted, in the form of `projects/{project_number}/locations/{location}/liveConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigCallable()
    
    
    public final UnaryCallable<DeleteLiveConfigRequest,Operation> deleteLiveConfigCallable()

Deletes the specified live config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteLiveConfigRequest request =
           DeleteLiveConfigRequest.newBuilder()
               .setName(LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.deleteLiveConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLiveConfigOperationCallable()
    
    
    public final OperationCallable<DeleteLiveConfigRequest,Empty,OperationMetadata> deleteLiveConfigOperationCallable()

Deletes the specified live config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteLiveConfigRequest request =
           DeleteLiveConfigRequest.newBuilder()
               .setName(LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           videoStitcherServiceClient.deleteLiveConfigOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateAsync(@Nullable SlateName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSlateAsync(@Nullable SlateName name)

Deletes the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       SlateName name = SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]");
       videoStitcherServiceClient.deleteSlateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.SlateName`  
Required. The name of the slate to be deleted, in the form of `projects/{project_number}/locations/{location}/slates/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateAsync(DeleteSlateRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSlateAsync(DeleteSlateRequest request)

Deletes the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteSlateRequest request =
           DeleteSlateRequest.newBuilder()
               .setName(SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString())
               .build();
       videoStitcherServiceClient.deleteSlateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteSlateAsync(String name)

Deletes the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString();
       videoStitcherServiceClient.deleteSlateAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the slate to be deleted, in the form of `projects/{project_number}/locations/{location}/slates/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateCallable()
    
    
    public final UnaryCallable<DeleteSlateRequest,Operation> deleteSlateCallable()

Deletes the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteSlateRequest request =
           DeleteSlateRequest.newBuilder()
               .setName(SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.deleteSlateCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSlateOperationCallable()
    
    
    public final OperationCallable<DeleteSlateRequest,Empty,OperationMetadata> deleteSlateOperationCallable()

Deletes the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteSlateRequest request =
           DeleteSlateRequest.newBuilder()
               .setName(SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           videoStitcherServiceClient.deleteSlateOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigAsync(@Nullable VodConfigName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVodConfigAsync(@Nullable VodConfigName name)

Deletes the specified VOD config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodConfigName name = VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]");
       videoStitcherServiceClient.deleteVodConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodConfigName`  
Required. The name of the VOD config to be deleted, in the form of `projects/{project_number}/locations/{location}/vodConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigAsync(DeleteVodConfigRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVodConfigAsync(DeleteVodConfigRequest request)

Deletes the specified VOD config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteVodConfigRequest request =
           DeleteVodConfigRequest.newBuilder()
               .setName(VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString())
               .build();
       videoStitcherServiceClient.deleteVodConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteVodConfigAsync(String name)

Deletes the specified VOD config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString();
       videoStitcherServiceClient.deleteVodConfigAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the VOD config to be deleted, in the form of `projects/{project_number}/locations/{location}/vodConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigCallable()
    
    
    public final UnaryCallable<DeleteVodConfigRequest,Operation> deleteVodConfigCallable()

Deletes the specified VOD config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteVodConfigRequest request =
           DeleteVodConfigRequest.newBuilder()
               .setName(VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.deleteVodConfigCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVodConfigOperationCallable()
    
    
    public final OperationCallable<DeleteVodConfigRequest,Empty,OperationMetadata> deleteVodConfigOperationCallable()

Deletes the specified VOD config.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       DeleteVodConfigRequest request =
           DeleteVodConfigRequest.newBuilder()
               .setName(VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           videoStitcherServiceClient.deleteVodConfigOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### getCdnKey(@Nullable CdnKeyName name)
    
    
    public final CdnKey getCdnKey(@Nullable CdnKeyName name)

Returns the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CdnKeyName name = CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]");
       CdnKey response = videoStitcherServiceClient.getCdnKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.CdnKeyName`  
Required. The name of the CDN key to be retrieved, in the form of `projects/{project}/locations/{location}/cdnKeys/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)` |   
  
### getCdnKey(GetCdnKeyRequest request)
    
    
    public final CdnKey getCdnKey(GetCdnKeyRequest request)

Returns the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetCdnKeyRequest request =
           GetCdnKeyRequest.newBuilder()
               .setName(CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString())
               .build();
       CdnKey response = videoStitcherServiceClient.getCdnKey(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetCdnKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)` |   
  
### getCdnKey(String name)
    
    
    public final CdnKey getCdnKey(String name)

Returns the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString();
       CdnKey response = videoStitcherServiceClient.getCdnKey(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the CDN key to be retrieved, in the form of `projects/{project}/locations/{location}/cdnKeys/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)` |   
  
### getCdnKeyCallable()
    
    
    public final UnaryCallable<GetCdnKeyRequest,CdnKey> getCdnKeyCallable()

Returns the specified CDN key.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetCdnKeyRequest request =
           GetCdnKeyRequest.newBuilder()
               .setName(CdnKeyName.of("[PROJECT]", "[LOCATION]", "[CDN_KEY]").toString())
               .build();
       ApiFuture<CdnKey> future = videoStitcherServiceClient.getCdnKeyCallable().futureCall(request);
       // Do something.
       CdnKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)>` |   
  
### getLiveAdTagDetail(@Nullable LiveAdTagDetailName name)
    
    
    public final LiveAdTagDetail getLiveAdTagDetail(@Nullable LiveAdTagDetailName name)

Returns the specified ad tag detail for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveAdTagDetailName name =
           LiveAdTagDetailName.of(
               "[PROJECT]", "[LOCATION]", "[LIVE_SESSION]", "[LIVE_AD_TAG_DETAIL]");
       LiveAdTagDetail response = videoStitcherServiceClient.getLiveAdTagDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LiveAdTagDetailName`  
Required. The resource name in the form of `projects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{live_ad_tag_detail}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)` |   
  
### getLiveAdTagDetail(GetLiveAdTagDetailRequest request)
    
    
    public final LiveAdTagDetail getLiveAdTagDetail(GetLiveAdTagDetailRequest request)

Returns the specified ad tag detail for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveAdTagDetailRequest request =
           GetLiveAdTagDetailRequest.newBuilder()
               .setName(
                   LiveAdTagDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[LIVE_SESSION]", "[LIVE_AD_TAG_DETAIL]")
                       .toString())
               .build();
       LiveAdTagDetail response = videoStitcherServiceClient.getLiveAdTagDetail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)` |   
  
### getLiveAdTagDetail(String name)
    
    
    public final LiveAdTagDetail getLiveAdTagDetail(String name)

Returns the specified ad tag detail for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name =
           LiveAdTagDetailName.of(
                   "[PROJECT]", "[LOCATION]", "[LIVE_SESSION]", "[LIVE_AD_TAG_DETAIL]")
               .toString();
       LiveAdTagDetail response = videoStitcherServiceClient.getLiveAdTagDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name in the form of `projects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{live_ad_tag_detail}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)` |   
  
### getLiveAdTagDetailCallable()
    
    
    public final UnaryCallable<GetLiveAdTagDetailRequest,LiveAdTagDetail> getLiveAdTagDetailCallable()

Returns the specified ad tag detail for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveAdTagDetailRequest request =
           GetLiveAdTagDetailRequest.newBuilder()
               .setName(
                   LiveAdTagDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[LIVE_SESSION]", "[LIVE_AD_TAG_DETAIL]")
                       .toString())
               .build();
       ApiFuture<LiveAdTagDetail> future =
           videoStitcherServiceClient.getLiveAdTagDetailCallable().futureCall(request);
       // Do something.
       LiveAdTagDetail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest),[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)>` |   
  
### getLiveConfig(@Nullable LiveConfigName name)
    
    
    public final LiveConfig getLiveConfig(@Nullable LiveConfigName name)

Returns the specified live config managed by the Video Stitcher service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveConfigName name = LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]");
       LiveConfig response = videoStitcherServiceClient.getLiveConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LiveConfigName`  
Required. The name of the live config to be retrieved, in the form of `projects/{project_number}/locations/{location}/liveConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)` |   
  
### getLiveConfig(GetLiveConfigRequest request)
    
    
    public final LiveConfig getLiveConfig(GetLiveConfigRequest request)

Returns the specified live config managed by the Video Stitcher service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveConfigRequest request =
           GetLiveConfigRequest.newBuilder()
               .setName(LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString())
               .build();
       LiveConfig response = videoStitcherServiceClient.getLiveConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)` |   
  
### getLiveConfig(String name)
    
    
    public final LiveConfig getLiveConfig(String name)

Returns the specified live config managed by the Video Stitcher service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString();
       LiveConfig response = videoStitcherServiceClient.getLiveConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the live config to be retrieved, in the form of `projects/{project_number}/locations/{location}/liveConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)` |   
  
### getLiveConfigCallable()
    
    
    public final UnaryCallable<GetLiveConfigRequest,LiveConfig> getLiveConfigCallable()

Returns the specified live config managed by the Video Stitcher service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveConfigRequest request =
           GetLiveConfigRequest.newBuilder()
               .setName(LiveConfigName.of("[PROJECT]", "[LOCATION]", "[LIVE_CONFIG]").toString())
               .build();
       ApiFuture<LiveConfig> future =
           videoStitcherServiceClient.getLiveConfigCallable().futureCall(request);
       // Do something.
       LiveConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)>` |   
  
### getLiveSession(@Nullable LiveSessionName name)
    
    
    public final LiveSession getLiveSession(@Nullable LiveSessionName name)

Returns the details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveSessionName name = LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]");
       LiveSession response = videoStitcherServiceClient.getLiveSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LiveSessionName`  
Required. The name of the live session, in the form of `projects/{project_number}/locations/{location}/liveSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### getLiveSession(GetLiveSessionRequest request)
    
    
    public final LiveSession getLiveSession(GetLiveSessionRequest request)

Returns the details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveSessionRequest request =
           GetLiveSessionRequest.newBuilder()
               .setName(LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString())
               .build();
       LiveSession response = videoStitcherServiceClient.getLiveSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### getLiveSession(String name)
    
    
    public final LiveSession getLiveSession(String name)

Returns the details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString();
       LiveSession response = videoStitcherServiceClient.getLiveSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the live session, in the form of `projects/{project_number}/locations/{location}/liveSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### getLiveSessionCallable()
    
    
    public final UnaryCallable<GetLiveSessionRequest,LiveSession> getLiveSessionCallable()

Returns the details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetLiveSessionRequest request =
           GetLiveSessionRequest.newBuilder()
               .setName(LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString())
               .build();
       ApiFuture<LiveSession> future =
           videoStitcherServiceClient.getLiveSessionCallable().futureCall(request);
       // Do something.
       LiveSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable VideoStitcherServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings` |   
  
### getSlate(@Nullable SlateName name)
    
    
    public final Slate getSlate(@Nullable SlateName name)

Returns the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       SlateName name = SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]");
       Slate response = videoStitcherServiceClient.getSlate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.SlateName`  
Required. The name of the slate to be retrieved, of the slate, in the form of `projects/{project_number}/locations/{location}/slates/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)` |   
  
### getSlate(GetSlateRequest request)
    
    
    public final Slate getSlate(GetSlateRequest request)

Returns the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetSlateRequest request =
           GetSlateRequest.newBuilder()
               .setName(SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString())
               .build();
       Slate response = videoStitcherServiceClient.getSlate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)` |   
  
### getSlate(String name)
    
    
    public final Slate getSlate(String name)

Returns the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString();
       Slate response = videoStitcherServiceClient.getSlate(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the slate to be retrieved, of the slate, in the form of `projects/{project_number}/locations/{location}/slates/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)` |   
  
### getSlateCallable()
    
    
    public final UnaryCallable<GetSlateRequest,Slate> getSlateCallable()

Returns the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetSlateRequest request =
           GetSlateRequest.newBuilder()
               .setName(SlateName.of("[PROJECT]", "[LOCATION]", "[SLATE]").toString())
               .build();
       ApiFuture<Slate> future = videoStitcherServiceClient.getSlateCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)>` |   
  
### getStub()
    
    
    public VideoStitcherServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStub)` |   
  
### getVodAdTagDetail(@Nullable VodAdTagDetailName name)
    
    
    public final VodAdTagDetail getVodAdTagDetail(@Nullable VodAdTagDetailName name)

Returns the specified ad tag detail for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodAdTagDetailName name =
           VodAdTagDetailName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_AD_TAG_DETAIL]");
       VodAdTagDetail response = videoStitcherServiceClient.getVodAdTagDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodAdTagDetailName`  
Required. The name of the ad tag detail for the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodAdTagDetails/{vod_ad_tag_detail}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)` |   
  
### getVodAdTagDetail(GetVodAdTagDetailRequest request)
    
    
    public final VodAdTagDetail getVodAdTagDetail(GetVodAdTagDetailRequest request)

Returns the specified ad tag detail for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodAdTagDetailRequest request =
           GetVodAdTagDetailRequest.newBuilder()
               .setName(
                   VodAdTagDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_AD_TAG_DETAIL]")
                       .toString())
               .build();
       VodAdTagDetail response = videoStitcherServiceClient.getVodAdTagDetail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)` |   
  
### getVodAdTagDetail(String name)
    
    
    public final VodAdTagDetail getVodAdTagDetail(String name)

Returns the specified ad tag detail for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name =
           VodAdTagDetailName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_AD_TAG_DETAIL]")
               .toString();
       VodAdTagDetail response = videoStitcherServiceClient.getVodAdTagDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ad tag detail for the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodAdTagDetails/{vod_ad_tag_detail}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)` |   
  
### getVodAdTagDetailCallable()
    
    
    public final UnaryCallable<GetVodAdTagDetailRequest,VodAdTagDetail> getVodAdTagDetailCallable()

Returns the specified ad tag detail for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodAdTagDetailRequest request =
           GetVodAdTagDetailRequest.newBuilder()
               .setName(
                   VodAdTagDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_AD_TAG_DETAIL]")
                       .toString())
               .build();
       ApiFuture<VodAdTagDetail> future =
           videoStitcherServiceClient.getVodAdTagDetailCallable().futureCall(request);
       // Do something.
       VodAdTagDetail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest),[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)>` |   
  
### getVodConfig(@Nullable VodConfigName name)
    
    
    public final VodConfig getVodConfig(@Nullable VodConfigName name)

Returns the specified VOD config managed by the Video Stitcher API service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodConfigName name = VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]");
       VodConfig response = videoStitcherServiceClient.getVodConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodConfigName`  
Required. The name of the VOD config to be retrieved, in the form of `projects/{project_number}/locations/{location}/vodConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)` |   
  
### getVodConfig(GetVodConfigRequest request)
    
    
    public final VodConfig getVodConfig(GetVodConfigRequest request)

Returns the specified VOD config managed by the Video Stitcher API service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodConfigRequest request =
           GetVodConfigRequest.newBuilder()
               .setName(VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString())
               .build();
       VodConfig response = videoStitcherServiceClient.getVodConfig(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)` |   
  
### getVodConfig(String name)
    
    
    public final VodConfig getVodConfig(String name)

Returns the specified VOD config managed by the Video Stitcher API service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString();
       VodConfig response = videoStitcherServiceClient.getVodConfig(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the VOD config to be retrieved, in the form of `projects/{project_number}/locations/{location}/vodConfigs/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)` |   
  
### getVodConfigCallable()
    
    
    public final UnaryCallable<GetVodConfigRequest,VodConfig> getVodConfigCallable()

Returns the specified VOD config managed by the Video Stitcher API service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodConfigRequest request =
           GetVodConfigRequest.newBuilder()
               .setName(VodConfigName.of("[PROJECT]", "[LOCATION]", "[VOD_CONFIG]").toString())
               .build();
       ApiFuture<VodConfig> future =
           videoStitcherServiceClient.getVodConfigCallable().futureCall(request);
       // Do something.
       VodConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)>` |   
  
### getVodSession(@Nullable VodSessionName name)
    
    
    public final VodSession getVodSession(@Nullable VodSessionName name)

Returns the full tracking, playback metadata, and relevant ad-ops logs for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodSessionName name = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]");
       VodSession response = videoStitcherServiceClient.getVodSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodSessionName`  
Required. The name of the VOD session to be retrieved, in the form of `projects/{project_number}/locations/{location}/vodSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### getVodSession(GetVodSessionRequest request)
    
    
    public final VodSession getVodSession(GetVodSessionRequest request)

Returns the full tracking, playback metadata, and relevant ad-ops logs for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodSessionRequest request =
           GetVodSessionRequest.newBuilder()
               .setName(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .build();
       VodSession response = videoStitcherServiceClient.getVodSession(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### getVodSession(String name)
    
    
    public final VodSession getVodSession(String name)

Returns the full tracking, playback metadata, and relevant ad-ops logs for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString();
       VodSession response = videoStitcherServiceClient.getVodSession(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the VOD session to be retrieved, in the form of `projects/{project_number}/locations/{location}/vodSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)` |   
  
### getVodSessionCallable()
    
    
    public final UnaryCallable<GetVodSessionRequest,VodSession> getVodSessionCallable()

Returns the full tracking, playback metadata, and relevant ad-ops logs for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodSessionRequest request =
           GetVodSessionRequest.newBuilder()
               .setName(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .build();
       ApiFuture<VodSession> future =
           videoStitcherServiceClient.getVodSessionCallable().futureCall(request);
       // Do something.
       VodSession response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### getVodStitchDetail(@Nullable VodStitchDetailName name)
    
    
    public final VodStitchDetail getVodStitchDetail(@Nullable VodStitchDetailName name)

Returns the specified stitching information for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodStitchDetailName name =
           VodStitchDetailName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_STITCH_DETAIL]");
       VodStitchDetail response = videoStitcherServiceClient.getVodStitchDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodStitchDetailName`  
Required. The name of the stitch detail in the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodStitchDetails/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)` |   
  
### getVodStitchDetail(GetVodStitchDetailRequest request)
    
    
    public final VodStitchDetail getVodStitchDetail(GetVodStitchDetailRequest request)

Returns the specified stitching information for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodStitchDetailRequest request =
           GetVodStitchDetailRequest.newBuilder()
               .setName(
                   VodStitchDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_STITCH_DETAIL]")
                       .toString())
               .build();
       VodStitchDetail response = videoStitcherServiceClient.getVodStitchDetail(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)` |   
  
### getVodStitchDetail(String name)
    
    
    public final VodStitchDetail getVodStitchDetail(String name)

Returns the specified stitching information for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String name =
           VodStitchDetailName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_STITCH_DETAIL]")
               .toString();
       VodStitchDetail response = videoStitcherServiceClient.getVodStitchDetail(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the stitch detail in the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodStitchDetails/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)` |   
  
### getVodStitchDetailCallable()
    
    
    public final UnaryCallable<GetVodStitchDetailRequest,VodStitchDetail> getVodStitchDetailCallable()

Returns the specified stitching information for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       GetVodStitchDetailRequest request =
           GetVodStitchDetailRequest.newBuilder()
               .setName(
                   VodStitchDetailName.of(
                           "[PROJECT]", "[LOCATION]", "[VOD_SESSION]", "[VOD_STITCH_DETAIL]")
                       .toString())
               .build();
       ApiFuture<VodStitchDetail> future =
           videoStitcherServiceClient.getVodStitchDetailCallable().futureCall(request);
       // Do something.
       VodStitchDetail response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest),[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)>` |   
  
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
  
### listCdnKeys(@Nullable LocationName parent)
    
    
    public final VideoStitcherServiceClient.ListCdnKeysPagedResponse listCdnKeys(@Nullable LocationName parent)

Lists all CDN keys in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (CdnKey element : videoStitcherServiceClient.listCdnKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project that contains the list of CDN keys, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)` |   
  
### listCdnKeys(ListCdnKeysRequest request)
    
    
    public final VideoStitcherServiceClient.ListCdnKeysPagedResponse listCdnKeys(ListCdnKeysRequest request)

Lists all CDN keys in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListCdnKeysRequest request =
           ListCdnKeysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (CdnKey element : videoStitcherServiceClient.listCdnKeys(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)` |   
  
### listCdnKeys(String parent)
    
    
    public final VideoStitcherServiceClient.ListCdnKeysPagedResponse listCdnKeys(String parent)

Lists all CDN keys in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (CdnKey element : videoStitcherServiceClient.listCdnKeys(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project that contains the list of CDN keys, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)` |   
  
### listCdnKeysCallable()
    
    
    public final UnaryCallable<ListCdnKeysRequest,ListCdnKeysResponse> listCdnKeysCallable()

Lists all CDN keys in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListCdnKeysRequest request =
           ListCdnKeysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListCdnKeysResponse response =
             videoStitcherServiceClient.listCdnKeysCallable().call(request);
         for (CdnKey element : response.getCdnKeysList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest),[ListCdnKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysResponse)>` |   
  
### listCdnKeysPagedCallable()
    
    
    public final UnaryCallable<ListCdnKeysRequest,VideoStitcherServiceClient.ListCdnKeysPagedResponse> listCdnKeysPagedCallable()

Lists all CDN keys in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListCdnKeysRequest request =
           ListCdnKeysRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<CdnKey> future =
           videoStitcherServiceClient.listCdnKeysPagedCallable().futureCall(request);
       // Do something.
       for (CdnKey element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest),[ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)>` |   
  
### listLiveAdTagDetails(@Nullable LiveSessionName parent)
    
    
    public final VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse listLiveAdTagDetails(@Nullable LiveSessionName parent)

Return the list of ad tag details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveSessionName parent = LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]");
       for (LiveAdTagDetail element :
           videoStitcherServiceClient.listLiveAdTagDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LiveSessionName`  
Required. The resource parent in the form of `projects/{project}/locations/{location}/liveSessions/{live_session}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)` |   
  
### listLiveAdTagDetails(ListLiveAdTagDetailsRequest request)
    
    
    public final VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse listLiveAdTagDetails(ListLiveAdTagDetailsRequest request)

Return the list of ad tag details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveAdTagDetailsRequest request =
           ListLiveAdTagDetailsRequest.newBuilder()
               .setParent(LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (LiveAdTagDetail element :
           videoStitcherServiceClient.listLiveAdTagDetails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)` |   
  
### listLiveAdTagDetails(String parent)
    
    
    public final VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse listLiveAdTagDetails(String parent)

Return the list of ad tag details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString();
       for (LiveAdTagDetail element :
           videoStitcherServiceClient.listLiveAdTagDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource parent in the form of `projects/{project}/locations/{location}/liveSessions/{live_session}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)` |   
  
### listLiveAdTagDetailsCallable()
    
    
    public final UnaryCallable<ListLiveAdTagDetailsRequest,ListLiveAdTagDetailsResponse> listLiveAdTagDetailsCallable()

Return the list of ad tag details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveAdTagDetailsRequest request =
           ListLiveAdTagDetailsRequest.newBuilder()
               .setParent(LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLiveAdTagDetailsResponse response =
             videoStitcherServiceClient.listLiveAdTagDetailsCallable().call(request);
         for (LiveAdTagDetail element : response.getLiveAdTagDetailsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest),[ListLiveAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsResponse)>` |   
  
### listLiveAdTagDetailsPagedCallable()
    
    
    public final UnaryCallable<ListLiveAdTagDetailsRequest,VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse> listLiveAdTagDetailsPagedCallable()

Return the list of ad tag details for the specified live session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveAdTagDetailsRequest request =
           ListLiveAdTagDetailsRequest.newBuilder()
               .setParent(LiveSessionName.of("[PROJECT]", "[LOCATION]", "[LIVE_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<LiveAdTagDetail> future =
           videoStitcherServiceClient.listLiveAdTagDetailsPagedCallable().futureCall(request);
       // Do something.
       for (LiveAdTagDetail element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest),[ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)>` |   
  
### listLiveConfigs(@Nullable LocationName parent)
    
    
    public final VideoStitcherServiceClient.ListLiveConfigsPagedResponse listLiveConfigs(@Nullable LocationName parent)

Lists all live configs managed by the Video Stitcher that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (LiveConfig element : videoStitcherServiceClient.listLiveConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project that contains the list of live configs, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)` |   
  
### listLiveConfigs(ListLiveConfigsRequest request)
    
    
    public final VideoStitcherServiceClient.ListLiveConfigsPagedResponse listLiveConfigs(ListLiveConfigsRequest request)

Lists all live configs managed by the Video Stitcher that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveConfigsRequest request =
           ListLiveConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (LiveConfig element : videoStitcherServiceClient.listLiveConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)` |   
  
### listLiveConfigs(String parent)
    
    
    public final VideoStitcherServiceClient.ListLiveConfigsPagedResponse listLiveConfigs(String parent)

Lists all live configs managed by the Video Stitcher that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (LiveConfig element : videoStitcherServiceClient.listLiveConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project that contains the list of live configs, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)` |   
  
### listLiveConfigsCallable()
    
    
    public final UnaryCallable<ListLiveConfigsRequest,ListLiveConfigsResponse> listLiveConfigsCallable()

Lists all live configs managed by the Video Stitcher that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveConfigsRequest request =
           ListLiveConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLiveConfigsResponse response =
             videoStitcherServiceClient.listLiveConfigsCallable().call(request);
         for (LiveConfig element : response.getLiveConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest),[ListLiveConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsResponse)>` |   
  
### listLiveConfigsPagedCallable()
    
    
    public final UnaryCallable<ListLiveConfigsRequest,VideoStitcherServiceClient.ListLiveConfigsPagedResponse> listLiveConfigsPagedCallable()

Lists all live configs managed by the Video Stitcher that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListLiveConfigsRequest request =
           ListLiveConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<LiveConfig> future =
           videoStitcherServiceClient.listLiveConfigsPagedCallable().futureCall(request);
       // Do something.
       for (LiveConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest),[ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)>` |   
  
### listSlates(@Nullable LocationName parent)
    
    
    public final VideoStitcherServiceClient.ListSlatesPagedResponse listSlates(@Nullable LocationName parent)

Lists all slates in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Slate element : videoStitcherServiceClient.listSlates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project to list slates, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)` |   
  
### listSlates(ListSlatesRequest request)
    
    
    public final VideoStitcherServiceClient.ListSlatesPagedResponse listSlates(ListSlatesRequest request)

Lists all slates in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Slate element : videoStitcherServiceClient.listSlates(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)` |   
  
### listSlates(String parent)
    
    
    public final VideoStitcherServiceClient.ListSlatesPagedResponse listSlates(String parent)

Lists all slates in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Slate element : videoStitcherServiceClient.listSlates(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project to list slates, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)` |   
  
### listSlatesCallable()
    
    
    public final UnaryCallable<ListSlatesRequest,ListSlatesResponse> listSlatesCallable()

Lists all slates in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListSlatesResponse response = videoStitcherServiceClient.listSlatesCallable().call(request);
         for (Slate element : response.getSlatesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest),[ListSlatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesResponse)>` |   
  
### listSlatesPagedCallable()
    
    
    public final UnaryCallable<ListSlatesRequest,VideoStitcherServiceClient.ListSlatesPagedResponse> listSlatesPagedCallable()

Lists all slates in the specified project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListSlatesRequest request =
           ListSlatesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Slate> future =
           videoStitcherServiceClient.listSlatesPagedCallable().futureCall(request);
       // Do something.
       for (Slate element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest),[ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)>` |   
  
### listVodAdTagDetails(@Nullable VodSessionName parent)
    
    
    public final VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse listVodAdTagDetails(@Nullable VodSessionName parent)

Return the list of ad tag details for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodSessionName parent = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]");
       for (VodAdTagDetail element :
           videoStitcherServiceClient.listVodAdTagDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodSessionName`  
Required. The VOD session which the ad tag details belong to, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)` |   
  
### listVodAdTagDetails(ListVodAdTagDetailsRequest request)
    
    
    public final VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse listVodAdTagDetails(ListVodAdTagDetailsRequest request)

Return the list of ad tag details for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodAdTagDetailsRequest request =
           ListVodAdTagDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (VodAdTagDetail element :
           videoStitcherServiceClient.listVodAdTagDetails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)` |   
  
### listVodAdTagDetails(String parent)
    
    
    public final VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse listVodAdTagDetails(String parent)

Return the list of ad tag details for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString();
       for (VodAdTagDetail element :
           videoStitcherServiceClient.listVodAdTagDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The VOD session which the ad tag details belong to, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)` |   
  
### listVodAdTagDetailsCallable()
    
    
    public final UnaryCallable<ListVodAdTagDetailsRequest,ListVodAdTagDetailsResponse> listVodAdTagDetailsCallable()

Return the list of ad tag details for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodAdTagDetailsRequest request =
           ListVodAdTagDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListVodAdTagDetailsResponse response =
             videoStitcherServiceClient.listVodAdTagDetailsCallable().call(request);
         for (VodAdTagDetail element : response.getVodAdTagDetailsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest),[ListVodAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsResponse)>` |   
  
### listVodAdTagDetailsPagedCallable()
    
    
    public final UnaryCallable<ListVodAdTagDetailsRequest,VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse> listVodAdTagDetailsPagedCallable()

Return the list of ad tag details for the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodAdTagDetailsRequest request =
           ListVodAdTagDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<VodAdTagDetail> future =
           videoStitcherServiceClient.listVodAdTagDetailsPagedCallable().futureCall(request);
       // Do something.
       for (VodAdTagDetail element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest),[ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)>` |   
  
### listVodConfigs(@Nullable LocationName parent)
    
    
    public final VideoStitcherServiceClient.ListVodConfigsPagedResponse listVodConfigs(@Nullable LocationName parent)

Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (VodConfig element : videoStitcherServiceClient.listVodConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.LocationName`  
Required. The project that contains the list of VOD configs, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)` |   
  
### listVodConfigs(ListVodConfigsRequest request)
    
    
    public final VideoStitcherServiceClient.ListVodConfigsPagedResponse listVodConfigs(ListVodConfigsRequest request)

Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodConfigsRequest request =
           ListVodConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (VodConfig element : videoStitcherServiceClient.listVodConfigs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)` |   
  
### listVodConfigs(String parent)
    
    
    public final VideoStitcherServiceClient.ListVodConfigsPagedResponse listVodConfigs(String parent)

Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (VodConfig element : videoStitcherServiceClient.listVodConfigs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The project that contains the list of VOD configs, in the form of `projects/{project_number}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)` |   
  
### listVodConfigsCallable()
    
    
    public final UnaryCallable<ListVodConfigsRequest,ListVodConfigsResponse> listVodConfigsCallable()

Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodConfigsRequest request =
           ListVodConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListVodConfigsResponse response =
             videoStitcherServiceClient.listVodConfigsCallable().call(request);
         for (VodConfig element : response.getVodConfigsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest),[ListVodConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsResponse)>` |   
  
### listVodConfigsPagedCallable()
    
    
    public final UnaryCallable<ListVodConfigsRequest,VideoStitcherServiceClient.ListVodConfigsPagedResponse> listVodConfigsPagedCallable()

Lists all VOD configs managed by the Video Stitcher API that belong to the specified project and region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodConfigsRequest request =
           ListVodConfigsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<VodConfig> future =
           videoStitcherServiceClient.listVodConfigsPagedCallable().futureCall(request);
       // Do something.
       for (VodConfig element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest),[ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)>` |   
  
### listVodStitchDetails(@Nullable VodSessionName parent)
    
    
    public final VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse listVodStitchDetails(@Nullable VodSessionName parent)

Returns a list of detailed stitching information of the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodSessionName parent = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]");
       for (VodStitchDetail element :
           videoStitcherServiceClient.listVodStitchDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.video.stitcher.v1.VodSessionName`  
Required. The VOD session where the stitch details belong to, in the form of `projects/{project}/locations/{location}/vodSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)` |   
  
### listVodStitchDetails(ListVodStitchDetailsRequest request)
    
    
    public final VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse listVodStitchDetails(ListVodStitchDetailsRequest request)

Returns a list of detailed stitching information of the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodStitchDetailsRequest request =
           ListVodStitchDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (VodStitchDetail element :
           videoStitcherServiceClient.listVodStitchDetails(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)` |   
  
### listVodStitchDetails(String parent)
    
    
    public final VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse listVodStitchDetails(String parent)

Returns a list of detailed stitching information of the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       String parent = VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString();
       for (VodStitchDetail element :
           videoStitcherServiceClient.listVodStitchDetails(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The VOD session where the stitch details belong to, in the form of `projects/{project}/locations/{location}/vodSessions/{id}`.  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)` |   
  
### listVodStitchDetailsCallable()
    
    
    public final UnaryCallable<ListVodStitchDetailsRequest,ListVodStitchDetailsResponse> listVodStitchDetailsCallable()

Returns a list of detailed stitching information of the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodStitchDetailsRequest request =
           ListVodStitchDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListVodStitchDetailsResponse response =
             videoStitcherServiceClient.listVodStitchDetailsCallable().call(request);
         for (VodStitchDetail element : response.getVodStitchDetailsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest),[ListVodStitchDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsResponse)>` |   
  
### listVodStitchDetailsPagedCallable()
    
    
    public final UnaryCallable<ListVodStitchDetailsRequest,VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse> listVodStitchDetailsPagedCallable()

Returns a list of detailed stitching information of the specified VOD session.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       ListVodStitchDetailsRequest request =
           ListVodStitchDetailsRequest.newBuilder()
               .setParent(VodSessionName.of("[PROJECT]", "[LOCATION]", "[VOD_SESSION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<VodStitchDetail> future =
           videoStitcherServiceClient.listVodStitchDetailsPagedCallable().futureCall(request);
       // Do something.
       for (VodStitchDetail element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest),[ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCdnKeyAsync(CdnKey cdnKey, FieldMask updateMask)
    
    
    public final OperationFuture<CdnKey,OperationMetadata> updateCdnKeyAsync(CdnKey cdnKey, FieldMask updateMask)

Updates the specified CDN key. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       CdnKey cdnKey = CdnKey.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       CdnKey response = videoStitcherServiceClient.updateCdnKeyAsync(cdnKey, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`cdnKey` | `[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)`  
Required. The CDN key resource which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateCdnKeyAsync(UpdateCdnKeyRequest request)
    
    
    public final OperationFuture<CdnKey,OperationMetadata> updateCdnKeyAsync(UpdateCdnKeyRequest request)

Updates the specified CDN key. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateCdnKeyRequest request =
           UpdateCdnKeyRequest.newBuilder()
               .setCdnKey(CdnKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       CdnKey response = videoStitcherServiceClient.updateCdnKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateCdnKeyCallable()
    
    
    public final UnaryCallable<UpdateCdnKeyRequest,Operation> updateCdnKeyCallable()

Updates the specified CDN key. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateCdnKeyRequest request =
           UpdateCdnKeyRequest.newBuilder()
               .setCdnKey(CdnKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.updateCdnKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCdnKeyOperationCallable()
    
    
    public final OperationCallable<UpdateCdnKeyRequest,CdnKey,OperationMetadata> updateCdnKeyOperationCallable()

Updates the specified CDN key. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateCdnKeyRequest request =
           UpdateCdnKeyRequest.newBuilder()
               .setCdnKey(CdnKey.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<CdnKey, OperationMetadata> future =
           videoStitcherServiceClient.updateCdnKeyOperationCallable().futureCall(request);
       // Do something.
       CdnKey response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateLiveConfigAsync(LiveConfig liveConfig, FieldMask updateMask)
    
    
    public final OperationFuture<LiveConfig,OperationMetadata> updateLiveConfigAsync(LiveConfig liveConfig, FieldMask updateMask)

Updates the specified LiveConfig. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       LiveConfig liveConfig = LiveConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       LiveConfig response =
           videoStitcherServiceClient.updateLiveConfigAsync(liveConfig, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`liveConfig` | `[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)`  
Required. The LiveConfig resource which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateLiveConfigAsync(UpdateLiveConfigRequest request)
    
    
    public final OperationFuture<LiveConfig,OperationMetadata> updateLiveConfigAsync(UpdateLiveConfigRequest request)

Updates the specified LiveConfig. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateLiveConfigRequest request =
           UpdateLiveConfigRequest.newBuilder()
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       LiveConfig response = videoStitcherServiceClient.updateLiveConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateLiveConfigCallable()
    
    
    public final UnaryCallable<UpdateLiveConfigRequest,Operation> updateLiveConfigCallable()

Updates the specified LiveConfig. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateLiveConfigRequest request =
           UpdateLiveConfigRequest.newBuilder()
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.updateLiveConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLiveConfigOperationCallable()
    
    
    public final OperationCallable<UpdateLiveConfigRequest,LiveConfig,OperationMetadata> updateLiveConfigOperationCallable()

Updates the specified LiveConfig. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateLiveConfigRequest request =
           UpdateLiveConfigRequest.newBuilder()
               .setLiveConfig(LiveConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<LiveConfig, OperationMetadata> future =
           videoStitcherServiceClient.updateLiveConfigOperationCallable().futureCall(request);
       // Do something.
       LiveConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateSlateAsync(Slate slate, FieldMask updateMask)
    
    
    public final OperationFuture<Slate,OperationMetadata> updateSlateAsync(Slate slate, FieldMask updateMask)

Updates the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       Slate slate = Slate.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Slate response = videoStitcherServiceClient.updateSlateAsync(slate, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`slate` | `[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)`  
Required. The resource with updated fields.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask which specifies fields which should be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateSlateAsync(UpdateSlateRequest request)
    
    
    public final OperationFuture<Slate,OperationMetadata> updateSlateAsync(UpdateSlateRequest request)

Updates the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateSlateRequest request =
           UpdateSlateRequest.newBuilder()
               .setSlate(Slate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Slate response = videoStitcherServiceClient.updateSlateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateSlateCallable()
    
    
    public final UnaryCallable<UpdateSlateRequest,Operation> updateSlateCallable()

Updates the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateSlateRequest request =
           UpdateSlateRequest.newBuilder()
               .setSlate(Slate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.updateSlateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSlateOperationCallable()
    
    
    public final OperationCallable<UpdateSlateRequest,Slate,OperationMetadata> updateSlateOperationCallable()

Updates the specified slate.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateSlateRequest request =
           UpdateSlateRequest.newBuilder()
               .setSlate(Slate.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Slate, OperationMetadata> future =
           videoStitcherServiceClient.updateSlateOperationCallable().futureCall(request);
       // Do something.
       Slate response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateVodConfigAsync(UpdateVodConfigRequest request)
    
    
    public final OperationFuture<VodConfig,OperationMetadata> updateVodConfigAsync(UpdateVodConfigRequest request)

Updates the specified VOD config. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateVodConfigRequest request =
           UpdateVodConfigRequest.newBuilder()
               .setVodConfig(VodConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       VodConfig response = videoStitcherServiceClient.updateVodConfigAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateVodConfigAsync(VodConfig vodConfig, FieldMask updateMask)
    
    
    public final OperationFuture<VodConfig,OperationMetadata> updateVodConfigAsync(VodConfig vodConfig, FieldMask updateMask)

Updates the specified VOD config. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       VodConfig vodConfig = VodConfig.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       VodConfig response =
           videoStitcherServiceClient.updateVodConfigAsync(vodConfig, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`vodConfig` | `[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)`  
Required. The VOD config resource which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask>  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateVodConfigCallable()
    
    
    public final UnaryCallable<UpdateVodConfigRequest,Operation> updateVodConfigCallable()

Updates the specified VOD config. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateVodConfigRequest request =
           UpdateVodConfigRequest.newBuilder()
               .setVodConfig(VodConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           videoStitcherServiceClient.updateVodConfigCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVodConfigOperationCallable()
    
    
    public final OperationCallable<UpdateVodConfigRequest,VodConfig,OperationMetadata> updateVodConfigOperationCallable()

Updates the specified VOD config. Only update fields specified in the call method body.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VideoStitcherServiceClient videoStitcherServiceClient =
         VideoStitcherServiceClient.create()) {
       UpdateVodConfigRequest request =
           UpdateVodConfigRequest.newBuilder()
               .setVodConfig(VodConfig.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<VodConfig, OperationMetadata> future =
           videoStitcherServiceClient.updateVodConfigOperationCallable().futureCall(request);
       // Do something.
       VodConfig response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
