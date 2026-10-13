---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings
title: Class InstancesSettings (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:05:33.057626+00:00
---

# Class InstancesSettings (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstancesSettings (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public class InstancesSettings extends ClientSettings<InstancesSettings>

Settings class to configure an instance of [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient).

The default instance has everything set to sensible defaults:

  * The default service address (compute.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of get:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstancesSettings.Builder instancesSettingsBuilder = InstancesSettings.newBuilder();
     instancesSettingsBuilder
         .getSettings()
         .setRetrySettings(
             instancesSettingsBuilder
                 .getSettings()
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
     InstancesSettings instancesSettings = instancesSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for addAccessConfig:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstancesSettings.Builder instancesSettingsBuilder = InstancesSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     instancesSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > InstancesSettings

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

### create(InstancesStubSettings stub)
    
    
    public static final InstancesSettings create(InstancesStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstancesStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstancesStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstancesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings)` |   
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
  
### defaultHttpJsonTransportProviderBuilder()
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

Returns a builder for the default ChannelProvider for this service.

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
    
    
    public static InstancesSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[InstancesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static InstancesSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstancesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings.Builder)` |   
  
## Constructors 

### InstancesSettings(InstancesSettings.Builder settingsBuilder)
    
    
    protected InstancesSettings(InstancesSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[InstancesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings.Builder)`  
  
  
## Methods 

### addAccessConfigOperationSettings()
    
    
    public OperationCallSettings<AddAccessConfigInstanceRequest,Operation,Operation> addAccessConfigOperationSettings()

Returns the object with the settings used for calls to addAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAccessConfigSettings()
    
    
    public UnaryCallSettings<AddAccessConfigInstanceRequest,Operation> addAccessConfigSettings()

Returns the object with the settings used for calls to addAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceOperationSettings()
    
    
    public OperationCallSettings<AddNetworkInterfaceInstanceRequest,Operation,Operation> addNetworkInterfaceOperationSettings()

Returns the object with the settings used for calls to addNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNetworkInterfaceSettings()
    
    
    public UnaryCallSettings<AddNetworkInterfaceInstanceRequest,Operation> addNetworkInterfaceSettings()

Returns the object with the settings used for calls to addNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesOperationSettings()
    
    
    public OperationCallSettings<AddResourcePoliciesInstanceRequest,Operation,Operation> addResourcePoliciesOperationSettings()

Returns the object with the settings used for calls to addResourcePolicies.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesSettings()
    
    
    public UnaryCallSettings<AddResourcePoliciesInstanceRequest,Operation> addResourcePoliciesSettings()

Returns the object with the settings used for calls to addResourcePolicies.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedListSettings()
    
    
    public PagedCallSettings<AggregatedListInstancesRequest,InstanceAggregatedList,InstancesClient.AggregatedListPagedResponse> aggregatedListSettings()

Returns the object with the settings used for calls to aggregatedList.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[AggregatedListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstancesRequest),[InstanceAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceAggregatedList),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.AggregatedListPagedResponse)>` |   
  
### attachDiskOperationSettings()
    
    
    public OperationCallSettings<AttachDiskInstanceRequest,Operation,Operation> attachDiskOperationSettings()

Returns the object with the settings used for calls to attachDisk.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AttachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachDiskSettings()
    
    
    public UnaryCallSettings<AttachDiskInstanceRequest,Operation> attachDiskSettings()

Returns the object with the settings used for calls to attachDisk.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AttachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertOperationSettings()
    
    
    public OperationCallSettings<BulkInsertInstanceRequest,Operation,Operation> bulkInsertOperationSettings()

Returns the object with the settings used for calls to bulkInsert.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[BulkInsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertSettings()
    
    
    public UnaryCallSettings<BulkInsertInstanceRequest,Operation> bulkInsertSettings()

Returns the object with the settings used for calls to bulkInsert.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BulkInsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAccessConfigOperationSettings()
    
    
    public OperationCallSettings<DeleteAccessConfigInstanceRequest,Operation,Operation> deleteAccessConfigOperationSettings()

Returns the object with the settings used for calls to deleteAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAccessConfigSettings()
    
    
    public UnaryCallSettings<DeleteAccessConfigInstanceRequest,Operation> deleteAccessConfigSettings()

Returns the object with the settings used for calls to deleteAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceOperationSettings()
    
    
    public OperationCallSettings<DeleteNetworkInterfaceInstanceRequest,Operation,Operation> deleteNetworkInterfaceOperationSettings()

Returns the object with the settings used for calls to deleteNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNetworkInterfaceSettings()
    
    
    public UnaryCallSettings<DeleteNetworkInterfaceInstanceRequest,Operation> deleteNetworkInterfaceSettings()

Returns the object with the settings used for calls to deleteNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationSettings()
    
    
    public OperationCallSettings<DeleteInstanceRequest,Operation,Operation> deleteOperationSettings()

Returns the object with the settings used for calls to delete.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSettings()
    
    
    public UnaryCallSettings<DeleteInstanceRequest,Operation> deleteSettings()

Returns the object with the settings used for calls to delete.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskOperationSettings()
    
    
    public OperationCallSettings<DetachDiskInstanceRequest,Operation,Operation> detachDiskOperationSettings()

Returns the object with the settings used for calls to detachDisk.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DetachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachDiskSettings()
    
    
    public UnaryCallSettings<DetachDiskInstanceRequest,Operation> detachDiskSettings()

Returns the object with the settings used for calls to detachDisk.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DetachDiskInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachDiskInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getEffectiveFirewallsSettings()
    
    
    public UnaryCallSettings<GetEffectiveFirewallsInstanceRequest,InstancesGetEffectiveFirewallsResponse> getEffectiveFirewallsSettings()

Returns the object with the settings used for calls to getEffectiveFirewalls.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEffectiveFirewallsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetEffectiveFirewallsInstanceRequest),[InstancesGetEffectiveFirewallsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesGetEffectiveFirewallsResponse)>` |   
  
### getGuestAttributesSettings()
    
    
    public UnaryCallSettings<GetGuestAttributesInstanceRequest,GuestAttributes> getGuestAttributesSettings()

Returns the object with the settings used for calls to getGuestAttributes.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGuestAttributesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGuestAttributesInstanceRequest),[GuestAttributes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestAttributes)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyInstanceRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstanceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getScreenshotSettings()
    
    
    public UnaryCallSettings<GetScreenshotInstanceRequest,Screenshot> getScreenshotSettings()

Returns the object with the settings used for calls to getScreenshot.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetScreenshotInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetScreenshotInstanceRequest),[Screenshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Screenshot)>` |   
  
### getSerialPortOutputSettings()
    
    
    public UnaryCallSettings<GetSerialPortOutputInstanceRequest,SerialPortOutput> getSerialPortOutputSettings()

Returns the object with the settings used for calls to getSerialPortOutput.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSerialPortOutputInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSerialPortOutputInstanceRequest),[SerialPortOutput](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SerialPortOutput)>` |   
  
### getSettings()
    
    
    public UnaryCallSettings<GetInstanceRequest,Instance> getSettings()

Returns the object with the settings used for calls to get.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance)>` |   
  
### getShieldedInstanceIdentitySettings()
    
    
    public UnaryCallSettings<GetShieldedInstanceIdentityInstanceRequest,ShieldedInstanceIdentity> getShieldedInstanceIdentitySettings()

Returns the object with the settings used for calls to getShieldedInstanceIdentity.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetShieldedInstanceIdentityInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetShieldedInstanceIdentityInstanceRequest),[ShieldedInstanceIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShieldedInstanceIdentity)>` |   
  
### insertOperationSettings()
    
    
    public OperationCallSettings<InsertInstanceRequest,Operation,Operation> insertOperationSettings()

Returns the object with the settings used for calls to insert.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertSettings()
    
    
    public UnaryCallSettings<InsertInstanceRequest,Operation> insertSettings()

Returns the object with the settings used for calls to insert.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### listReferrersSettings()
    
    
    public PagedCallSettings<ListReferrersInstancesRequest,InstanceListReferrers,InstancesClient.ListReferrersPagedResponse> listReferrersSettings()

Returns the object with the settings used for calls to listReferrers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListReferrersInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReferrersInstancesRequest),[InstanceListReferrers](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceListReferrers),[ListReferrersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListReferrersPagedResponse)>` |   
  
### listSettings()
    
    
    public PagedCallSettings<ListInstancesRequest,InstanceList,InstancesClient.ListPagedResponse> listSettings()

Returns the object with the settings used for calls to list.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRequest),[InstanceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceList),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.ListPagedResponse)>` |   
  
### performMaintenanceOperationSettings()
    
    
    public OperationCallSettings<PerformMaintenanceInstanceRequest,Operation,Operation> performMaintenanceOperationSettings()

Returns the object with the settings used for calls to performMaintenance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceSettings()
    
    
    public UnaryCallSettings<PerformMaintenanceInstanceRequest,Operation> performMaintenanceSettings()

Returns the object with the settings used for calls to performMaintenance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PerformMaintenanceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesOperationSettings()
    
    
    public OperationCallSettings<RemoveResourcePoliciesInstanceRequest,Operation,Operation> removeResourcePoliciesOperationSettings()

Returns the object with the settings used for calls to removeResourcePolicies.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesSettings()
    
    
    public UnaryCallSettings<RemoveResourcePoliciesInstanceRequest,Operation> removeResourcePoliciesSettings()

Returns the object with the settings used for calls to removeResourcePolicies.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveResourcePoliciesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultyOperationSettings()
    
    
    public OperationCallSettings<ReportHostAsFaultyInstanceRequest,Operation,Operation> reportHostAsFaultyOperationSettings()

Returns the object with the settings used for calls to reportHostAsFaulty.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportHostAsFaultyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportHostAsFaultySettings()
    
    
    public UnaryCallSettings<ReportHostAsFaultyInstanceRequest,Operation> reportHostAsFaultySettings()

Returns the object with the settings used for calls to reportHostAsFaulty.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReportHostAsFaultyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportHostAsFaultyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetOperationSettings()
    
    
    public OperationCallSettings<ResetInstanceRequest,Operation,Operation> resetOperationSettings()

Returns the object with the settings used for calls to reset.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResetInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resetSettings()
    
    
    public UnaryCallSettings<ResetInstanceRequest,Operation> resetSettings()

Returns the object with the settings used for calls to reset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResetInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeOperationSettings()
    
    
    public OperationCallSettings<ResumeInstanceRequest,Operation,Operation> resumeOperationSettings()

Returns the object with the settings used for calls to resume.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResumeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeSettings()
    
    
    public UnaryCallSettings<ResumeInstanceRequest,Operation> resumeSettings()

Returns the object with the settings used for calls to resume.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResumeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### sendDiagnosticInterruptSettings()
    
    
    public UnaryCallSettings<SendDiagnosticInterruptInstanceRequest,SendDiagnosticInterruptInstanceResponse> sendDiagnosticInterruptSettings()

Returns the object with the settings used for calls to sendDiagnosticInterrupt.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SendDiagnosticInterruptInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceRequest),[SendDiagnosticInterruptInstanceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SendDiagnosticInterruptInstanceResponse)>` |   
  
### setDeletionProtectionOperationSettings()
    
    
    public OperationCallSettings<SetDeletionProtectionInstanceRequest,Operation,Operation> setDeletionProtectionOperationSettings()

Returns the object with the settings used for calls to setDeletionProtection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDeletionProtectionSettings()
    
    
    public UnaryCallSettings<SetDeletionProtectionInstanceRequest,Operation> setDeletionProtectionSettings()

Returns the object with the settings used for calls to setDeletionProtection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetDeletionProtectionInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDeletionProtectionInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteOperationSettings()
    
    
    public OperationCallSettings<SetDiskAutoDeleteInstanceRequest,Operation,Operation> setDiskAutoDeleteOperationSettings()

Returns the object with the settings used for calls to setDiskAutoDelete.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDiskAutoDeleteSettings()
    
    
    public UnaryCallSettings<SetDiskAutoDeleteInstanceRequest,Operation> setDiskAutoDeleteSettings()

Returns the object with the settings used for calls to setDiskAutoDelete.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyInstanceRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetIamPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstanceRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsOperationSettings()
    
    
    public OperationCallSettings<SetLabelsInstanceRequest,Operation,Operation> setLabelsOperationSettings()

Returns the object with the settings used for calls to setLabels.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetLabelsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsSettings()
    
    
    public UnaryCallSettings<SetLabelsInstanceRequest,Operation> setLabelsSettings()

Returns the object with the settings used for calls to setLabels.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetLabelsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesOperationSettings()
    
    
    public OperationCallSettings<SetMachineResourcesInstanceRequest,Operation,Operation> setMachineResourcesOperationSettings()

Returns the object with the settings used for calls to setMachineResources.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineResourcesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineResourcesSettings()
    
    
    public UnaryCallSettings<SetMachineResourcesInstanceRequest,Operation> setMachineResourcesSettings()

Returns the object with the settings used for calls to setMachineResources.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMachineResourcesInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineResourcesInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeOperationSettings()
    
    
    public OperationCallSettings<SetMachineTypeInstanceRequest,Operation,Operation> setMachineTypeOperationSettings()

Returns the object with the settings used for calls to setMachineType.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMachineTypeSettings()
    
    
    public UnaryCallSettings<SetMachineTypeInstanceRequest,Operation> setMachineTypeSettings()

Returns the object with the settings used for calls to setMachineType.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataOperationSettings()
    
    
    public OperationCallSettings<SetMetadataInstanceRequest,Operation,Operation> setMetadataOperationSettings()

Returns the object with the settings used for calls to setMetadata.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetMetadataInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMetadataInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMetadataSettings()
    
    
    public UnaryCallSettings<SetMetadataInstanceRequest,Operation> setMetadataSettings()

Returns the object with the settings used for calls to setMetadata.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMetadataInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMetadataInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformOperationSettings()
    
    
    public OperationCallSettings<SetMinCpuPlatformInstanceRequest,Operation,Operation> setMinCpuPlatformOperationSettings()

Returns the object with the settings used for calls to setMinCpuPlatform.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMinCpuPlatformInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setMinCpuPlatformSettings()
    
    
    public UnaryCallSettings<SetMinCpuPlatformInstanceRequest,Operation> setMinCpuPlatformSettings()

Returns the object with the settings used for calls to setMinCpuPlatform.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMinCpuPlatformInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMinCpuPlatformInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameOperationSettings()
    
    
    public OperationCallSettings<SetNameInstanceRequest,Operation,Operation> setNameOperationSettings()

Returns the object with the settings used for calls to setName.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetNameInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNameInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNameSettings()
    
    
    public UnaryCallSettings<SetNameInstanceRequest,Operation> setNameSettings()

Returns the object with the settings used for calls to setName.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetNameInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNameInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingOperationSettings()
    
    
    public OperationCallSettings<SetSchedulingInstanceRequest,Operation,Operation> setSchedulingOperationSettings()

Returns the object with the settings used for calls to setScheduling.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetSchedulingInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSchedulingInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSchedulingSettings()
    
    
    public UnaryCallSettings<SetSchedulingInstanceRequest,Operation> setSchedulingSettings()

Returns the object with the settings used for calls to setScheduling.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetSchedulingInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSchedulingInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicyOperationSettings()
    
    
    public OperationCallSettings<SetSecurityPolicyInstanceRequest,Operation,Operation> setSecurityPolicyOperationSettings()

Returns the object with the settings used for calls to setSecurityPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSecurityPolicySettings()
    
    
    public UnaryCallSettings<SetSecurityPolicyInstanceRequest,Operation> setSecurityPolicySettings()

Returns the object with the settings used for calls to setSecurityPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetSecurityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSecurityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountOperationSettings()
    
    
    public OperationCallSettings<SetServiceAccountInstanceRequest,Operation,Operation> setServiceAccountOperationSettings()

Returns the object with the settings used for calls to setServiceAccount.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetServiceAccountInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setServiceAccountSettings()
    
    
    public UnaryCallSettings<SetServiceAccountInstanceRequest,Operation> setServiceAccountSettings()

Returns the object with the settings used for calls to setServiceAccount.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetServiceAccountInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetServiceAccountInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicyOperationSettings()
    
    
    public OperationCallSettings<SetShieldedInstanceIntegrityPolicyInstanceRequest,Operation,Operation> setShieldedInstanceIntegrityPolicyOperationSettings()

Returns the object with the settings used for calls to setShieldedInstanceIntegrityPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetShieldedInstanceIntegrityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setShieldedInstanceIntegrityPolicySettings()
    
    
    public UnaryCallSettings<SetShieldedInstanceIntegrityPolicyInstanceRequest,Operation> setShieldedInstanceIntegrityPolicySettings()

Returns the object with the settings used for calls to setShieldedInstanceIntegrityPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetShieldedInstanceIntegrityPolicyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetShieldedInstanceIntegrityPolicyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsOperationSettings()
    
    
    public OperationCallSettings<SetTagsInstanceRequest,Operation,Operation> setTagsOperationSettings()

Returns the object with the settings used for calls to setTags.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetTagsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTagsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setTagsSettings()
    
    
    public UnaryCallSettings<SetTagsInstanceRequest,Operation> setTagsSettings()

Returns the object with the settings used for calls to setTags.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetTagsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetTagsInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventOperationSettings()
    
    
    public OperationCallSettings<SimulateMaintenanceEventInstanceRequest,Operation,Operation> simulateMaintenanceEventOperationSettings()

Returns the object with the settings used for calls to simulateMaintenanceEvent.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventSettings()
    
    
    public UnaryCallSettings<SimulateMaintenanceEventInstanceRequest,Operation> simulateMaintenanceEventSettings()

Returns the object with the settings used for calls to simulateMaintenanceEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SimulateMaintenanceEventInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startOperationSettings()
    
    
    public OperationCallSettings<StartInstanceRequest,Operation,Operation> startOperationSettings()

Returns the object with the settings used for calls to start.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startSettings()
    
    
    public UnaryCallSettings<StartInstanceRequest,Operation> startSettings()

Returns the object with the settings used for calls to start.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeyOperationSettings()
    
    
    public OperationCallSettings<StartWithEncryptionKeyInstanceRequest,Operation,Operation> startWithEncryptionKeyOperationSettings()

Returns the object with the settings used for calls to startWithEncryptionKey.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startWithEncryptionKeySettings()
    
    
    public UnaryCallSettings<StartWithEncryptionKeyInstanceRequest,Operation> startWithEncryptionKeySettings()

Returns the object with the settings used for calls to startWithEncryptionKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopOperationSettings()
    
    
    public OperationCallSettings<StopInstanceRequest,Operation,Operation> stopOperationSettings()

Returns the object with the settings used for calls to stop.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopSettings()
    
    
    public UnaryCallSettings<StopInstanceRequest,Operation> stopSettings()

Returns the object with the settings used for calls to stop.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendOperationSettings()
    
    
    public OperationCallSettings<SuspendInstanceRequest,Operation,Operation> suspendOperationSettings()

Returns the object with the settings used for calls to suspend.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SuspendInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### suspendSettings()
    
    
    public UnaryCallSettings<SuspendInstanceRequest,Operation> suspendSettings()

Returns the object with the settings used for calls to suspend.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SuspendInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SuspendInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsInstanceRequest,TestPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[TestIamPermissionsInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### toBuilder()
    
    
    public InstancesSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[InstancesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateAccessConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateAccessConfigInstanceRequest,Operation,Operation> updateAccessConfigOperationSettings()

Returns the object with the settings used for calls to updateAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAccessConfigSettings()
    
    
    public UnaryCallSettings<UpdateAccessConfigInstanceRequest,Operation> updateAccessConfigSettings()

Returns the object with the settings used for calls to updateAccessConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAccessConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAccessConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceOperationSettings()
    
    
    public OperationCallSettings<UpdateDisplayDeviceInstanceRequest,Operation,Operation> updateDisplayDeviceOperationSettings()

Returns the object with the settings used for calls to updateDisplayDevice.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateDisplayDeviceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateDisplayDeviceSettings()
    
    
    public UnaryCallSettings<UpdateDisplayDeviceInstanceRequest,Operation> updateDisplayDeviceSettings()

Returns the object with the settings used for calls to updateDisplayDevice.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateDisplayDeviceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateDisplayDeviceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceOperationSettings()
    
    
    public OperationCallSettings<UpdateNetworkInterfaceInstanceRequest,Operation,Operation> updateNetworkInterfaceOperationSettings()

Returns the object with the settings used for calls to updateNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNetworkInterfaceSettings()
    
    
    public UnaryCallSettings<UpdateNetworkInterfaceInstanceRequest,Operation> updateNetworkInterfaceSettings()

Returns the object with the settings used for calls to updateNetworkInterface.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateNetworkInterfaceInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNetworkInterfaceInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationSettings()
    
    
    public OperationCallSettings<UpdateInstanceRequest,Operation,Operation> updateOperationSettings()

Returns the object with the settings used for calls to update.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateSettings()
    
    
    public UnaryCallSettings<UpdateInstanceRequest,Operation> updateSettings()

Returns the object with the settings used for calls to update.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateShieldedInstanceConfigInstanceRequest,Operation,Operation> updateShieldedInstanceConfigOperationSettings()

Returns the object with the settings used for calls to updateShieldedInstanceConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateShieldedInstanceConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateShieldedInstanceConfigSettings()
    
    
    public UnaryCallSettings<UpdateShieldedInstanceConfigInstanceRequest,Operation> updateShieldedInstanceConfigSettings()

Returns the object with the settings used for calls to updateShieldedInstanceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateShieldedInstanceConfigInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateShieldedInstanceConfigInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
