---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings
title: Class VideoStitcherServiceSettings (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:39.235075+00:00
---

# Class VideoStitcherServiceSettings (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VideoStitcherServiceSettings (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6  0.1.2 
    
    
    public class VideoStitcherServiceSettings extends ClientSettings<VideoStitcherServiceSettings>

Settings class to configure an instance of [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (videostitcher.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getCdnKey:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoStitcherServiceSettings.Builder videoStitcherServiceSettingsBuilder =
         VideoStitcherServiceSettings.newBuilder();
     videoStitcherServiceSettingsBuilder
         .getCdnKeySettings()
         .setRetrySettings(
             videoStitcherServiceSettingsBuilder
                 .getCdnKeySettings()
                 .getRetrySettings()
                 .toBuilder()
                 .setInitialRetryDelayDuration(Duration.ofSeconds(1))
                 .setInitialRpcTimeoutDuration(Duration.ofSeconds(5))
                 .setMaxAttempts(5)
                 .setMaxRetryDelayDuration(Duration.ofSeconds(30))
                 .setMaxRpcTimeoutDuration(Duration.ofSeconds(60))
                 .setRetryDelayMultiplier(1.3)
                 .setRpcTimeoutMultiplier(1.5)
                 .setTotalTimeoutDuration(Duration.ofSeconds(300))
                 .build());
     VideoStitcherServiceSettings videoStitcherServiceSettings =
         videoStitcherServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createCdnKey:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VideoStitcherServiceSettings.Builder videoStitcherServiceSettingsBuilder =
         VideoStitcherServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     videoStitcherServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > VideoStitcherServiceSettings

## Inherited Members

[ClientSettings.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

[ClientSettings.getApiKey()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getApiKey__)

[ClientSettings.getBackgroundExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getBackgroundExecutorProvider__)

[ClientSettings.getClock()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getClock__)

[ClientSettings.getCredentialsProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getCredentialsProvider__)

[ClientSettings.getEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getEndpoint__)

[ClientSettings.getExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getExecutorProvider__)

[ClientSettings.getGdchApiAudience()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getGdchApiAudience__)

[ClientSettings.getHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getHeaderProvider__)

[ClientSettings.getInternalHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getInternalHeaderProvider__)

[ClientSettings.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getQuotaProjectId__)

[ClientSettings.getStubSettings()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getStubSettings__)

[ClientSettings.getTransportChannelProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getTransportChannelProvider__)

[ClientSettings.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getUniverseDomain__)

[ClientSettings.getWatchdogCheckInterval()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckInterval__)

[ClientSettings.getWatchdogCheckIntervalDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckIntervalDuration__)

[ClientSettings.getWatchdogProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogProvider__)

[ClientSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### create(VideoStitcherServiceStubSettings stub)
    
    
    public static final VideoStitcherServiceSettings create(VideoStitcherServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VideoStitcherServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.stub.VideoStitcherServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### defaultApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultCredentialsProviderBuilder()
    
    
    public static GoogleCredentialsProvider.Builder defaultCredentialsProviderBuilder()

Returns a builder for the default credentials for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.GoogleCredentialsProvider.Builder.html)` |   
  
### defaultExecutorProviderBuilder()
    
    
    public static InstantiatingExecutorProvider.Builder defaultExecutorProviderBuilder()

Returns a builder for the default ExecutorProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider()
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint()
    
    
    public static String getDefaultEndpoint()

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultServiceScopes()
    
    
    public static List<String> getDefaultServiceScopes()

Returns the default service scopes.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### newBuilder()
    
    
    public static VideoStitcherServiceSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static VideoStitcherServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings.Builder)` |   
  
## Constructors 

### VideoStitcherServiceSettings(VideoStitcherServiceSettings.Builder settingsBuilder)
    
    
    protected VideoStitcherServiceSettings(VideoStitcherServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[VideoStitcherServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings.Builder)`  
  
  
## Methods 

### createCdnKeyOperationSettings()
    
    
    public OperationCallSettings<CreateCdnKeyRequest,CdnKey,OperationMetadata> createCdnKeyOperationSettings()

Returns the object with the settings used for calls to createCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createCdnKeySettings()
    
    
    public UnaryCallSettings<CreateCdnKeyRequest,Operation> createCdnKeySettings()

Returns the object with the settings used for calls to createCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLiveConfigOperationSettings()
    
    
    public OperationCallSettings<CreateLiveConfigRequest,LiveConfig,OperationMetadata> createLiveConfigOperationSettings()

Returns the object with the settings used for calls to createLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createLiveConfigSettings()
    
    
    public UnaryCallSettings<CreateLiveConfigRequest,Operation> createLiveConfigSettings()

Returns the object with the settings used for calls to createLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLiveSessionSettings()
    
    
    public UnaryCallSettings<CreateLiveSessionRequest,LiveSession> createLiveSessionSettings()

Returns the object with the settings used for calls to createLiveSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### createSlateOperationSettings()
    
    
    public OperationCallSettings<CreateSlateRequest,Slate,OperationMetadata> createSlateOperationSettings()

Returns the object with the settings used for calls to createSlate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createSlateSettings()
    
    
    public UnaryCallSettings<CreateSlateRequest,Operation> createSlateSettings()

Returns the object with the settings used for calls to createSlate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVodConfigOperationSettings()
    
    
    public OperationCallSettings<CreateVodConfigRequest,VodConfig,OperationMetadata> createVodConfigOperationSettings()

Returns the object with the settings used for calls to createVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### createVodConfigSettings()
    
    
    public UnaryCallSettings<CreateVodConfigRequest,Operation> createVodConfigSettings()

Returns the object with the settings used for calls to createVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVodSessionSettings()
    
    
    public UnaryCallSettings<CreateVodSessionRequest,VodSession> createVodSessionSettings()

Returns the object with the settings used for calls to createVodSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### deleteCdnKeyOperationSettings()
    
    
    public OperationCallSettings<DeleteCdnKeyRequest,Empty,OperationMetadata> deleteCdnKeyOperationSettings()

Returns the object with the settings used for calls to deleteCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteCdnKeySettings()
    
    
    public UnaryCallSettings<DeleteCdnKeyRequest,Operation> deleteCdnKeySettings()

Returns the object with the settings used for calls to deleteCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLiveConfigOperationSettings()
    
    
    public OperationCallSettings<DeleteLiveConfigRequest,Empty,OperationMetadata> deleteLiveConfigOperationSettings()

Returns the object with the settings used for calls to deleteLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteLiveConfigSettings()
    
    
    public UnaryCallSettings<DeleteLiveConfigRequest,Operation> deleteLiveConfigSettings()

Returns the object with the settings used for calls to deleteLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSlateOperationSettings()
    
    
    public OperationCallSettings<DeleteSlateRequest,Empty,OperationMetadata> deleteSlateOperationSettings()

Returns the object with the settings used for calls to deleteSlate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteSlateSettings()
    
    
    public UnaryCallSettings<DeleteSlateRequest,Operation> deleteSlateSettings()

Returns the object with the settings used for calls to deleteSlate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVodConfigOperationSettings()
    
    
    public OperationCallSettings<DeleteVodConfigRequest,Empty,OperationMetadata> deleteVodConfigOperationSettings()

Returns the object with the settings used for calls to deleteVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### deleteVodConfigSettings()
    
    
    public UnaryCallSettings<DeleteVodConfigRequest,Operation> deleteVodConfigSettings()

Returns the object with the settings used for calls to deleteVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCdnKeySettings()
    
    
    public UnaryCallSettings<GetCdnKeyRequest,CdnKey> getCdnKeySettings()

Returns the object with the settings used for calls to getCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey)>` |   
  
### getLiveAdTagDetailSettings()
    
    
    public UnaryCallSettings<GetLiveAdTagDetailRequest,LiveAdTagDetail> getLiveAdTagDetailSettings()

Returns the object with the settings used for calls to getLiveAdTagDetail.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLiveAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveAdTagDetailRequest),[LiveAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveAdTagDetail)>` |   
  
### getLiveConfigSettings()
    
    
    public UnaryCallSettings<GetLiveConfigRequest,LiveConfig> getLiveConfigSettings()

Returns the object with the settings used for calls to getLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig)>` |   
  
### getLiveSessionSettings()
    
    
    public UnaryCallSettings<GetLiveSessionRequest,LiveSession> getLiveSessionSettings()

Returns the object with the settings used for calls to getLiveSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLiveSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetLiveSessionRequest),[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)>` |   
  
### getSlateSettings()
    
    
    public UnaryCallSettings<GetSlateRequest,Slate> getSlateSettings()

Returns the object with the settings used for calls to getSlate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate)>` |   
  
### getVodAdTagDetailSettings()
    
    
    public UnaryCallSettings<GetVodAdTagDetailRequest,VodAdTagDetail> getVodAdTagDetailSettings()

Returns the object with the settings used for calls to getVodAdTagDetail.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVodAdTagDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodAdTagDetailRequest),[VodAdTagDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodAdTagDetail)>` |   
  
### getVodConfigSettings()
    
    
    public UnaryCallSettings<GetVodConfigRequest,VodConfig> getVodConfigSettings()

Returns the object with the settings used for calls to getVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig)>` |   
  
### getVodSessionSettings()
    
    
    public UnaryCallSettings<GetVodSessionRequest,VodSession> getVodSessionSettings()

Returns the object with the settings used for calls to getVodSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVodSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodSessionRequest),[VodSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodSession)>` |   
  
### getVodStitchDetailSettings()
    
    
    public UnaryCallSettings<GetVodStitchDetailRequest,VodStitchDetail> getVodStitchDetailSettings()

Returns the object with the settings used for calls to getVodStitchDetail.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVodStitchDetailRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GetVodStitchDetailRequest),[VodStitchDetail](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodStitchDetail)>` |   
  
### listCdnKeysSettings()
    
    
    public PagedCallSettings<ListCdnKeysRequest,ListCdnKeysResponse,VideoStitcherServiceClient.ListCdnKeysPagedResponse> listCdnKeysSettings()

Returns the object with the settings used for calls to listCdnKeys.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCdnKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysRequest),[ListCdnKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListCdnKeysResponse),[ListCdnKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListCdnKeysPagedResponse)>` |   
  
### listLiveAdTagDetailsSettings()
    
    
    public PagedCallSettings<ListLiveAdTagDetailsRequest,ListLiveAdTagDetailsResponse,VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse> listLiveAdTagDetailsSettings()

Returns the object with the settings used for calls to listLiveAdTagDetails.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListLiveAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsRequest),[ListLiveAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveAdTagDetailsResponse),[ListLiveAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveAdTagDetailsPagedResponse)>` |   
  
### listLiveConfigsSettings()
    
    
    public PagedCallSettings<ListLiveConfigsRequest,ListLiveConfigsResponse,VideoStitcherServiceClient.ListLiveConfigsPagedResponse> listLiveConfigsSettings()

Returns the object with the settings used for calls to listLiveConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListLiveConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsRequest),[ListLiveConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListLiveConfigsResponse),[ListLiveConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListLiveConfigsPagedResponse)>` |   
  
### listSlatesSettings()
    
    
    public PagedCallSettings<ListSlatesRequest,ListSlatesResponse,VideoStitcherServiceClient.ListSlatesPagedResponse> listSlatesSettings()

Returns the object with the settings used for calls to listSlates.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSlatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesRequest),[ListSlatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListSlatesResponse),[ListSlatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListSlatesPagedResponse)>` |   
  
### listVodAdTagDetailsSettings()
    
    
    public PagedCallSettings<ListVodAdTagDetailsRequest,ListVodAdTagDetailsResponse,VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse> listVodAdTagDetailsSettings()

Returns the object with the settings used for calls to listVodAdTagDetails.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVodAdTagDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsRequest),[ListVodAdTagDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodAdTagDetailsResponse),[ListVodAdTagDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodAdTagDetailsPagedResponse)>` |   
  
### listVodConfigsSettings()
    
    
    public PagedCallSettings<ListVodConfigsRequest,ListVodConfigsResponse,VideoStitcherServiceClient.ListVodConfigsPagedResponse> listVodConfigsSettings()

Returns the object with the settings used for calls to listVodConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVodConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsRequest),[ListVodConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodConfigsResponse),[ListVodConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodConfigsPagedResponse)>` |   
  
### listVodStitchDetailsSettings()
    
    
    public PagedCallSettings<ListVodStitchDetailsRequest,ListVodStitchDetailsResponse,VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse> listVodStitchDetailsSettings()

Returns the object with the settings used for calls to listVodStitchDetails.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVodStitchDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsRequest),[ListVodStitchDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ListVodStitchDetailsResponse),[ListVodStitchDetailsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.ListVodStitchDetailsPagedResponse)>` |   
  
### toBuilder()
    
    
    public VideoStitcherServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[VideoStitcherServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateCdnKeyOperationSettings()
    
    
    public OperationCallSettings<UpdateCdnKeyRequest,CdnKey,OperationMetadata> updateCdnKeyOperationSettings()

Returns the object with the settings used for calls to updateCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateCdnKeySettings()
    
    
    public UnaryCallSettings<UpdateCdnKeyRequest,Operation> updateCdnKeySettings()

Returns the object with the settings used for calls to updateCdnKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateCdnKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLiveConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateLiveConfigRequest,LiveConfig,OperationMetadata> updateLiveConfigOperationSettings()

Returns the object with the settings used for calls to updateLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[LiveConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateLiveConfigSettings()
    
    
    public UnaryCallSettings<UpdateLiveConfigRequest,Operation> updateLiveConfigSettings()

Returns the object with the settings used for calls to updateLiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateLiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateLiveConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSlateOperationSettings()
    
    
    public OperationCallSettings<UpdateSlateRequest,Slate,OperationMetadata> updateSlateOperationSettings()

Returns the object with the settings used for calls to updateSlate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateSlateSettings()
    
    
    public UnaryCallSettings<UpdateSlateRequest,Operation> updateSlateSettings()

Returns the object with the settings used for calls to updateSlate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateSlateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVodConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateVodConfigRequest,VodConfig,OperationMetadata> updateVodConfigOperationSettings()

Returns the object with the settings used for calls to updateVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[VodConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VodConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.OperationMetadata)>` |   
  
### updateVodConfigSettings()
    
    
    public UnaryCallSettings<UpdateVodConfigRequest,Operation> updateVodConfigSettings()

Returns the object with the settings used for calls to updateVodConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateVodConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.UpdateVodConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
