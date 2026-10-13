---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings
title: Class WebSecurityScannerStubSettings (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:18.057163+00:00
---

# Class WebSecurityScannerStubSettings (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WebSecurityScannerStubSettings (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.4  2.1.1  2.0.15 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class WebSecurityScannerStubSettings extends StubSettings<WebSecurityScannerStubSettings>

Settings class to configure an instance of [WebSecurityScannerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStub).

The default instance has everything set to sensible defaults:

  * The default service address (websecurityscanner.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createScanConfig:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WebSecurityScannerStubSettings.Builder webSecurityScannerSettingsBuilder =
         WebSecurityScannerStubSettings.newBuilder();
     webSecurityScannerSettingsBuilder
         .createScanConfigSettings()
         .setRetrySettings(
             webSecurityScannerSettingsBuilder
                 .createScanConfigSettings()
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
     WebSecurityScannerStubSettings webSecurityScannerSettings =
         webSecurityScannerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > WebSecurityScannerStubSettings

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
    
    
    public static WebSecurityScannerStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[WebSecurityScannerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static WebSecurityScannerStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebSecurityScannerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static WebSecurityScannerStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[WebSecurityScannerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings.Builder)` |   
  
## Constructors 

### WebSecurityScannerStubSettings(WebSecurityScannerStubSettings.Builder settingsBuilder)
    
    
    protected WebSecurityScannerStubSettings(WebSecurityScannerStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[WebSecurityScannerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings.Builder)`  
  
  
## Methods 

### createScanConfigSettings()
    
    
    public UnaryCallSettings<CreateScanConfigRequest,ScanConfig> createScanConfigSettings()

Returns the object with the settings used for calls to createScanConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateScanConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.CreateScanConfigRequest),[ScanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanConfig)>` |   
  
### createStub()
    
    
    public WebSecurityScannerStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[WebSecurityScannerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteScanConfigSettings()
    
    
    public UnaryCallSettings<DeleteScanConfigRequest,Empty> deleteScanConfigSettings()

Returns the object with the settings used for calls to deleteScanConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteScanConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.DeleteScanConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getFindingSettings()
    
    
    public UnaryCallSettings<GetFindingRequest,Finding> getFindingSettings()

Returns the object with the settings used for calls to getFinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.GetFindingRequest),[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.Finding)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getScanConfigSettings()
    
    
    public UnaryCallSettings<GetScanConfigRequest,ScanConfig> getScanConfigSettings()

Returns the object with the settings used for calls to getScanConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetScanConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.GetScanConfigRequest),[ScanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanConfig)>` |   
  
### getScanRunSettings()
    
    
    public UnaryCallSettings<GetScanRunRequest,ScanRun> getScanRunSettings()

Returns the object with the settings used for calls to getScanRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetScanRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.GetScanRunRequest),[ScanRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanRun)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listCrawledUrlsSettings()
    
    
    public PagedCallSettings<ListCrawledUrlsRequest,ListCrawledUrlsResponse,WebSecurityScannerClient.ListCrawledUrlsPagedResponse> listCrawledUrlsSettings()

Returns the object with the settings used for calls to listCrawledUrls.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCrawledUrlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsRequest),[ListCrawledUrlsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsResponse),[ListCrawledUrlsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.WebSecurityScannerClient.ListCrawledUrlsPagedResponse)>` |   
  
### listFindingTypeStatsSettings()
    
    
    public UnaryCallSettings<ListFindingTypeStatsRequest,ListFindingTypeStatsResponse> listFindingTypeStatsSettings()

Returns the object with the settings used for calls to listFindingTypeStats.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListFindingTypeStatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsRequest),[ListFindingTypeStatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsResponse)>` |   
  
### listFindingsSettings()
    
    
    public PagedCallSettings<ListFindingsRequest,ListFindingsResponse,WebSecurityScannerClient.ListFindingsPagedResponse> listFindingsSettings()

Returns the object with the settings used for calls to listFindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListFindingsRequest),[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListFindingsResponse),[ListFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.WebSecurityScannerClient.ListFindingsPagedResponse)>` |   
  
### listScanConfigsSettings()
    
    
    public PagedCallSettings<ListScanConfigsRequest,ListScanConfigsResponse,WebSecurityScannerClient.ListScanConfigsPagedResponse> listScanConfigsSettings()

Returns the object with the settings used for calls to listScanConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListScanConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListScanConfigsRequest),[ListScanConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListScanConfigsResponse),[ListScanConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.WebSecurityScannerClient.ListScanConfigsPagedResponse)>` |   
  
### listScanRunsSettings()
    
    
    public PagedCallSettings<ListScanRunsRequest,ListScanRunsResponse,WebSecurityScannerClient.ListScanRunsPagedResponse> listScanRunsSettings()

Returns the object with the settings used for calls to listScanRuns.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListScanRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListScanRunsRequest),[ListScanRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ListScanRunsResponse),[ListScanRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.WebSecurityScannerClient.ListScanRunsPagedResponse)>` |   
  
### startScanRunSettings()
    
    
    public UnaryCallSettings<StartScanRunRequest,ScanRun> startScanRunSettings()

Returns the object with the settings used for calls to startScanRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartScanRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.StartScanRunRequest),[ScanRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanRun)>` |   
  
### stopScanRunSettings()
    
    
    public UnaryCallSettings<StopScanRunRequest,ScanRun> stopScanRunSettings()

Returns the object with the settings used for calls to stopScanRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopScanRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.StopScanRunRequest),[ScanRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanRun)>` |   
  
### toBuilder()
    
    
    public WebSecurityScannerStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[WebSecurityScannerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.stub.WebSecurityScannerStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateScanConfigSettings()
    
    
    public UnaryCallSettings<UpdateScanConfigRequest,ScanConfig> updateScanConfigSettings()

Returns the object with the settings used for calls to updateScanConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateScanConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.UpdateScanConfigRequest),[ScanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-websecurityscanner/latest/com.google.cloud.websecurityscanner.v1alpha.ScanConfig)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
