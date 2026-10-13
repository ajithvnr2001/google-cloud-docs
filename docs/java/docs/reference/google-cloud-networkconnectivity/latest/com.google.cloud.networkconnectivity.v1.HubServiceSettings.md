---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings
title: Class HubServiceSettings (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:08.536553+00:00
---

# Class HubServiceSettings (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HubServiceSettings (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 
    
    
    public class HubServiceSettings extends ClientSettings<HubServiceSettings>

Settings class to configure an instance of [HubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.HubServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (networkconnectivity.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getHub:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HubServiceSettings.Builder hubServiceSettingsBuilder = HubServiceSettings.newBuilder();
     hubServiceSettingsBuilder
         .getHubSettings()
         .setRetrySettings(
             hubServiceSettingsBuilder
                 .getHubSettings()
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
     HubServiceSettings hubServiceSettings = hubServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createHub:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HubServiceSettings.Builder hubServiceSettingsBuilder = HubServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     hubServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > HubServiceSettings

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

### create(HubServiceStubSettings stub)
    
    
    public static final HubServiceSettings create(HubServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HubServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.stub.HubServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings)` |   
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
    
    
    public static HubServiceSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static HubServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings.Builder)` |   
  
## Constructors 

### HubServiceSettings(HubServiceSettings.Builder settingsBuilder)
    
    
    protected HubServiceSettings(HubServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[HubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings.Builder)`  
  
  
## Methods 

### acceptHubSpokeOperationSettings()
    
    
    public OperationCallSettings<AcceptHubSpokeRequest,AcceptHubSpokeResponse,OperationMetadata> acceptHubSpokeOperationSettings()

Returns the object with the settings used for calls to acceptHubSpoke.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeRequest),[AcceptHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptHubSpokeSettings()
    
    
    public UnaryCallSettings<AcceptHubSpokeRequest,Operation> acceptHubSpokeSettings()

Returns the object with the settings used for calls to acceptHubSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AcceptHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### acceptSpokeUpdateOperationSettings()
    
    
    public OperationCallSettings<AcceptSpokeUpdateRequest,AcceptSpokeUpdateResponse,OperationMetadata> acceptSpokeUpdateOperationSettings()

Returns the object with the settings used for calls to acceptSpokeUpdate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateRequest),[AcceptSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### acceptSpokeUpdateSettings()
    
    
    public UnaryCallSettings<AcceptSpokeUpdateRequest,Operation> acceptSpokeUpdateSettings()

Returns the object with the settings used for calls to acceptSpokeUpdate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AcceptSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.AcceptSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHubOperationSettings()
    
    
    public OperationCallSettings<CreateHubRequest,Hub,OperationMetadata> createHubOperationSettings()

Returns the object with the settings used for calls to createHub.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createHubSettings()
    
    
    public UnaryCallSettings<CreateHubRequest,Operation> createHubSettings()

Returns the object with the settings used for calls to createHub.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSpokeOperationSettings()
    
    
    public OperationCallSettings<CreateSpokeRequest,Spoke,OperationMetadata> createSpokeOperationSettings()

Returns the object with the settings used for calls to createSpoke.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### createSpokeSettings()
    
    
    public UnaryCallSettings<CreateSpokeRequest,Operation> createSpokeSettings()

Returns the object with the settings used for calls to createSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.CreateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHubOperationSettings()
    
    
    public OperationCallSettings<DeleteHubRequest,Empty,OperationMetadata> deleteHubOperationSettings()

Returns the object with the settings used for calls to deleteHub.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteHubRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteHubSettings()
    
    
    public UnaryCallSettings<DeleteHubRequest,Operation> deleteHubSettings()

Returns the object with the settings used for calls to deleteHub.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSpokeOperationSettings()
    
    
    public OperationCallSettings<DeleteSpokeRequest,Empty,OperationMetadata> deleteSpokeOperationSettings()

Returns the object with the settings used for calls to deleteSpoke.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteSpokeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### deleteSpokeSettings()
    
    
    public UnaryCallSettings<DeleteSpokeRequest,Operation> deleteSpokeSettings()

Returns the object with the settings used for calls to deleteSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.DeleteSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGroupSettings()
    
    
    public UnaryCallSettings<GetGroupRequest,Group> getGroupSettings()

Returns the object with the settings used for calls to getGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group)>` |   
  
### getHubSettings()
    
    
    public UnaryCallSettings<GetHubRequest,Hub> getHubSettings()

Returns the object with the settings used for calls to getHub.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getRouteSettings()
    
    
    public UnaryCallSettings<GetRouteRequest,Route> getRouteSettings()

Returns the object with the settings used for calls to getRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Route)>` |   
  
### getRouteTableSettings()
    
    
    public UnaryCallSettings<GetRouteTableRequest,RouteTable> getRouteTableSettings()

Returns the object with the settings used for calls to getRouteTable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRouteTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetRouteTableRequest),[RouteTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RouteTable)>` |   
  
### getSpokeSettings()
    
    
    public UnaryCallSettings<GetSpokeRequest,Spoke> getSpokeSettings()

Returns the object with the settings used for calls to getSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.GetSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke)>` |   
  
### listGroupsSettings()
    
    
    public PagedCallSettings<ListGroupsRequest,ListGroupsResponse,HubServiceClient.ListGroupsPagedResponse> listGroupsSettings()

Returns the object with the settings used for calls to listGroups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsRequest),[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListGroupsResponse),[ListGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListGroupsPagedResponse)>` |   
  
### listHubSpokesSettings()
    
    
    public PagedCallSettings<ListHubSpokesRequest,ListHubSpokesResponse,HubServiceClient.ListHubSpokesPagedResponse> listHubSpokesSettings()

Returns the object with the settings used for calls to listHubSpokes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHubSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesRequest),[ListHubSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubSpokesResponse),[ListHubSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubSpokesPagedResponse)>` |   
  
### listHubsSettings()
    
    
    public PagedCallSettings<ListHubsRequest,ListHubsResponse,HubServiceClient.ListHubsPagedResponse> listHubsSettings()

Returns the object with the settings used for calls to listHubs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHubsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsRequest),[ListHubsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListHubsResponse),[ListHubsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListHubsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,HubServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListLocationsPagedResponse)>` |   
  
### listRouteTablesSettings()
    
    
    public PagedCallSettings<ListRouteTablesRequest,ListRouteTablesResponse,HubServiceClient.ListRouteTablesPagedResponse> listRouteTablesSettings()

Returns the object with the settings used for calls to listRouteTables.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRouteTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesRequest),[ListRouteTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRouteTablesResponse),[ListRouteTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRouteTablesPagedResponse)>` |   
  
### listRoutesSettings()
    
    
    public PagedCallSettings<ListRoutesRequest,ListRoutesResponse,HubServiceClient.ListRoutesPagedResponse> listRoutesSettings()

Returns the object with the settings used for calls to listRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesRequest),[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListRoutesResponse),[ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListRoutesPagedResponse)>` |   
  
### listSpokesSettings()
    
    
    public PagedCallSettings<ListSpokesRequest,ListSpokesResponse,HubServiceClient.ListSpokesPagedResponse> listSpokesSettings()

Returns the object with the settings used for calls to listSpokes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSpokesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesRequest),[ListSpokesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.ListSpokesResponse),[ListSpokesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.ListSpokesPagedResponse)>` |   
  
### queryHubStatusSettings()
    
    
    public PagedCallSettings<QueryHubStatusRequest,QueryHubStatusResponse,HubServiceClient.QueryHubStatusPagedResponse> queryHubStatusSettings()

Returns the object with the settings used for calls to queryHubStatus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryHubStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusRequest),[QueryHubStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.QueryHubStatusResponse),[QueryHubStatusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceClient.QueryHubStatusPagedResponse)>` |   
  
### rejectHubSpokeOperationSettings()
    
    
    public OperationCallSettings<RejectHubSpokeRequest,RejectHubSpokeResponse,OperationMetadata> rejectHubSpokeOperationSettings()

Returns the object with the settings used for calls to rejectHubSpoke.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeRequest),[RejectHubSpokeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectHubSpokeSettings()
    
    
    public UnaryCallSettings<RejectHubSpokeRequest,Operation> rejectHubSpokeSettings()

Returns the object with the settings used for calls to rejectHubSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RejectHubSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectHubSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rejectSpokeUpdateOperationSettings()
    
    
    public OperationCallSettings<RejectSpokeUpdateRequest,RejectSpokeUpdateResponse,OperationMetadata> rejectSpokeUpdateOperationSettings()

Returns the object with the settings used for calls to rejectSpokeUpdate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateRequest),[RejectSpokeUpdateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### rejectSpokeUpdateSettings()
    
    
    public UnaryCallSettings<RejectSpokeUpdateRequest,Operation> rejectSpokeUpdateSettings()

Returns the object with the settings used for calls to rejectSpokeUpdate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RejectSpokeUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.RejectSpokeUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public HubServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[HubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.HubServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateGroupOperationSettings()
    
    
    public OperationCallSettings<UpdateGroupRequest,Group,OperationMetadata> updateGroupOperationSettings()

Returns the object with the settings used for calls to updateGroup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateGroupRequest),[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Group),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateGroupSettings()
    
    
    public UnaryCallSettings<UpdateGroupRequest,Operation> updateGroupSettings()

Returns the object with the settings used for calls to updateGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHubOperationSettings()
    
    
    public OperationCallSettings<UpdateHubRequest,Hub,OperationMetadata> updateHubOperationSettings()

Returns the object with the settings used for calls to updateHub.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateHubRequest),[Hub](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Hub),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateHubSettings()
    
    
    public UnaryCallSettings<UpdateHubRequest,Operation> updateHubSettings()

Returns the object with the settings used for calls to updateHub.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHubRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateHubRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSpokeOperationSettings()
    
    
    public OperationCallSettings<UpdateSpokeRequest,Spoke,OperationMetadata> updateSpokeOperationSettings()

Returns the object with the settings used for calls to updateSpoke.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateSpokeRequest),[Spoke](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.Spoke),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.OperationMetadata)>` |   
  
### updateSpokeSettings()
    
    
    public UnaryCallSettings<UpdateSpokeRequest,Operation> updateSpokeSettings()

Returns the object with the settings used for calls to updateSpoke.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSpokeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1.UpdateSpokeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
