---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings
title: Class TransportManagerSettings (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:31.792383+00:00
---

# Class TransportManagerSettings (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransportManagerSettings (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.9  1.1.1  1.0.0  0.5.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class TransportManagerSettings extends ClientSettings<TransportManagerSettings>

Settings class to configure an instance of [TransportManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerClient).

The default instance has everything set to sensible defaults:

  * The default service address (networkconnectivity.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getRemoteTransportProfile:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TransportManagerSettings.Builder transportManagerSettingsBuilder =
         TransportManagerSettings.newBuilder();
     transportManagerSettingsBuilder
         .getRemoteTransportProfileSettings()
         .setRetrySettings(
             transportManagerSettingsBuilder
                 .getRemoteTransportProfileSettings()
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
     TransportManagerSettings transportManagerSettings = transportManagerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createTransport:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TransportManagerSettings.Builder transportManagerSettingsBuilder =
         TransportManagerSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     transportManagerSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > TransportManagerSettings

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

### create(TransportManagerStubSettings stub)
    
    
    public static final TransportManagerSettings create(TransportManagerStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TransportManagerStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.stub.TransportManagerStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings)` |   
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
    
    
    public static TransportManagerSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[TransportManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static TransportManagerSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings.Builder)` |   
  
## Constructors 

### TransportManagerSettings(TransportManagerSettings.Builder settingsBuilder)
    
    
    protected TransportManagerSettings(TransportManagerSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[TransportManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings.Builder)`  
  
  
## Methods 

### createTransportOperationSettings()
    
    
    public OperationCallSettings<CreateTransportRequest,Transport,OperationMetadata> createTransportOperationSettings()

Returns the object with the settings used for calls to createTransport.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateTransportRequest),[Transport](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Transport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### createTransportSettings()
    
    
    public UnaryCallSettings<CreateTransportRequest,Operation> createTransportSettings()

Returns the object with the settings used for calls to createTransport.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.CreateTransportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTransportOperationSettings()
    
    
    public OperationCallSettings<DeleteTransportRequest,Empty,OperationMetadata> deleteTransportOperationSettings()

Returns the object with the settings used for calls to deleteTransport.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteTransportRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### deleteTransportSettings()
    
    
    public UnaryCallSettings<DeleteTransportRequest,Operation> deleteTransportSettings()

Returns the object with the settings used for calls to deleteTransport.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.DeleteTransportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
  
### getRemoteTransportProfileSettings()
    
    
    public UnaryCallSettings<GetRemoteTransportProfileRequest,RemoteTransportProfile> getRemoteTransportProfileSettings()

Returns the object with the settings used for calls to getRemoteTransportProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRemoteTransportProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetRemoteTransportProfileRequest),[RemoteTransportProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.RemoteTransportProfile)>` |   
  
### getStatusSettings()
    
    
    public UnaryCallSettings<GetStatusRequest,GetStatusResponse> getStatusSettings()

Returns the object with the settings used for calls to getStatus.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetStatusRequest),[GetStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetStatusResponse)>` |   
  
### getTransportSettings()
    
    
    public UnaryCallSettings<GetTransportRequest,Transport> getTransportSettings()

Returns the object with the settings used for calls to getTransport.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.GetTransportRequest),[Transport](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Transport)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,TransportManagerClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerClient.ListLocationsPagedResponse)>` |   
  
### listRemoteTransportProfilesSettings()
    
    
    public PagedCallSettings<ListRemoteTransportProfilesRequest,ListRemoteTransportProfilesResponse,TransportManagerClient.ListRemoteTransportProfilesPagedResponse> listRemoteTransportProfilesSettings()

Returns the object with the settings used for calls to listRemoteTransportProfiles.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRemoteTransportProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRemoteTransportProfilesRequest),[ListRemoteTransportProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListRemoteTransportProfilesResponse),[ListRemoteTransportProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerClient.ListRemoteTransportProfilesPagedResponse)>` |   
  
### listTransportsSettings()
    
    
    public PagedCallSettings<ListTransportsRequest,ListTransportsResponse,TransportManagerClient.ListTransportsPagedResponse> listTransportsSettings()

Returns the object with the settings used for calls to listTransports.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTransportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListTransportsRequest),[ListTransportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ListTransportsResponse),[ListTransportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerClient.ListTransportsPagedResponse)>` |   
  
### parseFromActivationKeySettings()
    
    
    public UnaryCallSettings<ParseFromActivationKeyRequest,ParseFromActivationKeyResponse> parseFromActivationKeySettings()

Returns the object with the settings used for calls to parseFromActivationKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ParseFromActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ParseFromActivationKeyRequest),[ParseFromActivationKeyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.ParseFromActivationKeyResponse)>` |   
  
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
    
    
    public TransportManagerSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[TransportManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.TransportManagerSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateTransportOperationSettings()
    
    
    public OperationCallSettings<UpdateTransportRequest,Transport,OperationMetadata> updateTransportOperationSettings()

Returns the object with the settings used for calls to updateTransport.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateTransportRequest),[Transport](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.Transport),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.OperationMetadata)>` |   
  
### updateTransportSettings()
    
    
    public UnaryCallSettings<UpdateTransportRequest,Operation> updateTransportSettings()

Returns the object with the settings used for calls to updateTransport.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTransportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkconnectivity/latest/com.google.cloud.networkconnectivity.v1beta.UpdateTransportRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
