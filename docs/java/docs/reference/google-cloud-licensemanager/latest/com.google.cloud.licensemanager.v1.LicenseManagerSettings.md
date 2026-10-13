---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings
title: Class LicenseManagerSettings (0.32.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:56.608079+00:00
---

# Class LicenseManagerSettings (0.32.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LicenseManagerSettings (0.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.32.0 (latest)  0.28.0  0.27.0  0.26.0  0.24.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public class LicenseManagerSettings extends ClientSettings<LicenseManagerSettings>

Settings class to configure an instance of [LicenseManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient).

The default instance has everything set to sensible defaults:

  * The default service address (licensemanager.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getConfiguration:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagerSettings.Builder licenseManagerSettingsBuilder =
         LicenseManagerSettings.newBuilder();
     licenseManagerSettingsBuilder
         .getConfigurationSettings()
         .setRetrySettings(
             licenseManagerSettingsBuilder
                 .getConfigurationSettings()
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
     LicenseManagerSettings licenseManagerSettings = licenseManagerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createConfiguration:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagerSettings.Builder licenseManagerSettingsBuilder =
         LicenseManagerSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     licenseManagerSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > LicenseManagerSettings

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

### create(LicenseManagerStubSettings stub)
    
    
    public static final LicenseManagerSettings create(LicenseManagerStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicenseManagerStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.stub.LicenseManagerStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings)` |   
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
    
    
    public static LicenseManagerSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static LicenseManagerSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static LicenseManagerSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings.Builder)` |   
  
## Constructors 

### LicenseManagerSettings(LicenseManagerSettings.Builder settingsBuilder)
    
    
    protected LicenseManagerSettings(LicenseManagerSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[LicenseManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings.Builder)`  
  
  
## Methods 

### aggregateUsageSettings()
    
    
    public PagedCallSettings<AggregateUsageRequest,AggregateUsageResponse,LicenseManagerClient.AggregateUsagePagedResponse> aggregateUsageSettings()

Returns the object with the settings used for calls to aggregateUsage.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[AggregateUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.AggregateUsageRequest),[AggregateUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.AggregateUsageResponse),[AggregateUsagePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient.AggregateUsagePagedResponse)>` |   
  
### createConfigurationOperationSettings()
    
    
    public OperationCallSettings<CreateConfigurationRequest,Configuration,OperationMetadata> createConfigurationOperationSettings()

Returns the object with the settings used for calls to createConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.CreateConfigurationRequest),[Configuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Configuration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.OperationMetadata)>` |   
  
### createConfigurationSettings()
    
    
    public UnaryCallSettings<CreateConfigurationRequest,Operation> createConfigurationSettings()

Returns the object with the settings used for calls to createConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.CreateConfigurationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deactivateConfigurationOperationSettings()
    
    
    public OperationCallSettings<DeactivateConfigurationRequest,Configuration,OperationMetadata> deactivateConfigurationOperationSettings()

Returns the object with the settings used for calls to deactivateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeactivateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.DeactivateConfigurationRequest),[Configuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Configuration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.OperationMetadata)>` |   
  
### deactivateConfigurationSettings()
    
    
    public UnaryCallSettings<DeactivateConfigurationRequest,Operation> deactivateConfigurationSettings()

Returns the object with the settings used for calls to deactivateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeactivateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.DeactivateConfigurationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConfigurationOperationSettings()
    
    
    public OperationCallSettings<DeleteConfigurationRequest,Empty,OperationMetadata> deleteConfigurationOperationSettings()

Returns the object with the settings used for calls to deleteConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.DeleteConfigurationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.OperationMetadata)>` |   
  
### deleteConfigurationSettings()
    
    
    public UnaryCallSettings<DeleteConfigurationRequest,Operation> deleteConfigurationSettings()

Returns the object with the settings used for calls to deleteConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.DeleteConfigurationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getConfigurationSettings()
    
    
    public UnaryCallSettings<GetConfigurationRequest,Configuration> getConfigurationSettings()

Returns the object with the settings used for calls to getConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.GetConfigurationRequest),[Configuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Configuration)>` |   
  
### getInstanceSettings()
    
    
    public UnaryCallSettings<GetInstanceRequest,Instance> getInstanceSettings()

Returns the object with the settings used for calls to getInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Instance)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getProductSettings()
    
    
    public UnaryCallSettings<GetProductRequest,Product> getProductSettings()

Returns the object with the settings used for calls to getProduct.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.GetProductRequest),[Product](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Product)>` |   
  
### listConfigurationsSettings()
    
    
    public PagedCallSettings<ListConfigurationsRequest,ListConfigurationsResponse,LicenseManagerClient.ListConfigurationsPagedResponse> listConfigurationsSettings()

Returns the object with the settings used for calls to listConfigurations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListConfigurationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListConfigurationsRequest),[ListConfigurationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListConfigurationsResponse),[ListConfigurationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient.ListConfigurationsPagedResponse)>` |   
  
### listInstancesSettings()
    
    
    public PagedCallSettings<ListInstancesRequest,ListInstancesResponse,LicenseManagerClient.ListInstancesPagedResponse> listInstancesSettings()

Returns the object with the settings used for calls to listInstances.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListInstancesResponse),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient.ListInstancesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,LicenseManagerClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient.ListLocationsPagedResponse)>` |   
  
### listProductsSettings()
    
    
    public PagedCallSettings<ListProductsRequest,ListProductsResponse,LicenseManagerClient.ListProductsPagedResponse> listProductsSettings()

Returns the object with the settings used for calls to listProducts.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ListProductsResponse),[ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerClient.ListProductsPagedResponse)>` |   
  
### queryConfigurationLicenseUsageSettings()
    
    
    public UnaryCallSettings<QueryConfigurationLicenseUsageRequest,QueryConfigurationLicenseUsageResponse> queryConfigurationLicenseUsageSettings()

Returns the object with the settings used for calls to queryConfigurationLicenseUsage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[QueryConfigurationLicenseUsageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageRequest),[QueryConfigurationLicenseUsageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.QueryConfigurationLicenseUsageResponse)>` |   
  
### reactivateConfigurationOperationSettings()
    
    
    public OperationCallSettings<ReactivateConfigurationRequest,Configuration,OperationMetadata> reactivateConfigurationOperationSettings()

Returns the object with the settings used for calls to reactivateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReactivateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ReactivateConfigurationRequest),[Configuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Configuration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.OperationMetadata)>` |   
  
### reactivateConfigurationSettings()
    
    
    public UnaryCallSettings<ReactivateConfigurationRequest,Operation> reactivateConfigurationSettings()

Returns the object with the settings used for calls to reactivateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReactivateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.ReactivateConfigurationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder()
    
    
    public LicenseManagerSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.LicenseManagerSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateConfigurationOperationSettings()
    
    
    public OperationCallSettings<UpdateConfigurationRequest,Configuration,OperationMetadata> updateConfigurationOperationSettings()

Returns the object with the settings used for calls to updateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.UpdateConfigurationRequest),[Configuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.Configuration),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.OperationMetadata)>` |   
  
### updateConfigurationSettings()
    
    
    public UnaryCallSettings<UpdateConfigurationRequest,Operation> updateConfigurationSettings()

Returns the object with the settings used for calls to updateConfiguration.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateConfigurationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-licensemanager/latest/com.google.cloud.licensemanager.v1.UpdateConfigurationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
