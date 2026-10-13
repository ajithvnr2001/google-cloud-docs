---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings
title: Class VmwareEngineSettings (0.93.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:52.312209+00:00
---

# Class VmwareEngineSettings (0.93.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VmwareEngineSettings (0.93.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.93.0 (latest)  0.89.0  0.88.0  0.87.0  0.85.0  0.82.0  0.81.0  0.79.0  0.77.0  0.76.0  0.74.0  0.72.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.58.0  0.57.0  0.56.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public class VmwareEngineSettings extends ClientSettings<VmwareEngineSettings>

Settings class to configure an instance of [VmwareEngineClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient).

The default instance has everything set to sensible defaults:

  * The default service address (vmwareengine.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getPrivateCloud:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VmwareEngineSettings.Builder vmwareEngineSettingsBuilder = VmwareEngineSettings.newBuilder();
     vmwareEngineSettingsBuilder
         .getPrivateCloudSettings()
         .setRetrySettings(
             vmwareEngineSettingsBuilder
                 .getPrivateCloudSettings()
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
     VmwareEngineSettings vmwareEngineSettings = vmwareEngineSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createPrivateCloud:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VmwareEngineSettings.Builder vmwareEngineSettingsBuilder = VmwareEngineSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     vmwareEngineSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > VmwareEngineSettings

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

### create(VmwareEngineStubSettings stub)
    
    
    public static final VmwareEngineSettings create(VmwareEngineStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VmwareEngineStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.stub.VmwareEngineStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings)` |   
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

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
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
    
    
    public static VmwareEngineSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static VmwareEngineSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static VmwareEngineSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings.Builder)` |   
  
## Constructors 

### VmwareEngineSettings(VmwareEngineSettings.Builder settingsBuilder)
    
    
    protected VmwareEngineSettings(VmwareEngineSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[VmwareEngineSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings.Builder)`  
  
  
## Methods 

### createClusterOperationSettings()
    
    
    public OperationCallSettings<CreateClusterRequest,Cluster,OperationMetadata> createClusterOperationSettings()

Returns the object with the settings used for calls to createCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createClusterSettings()
    
    
    public UnaryCallSettings<CreateClusterRequest,Operation> createClusterSettings()

Returns the object with the settings used for calls to createCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExternalAccessRuleOperationSettings()
    
    
    public OperationCallSettings<CreateExternalAccessRuleRequest,ExternalAccessRule,OperationMetadata> createExternalAccessRuleOperationSettings()

Returns the object with the settings used for calls to createExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAccessRuleSettings()
    
    
    public UnaryCallSettings<CreateExternalAccessRuleRequest,Operation> createExternalAccessRuleSettings()

Returns the object with the settings used for calls to createExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExternalAddressOperationSettings()
    
    
    public OperationCallSettings<CreateExternalAddressRequest,ExternalAddress,OperationMetadata> createExternalAddressOperationSettings()

Returns the object with the settings used for calls to createExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createExternalAddressSettings()
    
    
    public UnaryCallSettings<CreateExternalAddressRequest,Operation> createExternalAddressSettings()

Returns the object with the settings used for calls to createExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHcxActivationKeyOperationSettings()
    
    
    public OperationCallSettings<CreateHcxActivationKeyRequest,HcxActivationKey,OperationMetadata> createHcxActivationKeyOperationSettings()

Returns the object with the settings used for calls to createHcxActivationKey.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateHcxActivationKeyRequest),[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createHcxActivationKeySettings()
    
    
    public UnaryCallSettings<CreateHcxActivationKeyRequest,Operation> createHcxActivationKeySettings()

Returns the object with the settings used for calls to createHcxActivationKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateHcxActivationKeyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLoggingServerOperationSettings()
    
    
    public OperationCallSettings<CreateLoggingServerRequest,LoggingServer,OperationMetadata> createLoggingServerOperationSettings()

Returns the object with the settings used for calls to createLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createLoggingServerSettings()
    
    
    public UnaryCallSettings<CreateLoggingServerRequest,Operation> createLoggingServerSettings()

Returns the object with the settings used for calls to createLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createManagementDnsZoneBindingOperationSettings()
    
    
    public OperationCallSettings<CreateManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> createManagementDnsZoneBindingOperationSettings()

Returns the object with the settings used for calls to createManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createManagementDnsZoneBindingSettings()
    
    
    public UnaryCallSettings<CreateManagementDnsZoneBindingRequest,Operation> createManagementDnsZoneBindingSettings()

Returns the object with the settings used for calls to createManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkPeeringOperationSettings()
    
    
    public OperationCallSettings<CreateNetworkPeeringRequest,NetworkPeering,OperationMetadata> createNetworkPeeringOperationSettings()

Returns the object with the settings used for calls to createNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPeeringSettings()
    
    
    public UnaryCallSettings<CreateNetworkPeeringRequest,Operation> createNetworkPeeringSettings()

Returns the object with the settings used for calls to createNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkPolicyOperationSettings()
    
    
    public OperationCallSettings<CreateNetworkPolicyRequest,NetworkPolicy,OperationMetadata> createNetworkPolicyOperationSettings()

Returns the object with the settings used for calls to createNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createNetworkPolicySettings()
    
    
    public UnaryCallSettings<CreateNetworkPolicyRequest,Operation> createNetworkPolicySettings()

Returns the object with the settings used for calls to createNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateCloudOperationSettings()
    
    
    public OperationCallSettings<CreatePrivateCloudRequest,PrivateCloud,OperationMetadata> createPrivateCloudOperationSettings()

Returns the object with the settings used for calls to createPrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateCloudSettings()
    
    
    public UnaryCallSettings<CreatePrivateCloudRequest,Operation> createPrivateCloudSettings()

Returns the object with the settings used for calls to createPrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateConnectionOperationSettings()
    
    
    public OperationCallSettings<CreatePrivateConnectionRequest,PrivateConnection,OperationMetadata> createPrivateConnectionOperationSettings()

Returns the object with the settings used for calls to createPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createPrivateConnectionSettings()
    
    
    public UnaryCallSettings<CreatePrivateConnectionRequest,Operation> createPrivateConnectionSettings()

Returns the object with the settings used for calls to createPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createVmwareEngineNetworkOperationSettings()
    
    
    public OperationCallSettings<CreateVmwareEngineNetworkRequest,VmwareEngineNetwork,OperationMetadata> createVmwareEngineNetworkOperationSettings()

Returns the object with the settings used for calls to createVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### createVmwareEngineNetworkSettings()
    
    
    public UnaryCallSettings<CreateVmwareEngineNetworkRequest,Operation> createVmwareEngineNetworkSettings()

Returns the object with the settings used for calls to createVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.CreateVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClusterOperationSettings()
    
    
    public OperationCallSettings<DeleteClusterRequest,Empty,OperationMetadata> deleteClusterOperationSettings()

Returns the object with the settings used for calls to deleteCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteClusterSettings()
    
    
    public UnaryCallSettings<DeleteClusterRequest,Operation> deleteClusterSettings()

Returns the object with the settings used for calls to deleteCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExternalAccessRuleOperationSettings()
    
    
    public OperationCallSettings<DeleteExternalAccessRuleRequest,Empty,OperationMetadata> deleteExternalAccessRuleOperationSettings()

Returns the object with the settings used for calls to deleteExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAccessRuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAccessRuleSettings()
    
    
    public UnaryCallSettings<DeleteExternalAccessRuleRequest,Operation> deleteExternalAccessRuleSettings()

Returns the object with the settings used for calls to deleteExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExternalAddressOperationSettings()
    
    
    public OperationCallSettings<DeleteExternalAddressRequest,Empty,OperationMetadata> deleteExternalAddressOperationSettings()

Returns the object with the settings used for calls to deleteExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAddressRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteExternalAddressSettings()
    
    
    public UnaryCallSettings<DeleteExternalAddressRequest,Operation> deleteExternalAddressSettings()

Returns the object with the settings used for calls to deleteExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLoggingServerOperationSettings()
    
    
    public OperationCallSettings<DeleteLoggingServerRequest,Empty,OperationMetadata> deleteLoggingServerOperationSettings()

Returns the object with the settings used for calls to deleteLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteLoggingServerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteLoggingServerSettings()
    
    
    public UnaryCallSettings<DeleteLoggingServerRequest,Operation> deleteLoggingServerSettings()

Returns the object with the settings used for calls to deleteLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteManagementDnsZoneBindingOperationSettings()
    
    
    public OperationCallSettings<DeleteManagementDnsZoneBindingRequest,Empty,OperationMetadata> deleteManagementDnsZoneBindingOperationSettings()

Returns the object with the settings used for calls to deleteManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteManagementDnsZoneBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteManagementDnsZoneBindingSettings()
    
    
    public UnaryCallSettings<DeleteManagementDnsZoneBindingRequest,Operation> deleteManagementDnsZoneBindingSettings()

Returns the object with the settings used for calls to deleteManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkPeeringOperationSettings()
    
    
    public OperationCallSettings<DeleteNetworkPeeringRequest,Empty,OperationMetadata> deleteNetworkPeeringOperationSettings()

Returns the object with the settings used for calls to deleteNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPeeringRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPeeringSettings()
    
    
    public UnaryCallSettings<DeleteNetworkPeeringRequest,Operation> deleteNetworkPeeringSettings()

Returns the object with the settings used for calls to deleteNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkPolicyOperationSettings()
    
    
    public OperationCallSettings<DeleteNetworkPolicyRequest,Empty,OperationMetadata> deleteNetworkPolicyOperationSettings()

Returns the object with the settings used for calls to deleteNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteNetworkPolicySettings()
    
    
    public UnaryCallSettings<DeleteNetworkPolicyRequest,Operation> deleteNetworkPolicySettings()

Returns the object with the settings used for calls to deleteNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateCloudOperationSettings()
    
    
    public OperationCallSettings<DeletePrivateCloudRequest,PrivateCloud,OperationMetadata> deletePrivateCloudOperationSettings()

Returns the object with the settings used for calls to deletePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateCloudSettings()
    
    
    public UnaryCallSettings<DeletePrivateCloudRequest,Operation> deletePrivateCloudSettings()

Returns the object with the settings used for calls to deletePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateConnectionOperationSettings()
    
    
    public OperationCallSettings<DeletePrivateConnectionRequest,Empty,OperationMetadata> deletePrivateConnectionOperationSettings()

Returns the object with the settings used for calls to deletePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionSettings()
    
    
    public UnaryCallSettings<DeletePrivateConnectionRequest,Operation> deletePrivateConnectionSettings()

Returns the object with the settings used for calls to deletePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeletePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVmwareEngineNetworkOperationSettings()
    
    
    public OperationCallSettings<DeleteVmwareEngineNetworkRequest,Empty,OperationMetadata> deleteVmwareEngineNetworkOperationSettings()

Returns the object with the settings used for calls to deleteVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteVmwareEngineNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### deleteVmwareEngineNetworkSettings()
    
    
    public UnaryCallSettings<DeleteVmwareEngineNetworkRequest,Operation> deleteVmwareEngineNetworkSettings()

Returns the object with the settings used for calls to deleteVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DeleteVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### fetchNetworkPolicyExternalAddressesSettings()
    
    
    public PagedCallSettings<FetchNetworkPolicyExternalAddressesRequest,FetchNetworkPolicyExternalAddressesResponse,VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse> fetchNetworkPolicyExternalAddressesSettings()

Returns the object with the settings used for calls to fetchNetworkPolicyExternalAddresses.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FetchNetworkPolicyExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesRequest),[FetchNetworkPolicyExternalAddressesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.FetchNetworkPolicyExternalAddressesResponse),[FetchNetworkPolicyExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.FetchNetworkPolicyExternalAddressesPagedResponse)>` |   
  
### getClusterSettings()
    
    
    public UnaryCallSettings<GetClusterRequest,Cluster> getClusterSettings()

Returns the object with the settings used for calls to getCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster)>` |   
  
### getDnsBindPermissionSettings()
    
    
    public UnaryCallSettings<GetDnsBindPermissionRequest,DnsBindPermission> getDnsBindPermissionSettings()

Returns the object with the settings used for calls to getDnsBindPermission.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission)>` |   
  
### getDnsForwardingSettings()
    
    
    public UnaryCallSettings<GetDnsForwardingRequest,DnsForwarding> getDnsForwardingSettings()

Returns the object with the settings used for calls to getDnsForwarding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetDnsForwardingRequest),[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding)>` |   
  
### getExternalAccessRuleSettings()
    
    
    public UnaryCallSettings<GetExternalAccessRuleRequest,ExternalAccessRule> getExternalAccessRuleSettings()

Returns the object with the settings used for calls to getExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule)>` |   
  
### getExternalAddressSettings()
    
    
    public UnaryCallSettings<GetExternalAddressRequest,ExternalAddress> getExternalAddressSettings()

Returns the object with the settings used for calls to getExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)>` |   
  
### getHcxActivationKeySettings()
    
    
    public UnaryCallSettings<GetHcxActivationKeyRequest,HcxActivationKey> getHcxActivationKeySettings()

Returns the object with the settings used for calls to getHcxActivationKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHcxActivationKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetHcxActivationKeyRequest),[HcxActivationKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.HcxActivationKey)>` |   
  
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
  
### getLoggingServerSettings()
    
    
    public UnaryCallSettings<GetLoggingServerRequest,LoggingServer> getLoggingServerSettings()

Returns the object with the settings used for calls to getLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer)>` |   
  
### getManagementDnsZoneBindingSettings()
    
    
    public UnaryCallSettings<GetManagementDnsZoneBindingRequest,ManagementDnsZoneBinding> getManagementDnsZoneBindingSettings()

Returns the object with the settings used for calls to getManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding)>` |   
  
### getNetworkPeeringSettings()
    
    
    public UnaryCallSettings<GetNetworkPeeringRequest,NetworkPeering> getNetworkPeeringSettings()

Returns the object with the settings used for calls to getNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering)>` |   
  
### getNetworkPolicySettings()
    
    
    public UnaryCallSettings<GetNetworkPolicyRequest,NetworkPolicy> getNetworkPolicySettings()

Returns the object with the settings used for calls to getNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy)>` |   
  
### getNodeSettings()
    
    
    public UnaryCallSettings<GetNodeRequest,Node> getNodeSettings()

Returns the object with the settings used for calls to getNode.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNodeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeRequest),[Node](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Node)>` |   
  
### getNodeTypeSettings()
    
    
    public UnaryCallSettings<GetNodeTypeRequest,NodeType> getNodeTypeSettings()

Returns the object with the settings used for calls to getNodeType.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNodeTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetNodeTypeRequest),[NodeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NodeType)>` |   
  
### getPrivateCloudSettings()
    
    
    public UnaryCallSettings<GetPrivateCloudRequest,PrivateCloud> getPrivateCloudSettings()

Returns the object with the settings used for calls to getPrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud)>` |   
  
### getPrivateConnectionSettings()
    
    
    public UnaryCallSettings<GetPrivateConnectionRequest,PrivateConnection> getPrivateConnectionSettings()

Returns the object with the settings used for calls to getPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetPrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection)>` |   
  
### getSubnetSettings()
    
    
    public UnaryCallSettings<GetSubnetRequest,Subnet> getSubnetSettings()

Returns the object with the settings used for calls to getSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet)>` |   
  
### getVmwareEngineNetworkSettings()
    
    
    public UnaryCallSettings<GetVmwareEngineNetworkRequest,VmwareEngineNetwork> getVmwareEngineNetworkSettings()

Returns the object with the settings used for calls to getVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GetVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork)>` |   
  
### grantDnsBindPermissionOperationSettings()
    
    
    public OperationCallSettings<GrantDnsBindPermissionRequest,DnsBindPermission,OperationMetadata> grantDnsBindPermissionOperationSettings()

Returns the object with the settings used for calls to grantDnsBindPermission.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[GrantDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GrantDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### grantDnsBindPermissionSettings()
    
    
    public UnaryCallSettings<GrantDnsBindPermissionRequest,Operation> grantDnsBindPermissionSettings()

Returns the object with the settings used for calls to grantDnsBindPermission.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GrantDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.GrantDnsBindPermissionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listClustersSettings()
    
    
    public PagedCallSettings<ListClustersRequest,ListClustersResponse,VmwareEngineClient.ListClustersPagedResponse> listClustersSettings()

Returns the object with the settings used for calls to listClusters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListClustersResponse),[ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListClustersPagedResponse)>` |   
  
### listExternalAccessRulesSettings()
    
    
    public PagedCallSettings<ListExternalAccessRulesRequest,ListExternalAccessRulesResponse,VmwareEngineClient.ListExternalAccessRulesPagedResponse> listExternalAccessRulesSettings()

Returns the object with the settings used for calls to listExternalAccessRules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListExternalAccessRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesRequest),[ListExternalAccessRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAccessRulesResponse),[ListExternalAccessRulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAccessRulesPagedResponse)>` |   
  
### listExternalAddressesSettings()
    
    
    public PagedCallSettings<ListExternalAddressesRequest,ListExternalAddressesResponse,VmwareEngineClient.ListExternalAddressesPagedResponse> listExternalAddressesSettings()

Returns the object with the settings used for calls to listExternalAddresses.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListExternalAddressesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesRequest),[ListExternalAddressesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesResponse),[ListExternalAddressesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListExternalAddressesPagedResponse)>` |   
  
### listHcxActivationKeysSettings()
    
    
    public PagedCallSettings<ListHcxActivationKeysRequest,ListHcxActivationKeysResponse,VmwareEngineClient.ListHcxActivationKeysPagedResponse> listHcxActivationKeysSettings()

Returns the object with the settings used for calls to listHcxActivationKeys.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHcxActivationKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysRequest),[ListHcxActivationKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListHcxActivationKeysResponse),[ListHcxActivationKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListHcxActivationKeysPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,VmwareEngineClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLocationsPagedResponse)>` |   
  
### listLoggingServersSettings()
    
    
    public PagedCallSettings<ListLoggingServersRequest,ListLoggingServersResponse,VmwareEngineClient.ListLoggingServersPagedResponse> listLoggingServersSettings()

Returns the object with the settings used for calls to listLoggingServers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListLoggingServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersRequest),[ListLoggingServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListLoggingServersResponse),[ListLoggingServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListLoggingServersPagedResponse)>` |   
  
### listManagementDnsZoneBindingsSettings()
    
    
    public PagedCallSettings<ListManagementDnsZoneBindingsRequest,ListManagementDnsZoneBindingsResponse,VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse> listManagementDnsZoneBindingsSettings()

Returns the object with the settings used for calls to listManagementDnsZoneBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListManagementDnsZoneBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsRequest),[ListManagementDnsZoneBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListManagementDnsZoneBindingsResponse),[ListManagementDnsZoneBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListManagementDnsZoneBindingsPagedResponse)>` |   
  
### listNetworkPeeringsSettings()
    
    
    public PagedCallSettings<ListNetworkPeeringsRequest,ListNetworkPeeringsResponse,VmwareEngineClient.ListNetworkPeeringsPagedResponse> listNetworkPeeringsSettings()

Returns the object with the settings used for calls to listNetworkPeerings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNetworkPeeringsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsRequest),[ListNetworkPeeringsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPeeringsResponse),[ListNetworkPeeringsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPeeringsPagedResponse)>` |   
  
### listNetworkPoliciesSettings()
    
    
    public PagedCallSettings<ListNetworkPoliciesRequest,ListNetworkPoliciesResponse,VmwareEngineClient.ListNetworkPoliciesPagedResponse> listNetworkPoliciesSettings()

Returns the object with the settings used for calls to listNetworkPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNetworkPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesRequest),[ListNetworkPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNetworkPoliciesResponse),[ListNetworkPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNetworkPoliciesPagedResponse)>` |   
  
### listNodeTypesSettings()
    
    
    public PagedCallSettings<ListNodeTypesRequest,ListNodeTypesResponse,VmwareEngineClient.ListNodeTypesPagedResponse> listNodeTypesSettings()

Returns the object with the settings used for calls to listNodeTypes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNodeTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesRequest),[ListNodeTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodeTypesResponse),[ListNodeTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodeTypesPagedResponse)>` |   
  
### listNodesSettings()
    
    
    public PagedCallSettings<ListNodesRequest,ListNodesResponse,VmwareEngineClient.ListNodesPagedResponse> listNodesSettings()

Returns the object with the settings used for calls to listNodes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesRequest),[ListNodesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListNodesResponse),[ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListNodesPagedResponse)>` |   
  
### listPeeringRoutesSettings()
    
    
    public PagedCallSettings<ListPeeringRoutesRequest,ListPeeringRoutesResponse,VmwareEngineClient.ListPeeringRoutesPagedResponse> listPeeringRoutesSettings()

Returns the object with the settings used for calls to listPeeringRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesRequest),[ListPeeringRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPeeringRoutesResponse),[ListPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPeeringRoutesPagedResponse)>` |   
  
### listPrivateCloudsSettings()
    
    
    public PagedCallSettings<ListPrivateCloudsRequest,ListPrivateCloudsResponse,VmwareEngineClient.ListPrivateCloudsPagedResponse> listPrivateCloudsSettings()

Returns the object with the settings used for calls to listPrivateClouds.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPrivateCloudsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsRequest),[ListPrivateCloudsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateCloudsResponse),[ListPrivateCloudsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateCloudsPagedResponse)>` |   
  
### listPrivateConnectionPeeringRoutesSettings()
    
    
    public PagedCallSettings<ListPrivateConnectionPeeringRoutesRequest,ListPrivateConnectionPeeringRoutesResponse,VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse> listPrivateConnectionPeeringRoutesSettings()

Returns the object with the settings used for calls to listPrivateConnectionPeeringRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPrivateConnectionPeeringRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesRequest),[ListPrivateConnectionPeeringRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionPeeringRoutesResponse),[ListPrivateConnectionPeeringRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionPeeringRoutesPagedResponse)>` |   
  
### listPrivateConnectionsSettings()
    
    
    public PagedCallSettings<ListPrivateConnectionsRequest,ListPrivateConnectionsResponse,VmwareEngineClient.ListPrivateConnectionsPagedResponse> listPrivateConnectionsSettings()

Returns the object with the settings used for calls to listPrivateConnections.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListPrivateConnectionsResponse),[ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListPrivateConnectionsPagedResponse)>` |   
  
### listSubnetsSettings()
    
    
    public PagedCallSettings<ListSubnetsRequest,ListSubnetsResponse,VmwareEngineClient.ListSubnetsPagedResponse> listSubnetsSettings()

Returns the object with the settings used for calls to listSubnets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsRequest),[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListSubnetsResponse),[ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListSubnetsPagedResponse)>` |   
  
### listVmwareEngineNetworksSettings()
    
    
    public PagedCallSettings<ListVmwareEngineNetworksRequest,ListVmwareEngineNetworksResponse,VmwareEngineClient.ListVmwareEngineNetworksPagedResponse> listVmwareEngineNetworksSettings()

Returns the object with the settings used for calls to listVmwareEngineNetworks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVmwareEngineNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksRequest),[ListVmwareEngineNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListVmwareEngineNetworksResponse),[ListVmwareEngineNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineClient.ListVmwareEngineNetworksPagedResponse)>` |   
  
### repairManagementDnsZoneBindingOperationSettings()
    
    
    public OperationCallSettings<RepairManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> repairManagementDnsZoneBindingOperationSettings()

Returns the object with the settings used for calls to repairManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RepairManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RepairManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### repairManagementDnsZoneBindingSettings()
    
    
    public UnaryCallSettings<RepairManagementDnsZoneBindingRequest,Operation> repairManagementDnsZoneBindingSettings()

Returns the object with the settings used for calls to repairManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RepairManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RepairManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetNsxCredentialsOperationSettings()
    
    
    public OperationCallSettings<ResetNsxCredentialsRequest,PrivateCloud,OperationMetadata> resetNsxCredentialsOperationSettings()

Returns the object with the settings used for calls to resetNsxCredentials.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResetNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetNsxCredentialsRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetNsxCredentialsSettings()
    
    
    public UnaryCallSettings<ResetNsxCredentialsRequest,Operation> resetNsxCredentialsSettings()

Returns the object with the settings used for calls to resetNsxCredentials.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetNsxCredentialsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetVcenterCredentialsOperationSettings()
    
    
    public OperationCallSettings<ResetVcenterCredentialsRequest,PrivateCloud,OperationMetadata> resetVcenterCredentialsOperationSettings()

Returns the object with the settings used for calls to resetVcenterCredentials.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResetVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetVcenterCredentialsRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### resetVcenterCredentialsSettings()
    
    
    public UnaryCallSettings<ResetVcenterCredentialsRequest,Operation> resetVcenterCredentialsSettings()

Returns the object with the settings used for calls to resetVcenterCredentials.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ResetVcenterCredentialsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### revokeDnsBindPermissionOperationSettings()
    
    
    public OperationCallSettings<RevokeDnsBindPermissionRequest,DnsBindPermission,OperationMetadata> revokeDnsBindPermissionOperationSettings()

Returns the object with the settings used for calls to revokeDnsBindPermission.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RevokeDnsBindPermissionRequest),[DnsBindPermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsBindPermission),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### revokeDnsBindPermissionSettings()
    
    
    public UnaryCallSettings<RevokeDnsBindPermissionRequest,Operation> revokeDnsBindPermissionSettings()

Returns the object with the settings used for calls to revokeDnsBindPermission.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RevokeDnsBindPermissionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.RevokeDnsBindPermissionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### showNsxCredentialsSettings()
    
    
    public UnaryCallSettings<ShowNsxCredentialsRequest,Credentials> showNsxCredentialsSettings()

Returns the object with the settings used for calls to showNsxCredentials.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ShowNsxCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowNsxCredentialsRequest),[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)>` |   
  
### showVcenterCredentialsSettings()
    
    
    public UnaryCallSettings<ShowVcenterCredentialsRequest,Credentials> showVcenterCredentialsSettings()

Returns the object with the settings used for calls to showVcenterCredentials.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ShowVcenterCredentialsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ShowVcenterCredentialsRequest),[Credentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Credentials)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public VmwareEngineSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[VmwareEngineSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### undeletePrivateCloudOperationSettings()
    
    
    public OperationCallSettings<UndeletePrivateCloudRequest,PrivateCloud,OperationMetadata> undeletePrivateCloudOperationSettings()

Returns the object with the settings used for calls to undeletePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UndeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UndeletePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### undeletePrivateCloudSettings()
    
    
    public UnaryCallSettings<UndeletePrivateCloudRequest,Operation> undeletePrivateCloudSettings()

Returns the object with the settings used for calls to undeletePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UndeletePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UndeletePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClusterOperationSettings()
    
    
    public OperationCallSettings<UpdateClusterRequest,Cluster,OperationMetadata> updateClusterOperationSettings()

Returns the object with the settings used for calls to updateCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateClusterSettings()
    
    
    public UnaryCallSettings<UpdateClusterRequest,Operation> updateClusterSettings()

Returns the object with the settings used for calls to updateCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDnsForwardingOperationSettings()
    
    
    public OperationCallSettings<UpdateDnsForwardingRequest,DnsForwarding,OperationMetadata> updateDnsForwardingOperationSettings()

Returns the object with the settings used for calls to updateDnsForwarding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateDnsForwardingRequest),[DnsForwarding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.DnsForwarding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateDnsForwardingSettings()
    
    
    public UnaryCallSettings<UpdateDnsForwardingRequest,Operation> updateDnsForwardingSettings()

Returns the object with the settings used for calls to updateDnsForwarding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateDnsForwardingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateDnsForwardingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExternalAccessRuleOperationSettings()
    
    
    public OperationCallSettings<UpdateExternalAccessRuleRequest,ExternalAccessRule,OperationMetadata> updateExternalAccessRuleOperationSettings()

Returns the object with the settings used for calls to updateExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAccessRuleRequest),[ExternalAccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAccessRule),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAccessRuleSettings()
    
    
    public UnaryCallSettings<UpdateExternalAccessRuleRequest,Operation> updateExternalAccessRuleSettings()

Returns the object with the settings used for calls to updateExternalAccessRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateExternalAccessRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAccessRuleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExternalAddressOperationSettings()
    
    
    public OperationCallSettings<UpdateExternalAddressRequest,ExternalAddress,OperationMetadata> updateExternalAddressOperationSettings()

Returns the object with the settings used for calls to updateExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAddressRequest),[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateExternalAddressSettings()
    
    
    public UnaryCallSettings<UpdateExternalAddressRequest,Operation> updateExternalAddressSettings()

Returns the object with the settings used for calls to updateExternalAddress.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateExternalAddressRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateExternalAddressRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLoggingServerOperationSettings()
    
    
    public OperationCallSettings<UpdateLoggingServerRequest,LoggingServer,OperationMetadata> updateLoggingServerOperationSettings()

Returns the object with the settings used for calls to updateLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateLoggingServerRequest),[LoggingServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.LoggingServer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateLoggingServerSettings()
    
    
    public UnaryCallSettings<UpdateLoggingServerRequest,Operation> updateLoggingServerSettings()

Returns the object with the settings used for calls to updateLoggingServer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateLoggingServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateLoggingServerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateManagementDnsZoneBindingOperationSettings()
    
    
    public OperationCallSettings<UpdateManagementDnsZoneBindingRequest,ManagementDnsZoneBinding,OperationMetadata> updateManagementDnsZoneBindingOperationSettings()

Returns the object with the settings used for calls to updateManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateManagementDnsZoneBindingRequest),[ManagementDnsZoneBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ManagementDnsZoneBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateManagementDnsZoneBindingSettings()
    
    
    public UnaryCallSettings<UpdateManagementDnsZoneBindingRequest,Operation> updateManagementDnsZoneBindingSettings()

Returns the object with the settings used for calls to updateManagementDnsZoneBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateManagementDnsZoneBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateManagementDnsZoneBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateNetworkPeeringOperationSettings()
    
    
    public OperationCallSettings<UpdateNetworkPeeringRequest,NetworkPeering,OperationMetadata> updateNetworkPeeringOperationSettings()

Returns the object with the settings used for calls to updateNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPeeringRequest),[NetworkPeering](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPeering),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPeeringSettings()
    
    
    public UnaryCallSettings<UpdateNetworkPeeringRequest,Operation> updateNetworkPeeringSettings()

Returns the object with the settings used for calls to updateNetworkPeering.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateNetworkPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPeeringRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateNetworkPolicyOperationSettings()
    
    
    public OperationCallSettings<UpdateNetworkPolicyRequest,NetworkPolicy,OperationMetadata> updateNetworkPolicyOperationSettings()

Returns the object with the settings used for calls to updateNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPolicyRequest),[NetworkPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.NetworkPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateNetworkPolicySettings()
    
    
    public UnaryCallSettings<UpdateNetworkPolicyRequest,Operation> updateNetworkPolicySettings()

Returns the object with the settings used for calls to updateNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePrivateCloudOperationSettings()
    
    
    public OperationCallSettings<UpdatePrivateCloudRequest,PrivateCloud,OperationMetadata> updatePrivateCloudOperationSettings()

Returns the object with the settings used for calls to updatePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateCloudRequest),[PrivateCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateCloud),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateCloudSettings()
    
    
    public UnaryCallSettings<UpdatePrivateCloudRequest,Operation> updatePrivateCloudSettings()

Returns the object with the settings used for calls to updatePrivateCloud.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePrivateCloudRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateCloudRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePrivateConnectionOperationSettings()
    
    
    public OperationCallSettings<UpdatePrivateConnectionRequest,PrivateConnection,OperationMetadata> updatePrivateConnectionOperationSettings()

Returns the object with the settings used for calls to updatePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updatePrivateConnectionSettings()
    
    
    public UnaryCallSettings<UpdatePrivateConnectionRequest,Operation> updatePrivateConnectionSettings()

Returns the object with the settings used for calls to updatePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubnetOperationSettings()
    
    
    public OperationCallSettings<UpdateSubnetRequest,Subnet,OperationMetadata> updateSubnetOperationSettings()

Returns the object with the settings used for calls to updateSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateSubnetSettings()
    
    
    public UnaryCallSettings<UpdateSubnetRequest,Operation> updateSubnetSettings()

Returns the object with the settings used for calls to updateSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateVmwareEngineNetworkOperationSettings()
    
    
    public OperationCallSettings<UpdateVmwareEngineNetworkRequest,VmwareEngineNetwork,OperationMetadata> updateVmwareEngineNetworkOperationSettings()

Returns the object with the settings used for calls to updateVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateVmwareEngineNetworkRequest),[VmwareEngineNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.VmwareEngineNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.OperationMetadata)>` |   
  
### updateVmwareEngineNetworkSettings()
    
    
    public UnaryCallSettings<UpdateVmwareEngineNetworkRequest,Operation> updateVmwareEngineNetworkSettings()

Returns the object with the settings used for calls to updateVmwareEngineNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateVmwareEngineNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.UpdateVmwareEngineNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
