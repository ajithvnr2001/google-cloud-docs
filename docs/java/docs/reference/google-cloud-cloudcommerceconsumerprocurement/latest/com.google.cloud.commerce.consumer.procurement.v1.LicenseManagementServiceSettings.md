---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings
title: Class LicenseManagementServiceSettings (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:29.276525+00:00
---

# Class LicenseManagementServiceSettings (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LicenseManagementServiceSettings (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public class LicenseManagementServiceSettings extends ClientSettings<LicenseManagementServiceSettings>

Settings class to configure an instance of [LicenseManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudcommerceconsumerprocurement.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getLicensePool:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LicenseManagementServiceSettings.Builder licenseManagementServiceSettingsBuilder =
         LicenseManagementServiceSettings.newBuilder();
     licenseManagementServiceSettingsBuilder
         .getLicensePoolSettings()
         .setRetrySettings(
             licenseManagementServiceSettingsBuilder
                 .getLicensePoolSettings()
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
     LicenseManagementServiceSettings licenseManagementServiceSettings =
         licenseManagementServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > LicenseManagementServiceSettings

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

### create(LicenseManagementServiceStubSettings stub)
    
    
    public static final LicenseManagementServiceSettings create(LicenseManagementServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[LicenseManagementServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.stub.LicenseManagementServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings)` |   
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
    
    
    public static LicenseManagementServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static LicenseManagementServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static LicenseManagementServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings.Builder)` |   
  
## Constructors 

### LicenseManagementServiceSettings(LicenseManagementServiceSettings.Builder settingsBuilder)
    
    
    protected LicenseManagementServiceSettings(LicenseManagementServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[LicenseManagementServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings.Builder)`  
  
  
## Methods 

### assignSettings()
    
    
    public UnaryCallSettings<AssignRequest,AssignResponse> assignSettings()

Returns the object with the settings used for calls to assign.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AssignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignRequest),[AssignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.AssignResponse)>` |   
  
### enumerateLicensedUsersSettings()
    
    
    public PagedCallSettings<EnumerateLicensedUsersRequest,EnumerateLicensedUsersResponse,LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse> enumerateLicensedUsersSettings()

Returns the object with the settings used for calls to enumerateLicensedUsers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[EnumerateLicensedUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersRequest),[EnumerateLicensedUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.EnumerateLicensedUsersResponse),[EnumerateLicensedUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceClient.EnumerateLicensedUsersPagedResponse)>` |   
  
### getLicensePoolSettings()
    
    
    public UnaryCallSettings<GetLicensePoolRequest,LicensePool> getLicensePoolSettings()

Returns the object with the settings used for calls to getLicensePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.GetLicensePoolRequest),[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)>` |   
  
### toBuilder()
    
    
    public LicenseManagementServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[LicenseManagementServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicenseManagementServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### unassignSettings()
    
    
    public UnaryCallSettings<UnassignRequest,UnassignResponse> unassignSettings()

Returns the object with the settings used for calls to unassign.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UnassignRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignRequest),[UnassignResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UnassignResponse)>` |   
  
### updateLicensePoolSettings()
    
    
    public UnaryCallSettings<UpdateLicensePoolRequest,LicensePool> updateLicensePoolSettings()

Returns the object with the settings used for calls to updateLicensePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateLicensePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.UpdateLicensePoolRequest),[LicensePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LicensePool)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
