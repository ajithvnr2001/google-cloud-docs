---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings
title: Class UptimeCheckServiceSettings (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:21.236669+00:00
---

# Class UptimeCheckServiceSettings (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UptimeCheckServiceSettings (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.6  3.3.6  3.2.10 
    
    
    public class UptimeCheckServiceSettings extends ClientSettings<UptimeCheckServiceSettings>

Settings class to configure an instance of [UptimeCheckServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (monitoring.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getUptimeCheckConfig:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UptimeCheckServiceSettings.Builder uptimeCheckServiceSettingsBuilder =
         UptimeCheckServiceSettings.newBuilder();
     uptimeCheckServiceSettingsBuilder
         .getUptimeCheckConfigSettings()
         .setRetrySettings(
             uptimeCheckServiceSettingsBuilder
                 .getUptimeCheckConfigSettings()
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
     UptimeCheckServiceSettings uptimeCheckServiceSettings =
         uptimeCheckServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > UptimeCheckServiceSettings

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

### create(UptimeCheckServiceStubSettings stub)
    
    
    public static final UptimeCheckServiceSettings create(UptimeCheckServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UptimeCheckServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.stub.UptimeCheckServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UptimeCheckServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings)` |   
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
    
    
    public static UptimeCheckServiceSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[UptimeCheckServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static UptimeCheckServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[UptimeCheckServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings.Builder)` |   
  
## Constructors 

### UptimeCheckServiceSettings(UptimeCheckServiceSettings.Builder settingsBuilder)
    
    
    protected UptimeCheckServiceSettings(UptimeCheckServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[UptimeCheckServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings.Builder)`  
  
  
## Methods 

### createUptimeCheckConfigSettings()
    
    
    public UnaryCallSettings<CreateUptimeCheckConfigRequest,UptimeCheckConfig> createUptimeCheckConfigSettings()

Returns the object with the settings used for calls to createUptimeCheckConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateUptimeCheckConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.CreateUptimeCheckConfigRequest),[UptimeCheckConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.UptimeCheckConfig)>` |   
  
### deleteUptimeCheckConfigSettings()
    
    
    public UnaryCallSettings<DeleteUptimeCheckConfigRequest,Empty> deleteUptimeCheckConfigSettings()

Returns the object with the settings used for calls to deleteUptimeCheckConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteUptimeCheckConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.DeleteUptimeCheckConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getUptimeCheckConfigSettings()
    
    
    public UnaryCallSettings<GetUptimeCheckConfigRequest,UptimeCheckConfig> getUptimeCheckConfigSettings()

Returns the object with the settings used for calls to getUptimeCheckConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetUptimeCheckConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.GetUptimeCheckConfigRequest),[UptimeCheckConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.UptimeCheckConfig)>` |   
  
### listUptimeCheckConfigsSettings()
    
    
    public PagedCallSettings<ListUptimeCheckConfigsRequest,ListUptimeCheckConfigsResponse,UptimeCheckServiceClient.ListUptimeCheckConfigsPagedResponse> listUptimeCheckConfigsSettings()

Returns the object with the settings used for calls to listUptimeCheckConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUptimeCheckConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListUptimeCheckConfigsRequest),[ListUptimeCheckConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListUptimeCheckConfigsResponse),[ListUptimeCheckConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceClient.ListUptimeCheckConfigsPagedResponse)>` |   
  
### listUptimeCheckIpsSettings()
    
    
    public PagedCallSettings<ListUptimeCheckIpsRequest,ListUptimeCheckIpsResponse,UptimeCheckServiceClient.ListUptimeCheckIpsPagedResponse> listUptimeCheckIpsSettings()

Returns the object with the settings used for calls to listUptimeCheckIps.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUptimeCheckIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListUptimeCheckIpsRequest),[ListUptimeCheckIpsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.ListUptimeCheckIpsResponse),[ListUptimeCheckIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceClient.ListUptimeCheckIpsPagedResponse)>` |   
  
### toBuilder()
    
    
    public UptimeCheckServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[UptimeCheckServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.cloud.monitoring.v3.UptimeCheckServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateUptimeCheckConfigSettings()
    
    
    public UnaryCallSettings<UpdateUptimeCheckConfigRequest,UptimeCheckConfig> updateUptimeCheckConfigSettings()

Returns the object with the settings used for calls to updateUptimeCheckConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateUptimeCheckConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.UpdateUptimeCheckConfigRequest),[UptimeCheckConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-monitoring/latest/com.google.monitoring.v3.UptimeCheckConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
