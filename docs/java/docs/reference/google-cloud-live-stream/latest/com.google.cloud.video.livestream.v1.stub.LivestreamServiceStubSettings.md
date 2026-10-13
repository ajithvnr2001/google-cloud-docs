---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings
title: Class LivestreamServiceStubSettings (0.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:45.748501+00:00
---

# Class LivestreamServiceStubSettings (0.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LivestreamServiceStubSettings (0.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.101.0 (latest)  0.97.0  0.96.0  0.95.0  0.93.0  0.90.0  0.89.0  0.87.0  0.85.0  0.84.0  0.82.0  0.80.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.72.0  0.70.0  0.69.0  0.66.0  0.65.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.8  0.3.0 
    
    
    public class LivestreamServiceStubSettings extends StubSettings<LivestreamServiceStubSettings>

Settings class to configure an instance of [LivestreamServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (livestream.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getChannel:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LivestreamServiceStubSettings.Builder livestreamServiceSettingsBuilder =
         LivestreamServiceStubSettings.newBuilder();
     livestreamServiceSettingsBuilder
         .getChannelSettings()
         .setRetrySettings(
             livestreamServiceSettingsBuilder
                 .getChannelSettings()
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
     LivestreamServiceStubSettings livestreamServiceSettings =
         livestreamServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createChannel:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LivestreamServiceStubSettings.Builder livestreamServiceSettingsBuilder =
         LivestreamServiceStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     livestreamServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > LivestreamServiceStubSettings

## Inherited Members

[StubSettings.getApiKey()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getApiKey__)

[StubSettings.getBackgroundExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getBackgroundExecutorProvider__)

[StubSettings.getClock()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getClock__)

[StubSettings.getCredentialsProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getCredentialsProvider__)

[StubSettings.getEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getEndpoint__)

[StubSettings.getExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getExecutorProvider__)

[StubSettings.getGdchApiAudience()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getGdchApiAudience__)

[StubSettings.getHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getHeaderProvider__)

[StubSettings.getInternalHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getInternalHeaderProvider__)

[StubSettings.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

[StubSettings.getMtlsEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getMtlsEndpoint__)

[StubSettings.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getQuotaProjectId__)

[StubSettings.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

[StubSettings.getStreamWatchdogCheckInterval()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogCheckInterval__)

[StubSettings.getStreamWatchdogCheckIntervalDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogCheckIntervalDuration__)

[StubSettings.getStreamWatchdogProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogProvider__)

[StubSettings.getTracerFactory()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getTracerFactory__)

[StubSettings.getTransportChannelProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getTransportChannelProvider__)

[StubSettings.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getUniverseDomain__)

[StubSettings.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

[StubSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toString__)

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
  
### defaultGrpcApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultGrpcApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultHttpJsonApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultHttpJsonTransportProviderBuilder()
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a builder for the default REST ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider()
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint()
    
    
    public static String getDefaultEndpoint()

**Obsolete**

_Use getEndpoint() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultMtlsEndpoint()
    
    
    public static String getDefaultMtlsEndpoint()

Returns the default mTLS service endpoint.

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
    
    
    public static LivestreamServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static LivestreamServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static LivestreamServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings.Builder)` |   
  
## Constructors 

### LivestreamServiceStubSettings(LivestreamServiceStubSettings.Builder settingsBuilder)
    
    
    protected LivestreamServiceStubSettings(LivestreamServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[LivestreamServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings.Builder)`  
  
  
## Methods 

### createAssetOperationSettings()
    
    
    public OperationCallSettings<CreateAssetRequest,Asset,OperationMetadata> createAssetOperationSettings()

Returns the object with the settings used for calls to createAsset.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### createAssetSettings()
    
    
    public UnaryCallSettings<CreateAssetRequest,Operation> createAssetSettings()

Returns the object with the settings used for calls to createAsset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createChannelOperationSettings()
    
    
    public OperationCallSettings<CreateChannelRequest,Channel,OperationMetadata> createChannelOperationSettings()

Returns the object with the settings used for calls to createChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### createChannelSettings()
    
    
    public UnaryCallSettings<CreateChannelRequest,Operation> createChannelSettings()

Returns the object with the settings used for calls to createChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClipOperationSettings()
    
    
    public OperationCallSettings<CreateClipRequest,Clip,OperationMetadata> createClipOperationSettings()

Returns the object with the settings used for calls to createClip.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequest),[Clip](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Clip),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### createClipSettings()
    
    
    public UnaryCallSettings<CreateClipRequest,Operation> createClipSettings()

Returns the object with the settings used for calls to createClip.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateClipRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDvrSessionOperationSettings()
    
    
    public OperationCallSettings<CreateDvrSessionRequest,DvrSession,OperationMetadata> createDvrSessionOperationSettings()

Returns the object with the settings used for calls to createDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateDvrSessionRequest),[DvrSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DvrSession),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### createDvrSessionSettings()
    
    
    public UnaryCallSettings<CreateDvrSessionRequest,Operation> createDvrSessionSettings()

Returns the object with the settings used for calls to createDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEventSettings()
    
    
    public UnaryCallSettings<CreateEventRequest,Event> createEventSettings()

Returns the object with the settings used for calls to createEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)>` |   
  
### createInputOperationSettings()
    
    
    public OperationCallSettings<CreateInputRequest,Input,OperationMetadata> createInputOperationSettings()

Returns the object with the settings used for calls to createInput.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateInputRequest),[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Input),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### createInputSettings()
    
    
    public UnaryCallSettings<CreateInputRequest,Operation> createInputSettings()

Returns the object with the settings used for calls to createInput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public LivestreamServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteAssetOperationSettings()
    
    
    public OperationCallSettings<DeleteAssetRequest,Empty,OperationMetadata> deleteAssetOperationSettings()

Returns the object with the settings used for calls to deleteAsset.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteAssetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### deleteAssetSettings()
    
    
    public UnaryCallSettings<DeleteAssetRequest,Operation> deleteAssetSettings()

Returns the object with the settings used for calls to deleteAsset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteChannelOperationSettings()
    
    
    public OperationCallSettings<DeleteChannelRequest,Empty,OperationMetadata> deleteChannelOperationSettings()

Returns the object with the settings used for calls to deleteChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteChannelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### deleteChannelSettings()
    
    
    public UnaryCallSettings<DeleteChannelRequest,Operation> deleteChannelSettings()

Returns the object with the settings used for calls to deleteChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClipOperationSettings()
    
    
    public OperationCallSettings<DeleteClipRequest,Empty,OperationMetadata> deleteClipOperationSettings()

Returns the object with the settings used for calls to deleteClip.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteClipRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### deleteClipSettings()
    
    
    public UnaryCallSettings<DeleteClipRequest,Operation> deleteClipSettings()

Returns the object with the settings used for calls to deleteClip.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteClipRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDvrSessionOperationSettings()
    
    
    public OperationCallSettings<DeleteDvrSessionRequest,Empty,OperationMetadata> deleteDvrSessionOperationSettings()

Returns the object with the settings used for calls to deleteDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteDvrSessionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### deleteDvrSessionSettings()
    
    
    public UnaryCallSettings<DeleteDvrSessionRequest,Operation> deleteDvrSessionSettings()

Returns the object with the settings used for calls to deleteDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEventSettings()
    
    
    public UnaryCallSettings<DeleteEventRequest,Empty> deleteEventSettings()

Returns the object with the settings used for calls to deleteEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteEventRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteInputOperationSettings()
    
    
    public OperationCallSettings<DeleteInputRequest,Empty,OperationMetadata> deleteInputOperationSettings()

Returns the object with the settings used for calls to deleteInput.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### deleteInputSettings()
    
    
    public UnaryCallSettings<DeleteInputRequest,Operation> deleteInputSettings()

Returns the object with the settings used for calls to deleteInput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAssetSettings()
    
    
    public UnaryCallSettings<GetAssetRequest,Asset> getAssetSettings()

Returns the object with the settings used for calls to getAsset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset)>` |   
  
### getChannelSettings()
    
    
    public UnaryCallSettings<GetChannelRequest,Channel> getChannelSettings()

Returns the object with the settings used for calls to getChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel)>` |   
  
### getClipSettings()
    
    
    public UnaryCallSettings<GetClipRequest,Clip> getClipSettings()

Returns the object with the settings used for calls to getClip.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetClipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetClipRequest),[Clip](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Clip)>` |   
  
### getDvrSessionSettings()
    
    
    public UnaryCallSettings<GetDvrSessionRequest,DvrSession> getDvrSessionSettings()

Returns the object with the settings used for calls to getDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetDvrSessionRequest),[DvrSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DvrSession)>` |   
  
### getEventSettings()
    
    
    public UnaryCallSettings<GetEventRequest,Event> getEventSettings()

Returns the object with the settings used for calls to getEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetEventRequest),[Event](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Event)>` |   
  
### getInputSettings()
    
    
    public UnaryCallSettings<GetInputRequest,Input> getInputSettings()

Returns the object with the settings used for calls to getInput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetInputRequest),[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Input)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getPoolSettings()
    
    
    public UnaryCallSettings<GetPoolRequest,Pool> getPoolSettings()

Returns the object with the settings used for calls to getPool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.GetPoolRequest),[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listAssetsSettings()
    
    
    public PagedCallSettings<ListAssetsRequest,ListAssetsResponse,LivestreamServiceClient.ListAssetsPagedResponse> listAssetsSettings()

Returns the object with the settings used for calls to listAssets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsRequest),[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListAssetsResponse),[ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListAssetsPagedResponse)>` |   
  
### listChannelsSettings()
    
    
    public PagedCallSettings<ListChannelsRequest,ListChannelsResponse,LivestreamServiceClient.ListChannelsPagedResponse> listChannelsSettings()

Returns the object with the settings used for calls to listChannels.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsRequest),[ListChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListChannelsResponse),[ListChannelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListChannelsPagedResponse)>` |   
  
### listClipsSettings()
    
    
    public PagedCallSettings<ListClipsRequest,ListClipsResponse,LivestreamServiceClient.ListClipsPagedResponse> listClipsSettings()

Returns the object with the settings used for calls to listClips.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListClipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsRequest),[ListClipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListClipsResponse),[ListClipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListClipsPagedResponse)>` |   
  
### listDvrSessionsSettings()
    
    
    public PagedCallSettings<ListDvrSessionsRequest,ListDvrSessionsResponse,LivestreamServiceClient.ListDvrSessionsPagedResponse> listDvrSessionsSettings()

Returns the object with the settings used for calls to listDvrSessions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDvrSessionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsRequest),[ListDvrSessionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListDvrSessionsResponse),[ListDvrSessionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListDvrSessionsPagedResponse)>` |   
  
### listEventsSettings()
    
    
    public PagedCallSettings<ListEventsRequest,ListEventsResponse,LivestreamServiceClient.ListEventsPagedResponse> listEventsSettings()

Returns the object with the settings used for calls to listEvents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsRequest),[ListEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListEventsResponse),[ListEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListEventsPagedResponse)>` |   
  
### listInputsSettings()
    
    
    public PagedCallSettings<ListInputsRequest,ListInputsResponse,LivestreamServiceClient.ListInputsPagedResponse> listInputsSettings()

Returns the object with the settings used for calls to listInputs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInputsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsRequest),[ListInputsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ListInputsResponse),[ListInputsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListInputsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,LivestreamServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.ListLocationsPagedResponse)>` |   
  
### previewInputSettings()
    
    
    public UnaryCallSettings<PreviewInputRequest,PreviewInputResponse> previewInputSettings()

Returns the object with the settings used for calls to previewInput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PreviewInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputRequest),[PreviewInputResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PreviewInputResponse)>` |   
  
### startChannelOperationSettings()
    
    
    public OperationCallSettings<StartChannelRequest,ChannelOperationResponse,OperationMetadata> startChannelOperationSettings()

Returns the object with the settings used for calls to startChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartChannelRequest),[ChannelOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelOperationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### startChannelSettings()
    
    
    public UnaryCallSettings<StartChannelRequest,Operation> startChannelSettings()

Returns the object with the settings used for calls to startChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startDistributionOperationSettings()
    
    
    public OperationCallSettings<StartDistributionRequest,ChannelOperationResponse,OperationMetadata> startDistributionOperationSettings()

Returns the object with the settings used for calls to startDistribution.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartDistributionRequest),[ChannelOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelOperationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### startDistributionSettings()
    
    
    public UnaryCallSettings<StartDistributionRequest,Operation> startDistributionSettings()

Returns the object with the settings used for calls to startDistribution.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StartDistributionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopChannelOperationSettings()
    
    
    public OperationCallSettings<StopChannelRequest,ChannelOperationResponse,OperationMetadata> stopChannelOperationSettings()

Returns the object with the settings used for calls to stopChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopChannelRequest),[ChannelOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelOperationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### stopChannelSettings()
    
    
    public UnaryCallSettings<StopChannelRequest,Operation> stopChannelSettings()

Returns the object with the settings used for calls to stopChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopDistributionOperationSettings()
    
    
    public OperationCallSettings<StopDistributionRequest,ChannelOperationResponse,OperationMetadata> stopDistributionOperationSettings()

Returns the object with the settings used for calls to stopDistribution.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopDistributionRequest),[ChannelOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.ChannelOperationResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### stopDistributionSettings()
    
    
    public UnaryCallSettings<StopDistributionRequest,Operation> stopDistributionSettings()

Returns the object with the settings used for calls to stopDistribution.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopDistributionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.StopDistributionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder()
    
    
    public LivestreamServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[LivestreamServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.stub.LivestreamServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateChannelOperationSettings()
    
    
    public OperationCallSettings<UpdateChannelRequest,Channel,OperationMetadata> updateChannelOperationSettings()

Returns the object with the settings used for calls to updateChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateChannelRequest),[Channel](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Channel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### updateChannelSettings()
    
    
    public UnaryCallSettings<UpdateChannelRequest,Operation> updateChannelSettings()

Returns the object with the settings used for calls to updateChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDvrSessionOperationSettings()
    
    
    public OperationCallSettings<UpdateDvrSessionRequest,DvrSession,OperationMetadata> updateDvrSessionOperationSettings()

Returns the object with the settings used for calls to updateDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateDvrSessionRequest),[DvrSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DvrSession),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### updateDvrSessionSettings()
    
    
    public UnaryCallSettings<UpdateDvrSessionRequest,Operation> updateDvrSessionSettings()

Returns the object with the settings used for calls to updateDvrSession.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateDvrSessionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateDvrSessionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInputOperationSettings()
    
    
    public OperationCallSettings<UpdateInputRequest,Input,OperationMetadata> updateInputOperationSettings()

Returns the object with the settings used for calls to updateInput.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateInputRequest),[Input](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Input),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### updateInputSettings()
    
    
    public UnaryCallSettings<UpdateInputRequest,Operation> updateInputSettings()

Returns the object with the settings used for calls to updateInput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdateInputRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePoolOperationSettings()
    
    
    public OperationCallSettings<UpdatePoolRequest,Pool,OperationMetadata> updatePoolOperationSettings()

Returns the object with the settings used for calls to updatePool.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest),[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.OperationMetadata)>` |   
  
### updatePoolSettings()
    
    
    public UnaryCallSettings<UpdatePoolRequest,Operation> updatePoolSettings()

Returns the object with the settings used for calls to updatePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
