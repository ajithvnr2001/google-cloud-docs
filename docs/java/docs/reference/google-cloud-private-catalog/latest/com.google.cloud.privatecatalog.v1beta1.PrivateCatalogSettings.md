---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings
title: Class PrivateCatalogSettings (0.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:50.083763+00:00
---

# Class PrivateCatalogSettings (0.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PrivateCatalogSettings (0.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.101.0 (latest)  0.97.0  0.96.0  0.95.0  0.93.0  0.90.0  0.89.0  0.87.0  0.85.0  0.84.0  0.82.0  0.80.0  0.78.0  0.77.0  0.76.0  0.75.0  0.74.0  0.72.0  0.70.0  0.69.0  0.66.0  0.65.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.7 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class PrivateCatalogSettings extends ClientSettings<PrivateCatalogSettings>

Settings class to configure an instance of [PrivateCatalogClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudprivatecatalog.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of searchCatalogs:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PrivateCatalogSettings.Builder privateCatalogSettingsBuilder =
         PrivateCatalogSettings.newBuilder();
     privateCatalogSettingsBuilder
         .searchCatalogsSettings()
         .setRetrySettings(
             privateCatalogSettingsBuilder
                 .searchCatalogsSettings()
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
     PrivateCatalogSettings privateCatalogSettings = privateCatalogSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > PrivateCatalogSettings

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

### create(PrivateCatalogStubSettings stub)
    
    
    public static final PrivateCatalogSettings create(PrivateCatalogStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PrivateCatalogStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.stub.PrivateCatalogStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateCatalogSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings)` |   
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
    
    
    public static PrivateCatalogSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[PrivateCatalogSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static PrivateCatalogSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[PrivateCatalogSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static PrivateCatalogSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[PrivateCatalogSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings.Builder)` |   
  
## Constructors 

### PrivateCatalogSettings(PrivateCatalogSettings.Builder settingsBuilder)
    
    
    protected PrivateCatalogSettings(PrivateCatalogSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[PrivateCatalogSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings.Builder)`  
  
  
## Methods 

### searchCatalogsSettings()
    
    
    public PagedCallSettings<SearchCatalogsRequest,SearchCatalogsResponse,PrivateCatalogClient.SearchCatalogsPagedResponse> searchCatalogsSettings()

Returns the object with the settings used for calls to searchCatalogs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchCatalogsRequest),[SearchCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchCatalogsResponse),[SearchCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogClient.SearchCatalogsPagedResponse)>` |   
  
### searchProductsSettings()
    
    
    public PagedCallSettings<SearchProductsRequest,SearchProductsResponse,PrivateCatalogClient.SearchProductsPagedResponse> searchProductsSettings()

Returns the object with the settings used for calls to searchProducts.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchProductsRequest),[SearchProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchProductsResponse),[SearchProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogClient.SearchProductsPagedResponse)>` |   
  
### searchVersionsSettings()
    
    
    public PagedCallSettings<SearchVersionsRequest,SearchVersionsResponse,PrivateCatalogClient.SearchVersionsPagedResponse> searchVersionsSettings()

Returns the object with the settings used for calls to searchVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchVersionsRequest),[SearchVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.SearchVersionsResponse),[SearchVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogClient.SearchVersionsPagedResponse)>` |   
  
### toBuilder()
    
    
    public PrivateCatalogSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[PrivateCatalogSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-private-catalog/latest/com.google.cloud.privatecatalog.v1beta1.PrivateCatalogSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
