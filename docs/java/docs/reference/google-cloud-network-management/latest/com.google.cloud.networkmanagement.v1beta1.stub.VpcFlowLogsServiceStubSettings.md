---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings
title: Class VpcFlowLogsServiceStubSettings (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:06.435506+00:00
---

# Class VpcFlowLogsServiceStubSettings (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VpcFlowLogsServiceStubSettings (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.1.10 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class VpcFlowLogsServiceStubSettings extends StubSettings<VpcFlowLogsServiceStubSettings>

Settings class to configure an instance of [VpcFlowLogsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (networkmanagement.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getVpcFlowLogsConfig:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VpcFlowLogsServiceStubSettings.Builder vpcFlowLogsServiceSettingsBuilder =
         VpcFlowLogsServiceStubSettings.newBuilder();
     vpcFlowLogsServiceSettingsBuilder
         .getVpcFlowLogsConfigSettings()
         .setRetrySettings(
             vpcFlowLogsServiceSettingsBuilder
                 .getVpcFlowLogsConfigSettings()
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
     VpcFlowLogsServiceStubSettings vpcFlowLogsServiceSettings =
         vpcFlowLogsServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createVpcFlowLogsConfig:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VpcFlowLogsServiceStubSettings.Builder vpcFlowLogsServiceSettingsBuilder =
         VpcFlowLogsServiceStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     vpcFlowLogsServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > VpcFlowLogsServiceStubSettings

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
    
    
    public static VpcFlowLogsServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static VpcFlowLogsServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static VpcFlowLogsServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings.Builder)` |   
  
## Constructors 

### VpcFlowLogsServiceStubSettings(VpcFlowLogsServiceStubSettings.Builder settingsBuilder)
    
    
    protected VpcFlowLogsServiceStubSettings(VpcFlowLogsServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[VpcFlowLogsServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings.Builder)`  
  
  
## Methods 

### createStub()
    
    
    public VpcFlowLogsServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### createVpcFlowLogsConfigOperationSettings()
    
    
    public OperationCallSettings<CreateVpcFlowLogsConfigRequest,VpcFlowLogsConfig,OperationMetadata> createVpcFlowLogsConfigOperationSettings()

Returns the object with the settings used for calls to createVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.CreateVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.OperationMetadata)>` |   
  
### createVpcFlowLogsConfigSettings()
    
    
    public UnaryCallSettings<CreateVpcFlowLogsConfigRequest,Operation> createVpcFlowLogsConfigSettings()

Returns the object with the settings used for calls to createVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.CreateVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteVpcFlowLogsConfigOperationSettings()
    
    
    public OperationCallSettings<DeleteVpcFlowLogsConfigRequest,Empty,OperationMetadata> deleteVpcFlowLogsConfigOperationSettings()

Returns the object with the settings used for calls to deleteVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.DeleteVpcFlowLogsConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.OperationMetadata)>` |   
  
### deleteVpcFlowLogsConfigSettings()
    
    
    public UnaryCallSettings<DeleteVpcFlowLogsConfigRequest,Operation> deleteVpcFlowLogsConfigSettings()

Returns the object with the settings used for calls to deleteVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.DeleteVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
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
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getVpcFlowLogsConfigSettings()
    
    
    public UnaryCallSettings<GetVpcFlowLogsConfigRequest,VpcFlowLogsConfig> getVpcFlowLogsConfigSettings()

Returns the object with the settings used for calls to getVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.GetVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,VpcFlowLogsServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsServiceClient.ListLocationsPagedResponse)>` |   
  
### listVpcFlowLogsConfigsSettings()
    
    
    public PagedCallSettings<ListVpcFlowLogsConfigsRequest,ListVpcFlowLogsConfigsResponse,VpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse> listVpcFlowLogsConfigsSettings()

Returns the object with the settings used for calls to listVpcFlowLogsConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVpcFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.ListVpcFlowLogsConfigsRequest),[ListVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.ListVpcFlowLogsConfigsResponse),[ListVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsServiceClient.ListVpcFlowLogsConfigsPagedResponse)>` |   
  
### queryOrgVpcFlowLogsConfigsSettings()
    
    
    public PagedCallSettings<QueryOrgVpcFlowLogsConfigsRequest,QueryOrgVpcFlowLogsConfigsResponse,VpcFlowLogsServiceClient.QueryOrgVpcFlowLogsConfigsPagedResponse> queryOrgVpcFlowLogsConfigsSettings()

Returns the object with the settings used for calls to queryOrgVpcFlowLogsConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryOrgVpcFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.QueryOrgVpcFlowLogsConfigsRequest),[QueryOrgVpcFlowLogsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.QueryOrgVpcFlowLogsConfigsResponse),[QueryOrgVpcFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsServiceClient.QueryOrgVpcFlowLogsConfigsPagedResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### showEffectiveFlowLogsConfigsSettings()
    
    
    public PagedCallSettings<ShowEffectiveFlowLogsConfigsRequest,ShowEffectiveFlowLogsConfigsResponse,VpcFlowLogsServiceClient.ShowEffectiveFlowLogsConfigsPagedResponse> showEffectiveFlowLogsConfigsSettings()

Returns the object with the settings used for calls to showEffectiveFlowLogsConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ShowEffectiveFlowLogsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.ShowEffectiveFlowLogsConfigsRequest),[ShowEffectiveFlowLogsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.ShowEffectiveFlowLogsConfigsResponse),[ShowEffectiveFlowLogsConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsServiceClient.ShowEffectiveFlowLogsConfigsPagedResponse)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public VpcFlowLogsServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[VpcFlowLogsServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.stub.VpcFlowLogsServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateVpcFlowLogsConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateVpcFlowLogsConfigRequest,VpcFlowLogsConfig,OperationMetadata> updateVpcFlowLogsConfigOperationSettings()

Returns the object with the settings used for calls to updateVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.UpdateVpcFlowLogsConfigRequest),[VpcFlowLogsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.VpcFlowLogsConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.OperationMetadata)>` |   
  
### updateVpcFlowLogsConfigSettings()
    
    
    public UnaryCallSettings<UpdateVpcFlowLogsConfigRequest,Operation> updateVpcFlowLogsConfigSettings()

Returns the object with the settings used for calls to updateVpcFlowLogsConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateVpcFlowLogsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-management/latest/com.google.cloud.networkmanagement.v1beta1.UpdateVpcFlowLogsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
