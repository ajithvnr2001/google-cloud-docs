---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings
title: Class DataCatalogStubSettings (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:56.882355+00:00
---

# Class DataCatalogStubSettings (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataCatalogStubSettings (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public class DataCatalogStubSettings extends StubSettings<DataCatalogStubSettings>

**Deprecated.** _This class is deprecated and will be removed in the next major version update._

Settings class to configure an instance of [DataCatalogStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStub).

The default instance has everything set to sensible defaults:

  * The default service address (datacatalog.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createEntryGroup:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataCatalogStubSettings.Builder dataCatalogSettingsBuilder =
         DataCatalogStubSettings.newBuilder();
     dataCatalogSettingsBuilder
         .createEntryGroupSettings()
         .setRetrySettings(
             dataCatalogSettingsBuilder
                 .createEntryGroupSettings()
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
     DataCatalogStubSettings dataCatalogSettings = dataCatalogSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for reconcileTags:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataCatalogStubSettings.Builder dataCatalogSettingsBuilder =
         DataCatalogStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     dataCatalogSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > DataCatalogStubSettings

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

### defaultApiClientHeaderProviderBuilder() (deprecated)
    
    
    public static ApiClientHeaderProvider.Builder defaultApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultCredentialsProviderBuilder() (deprecated)
    
    
    public static GoogleCredentialsProvider.Builder defaultCredentialsProviderBuilder()

Returns a builder for the default credentials for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.GoogleCredentialsProvider.Builder.html)` |   
  
### defaultExecutorProviderBuilder() (deprecated)
    
    
    public static InstantiatingExecutorProvider.Builder defaultExecutorProviderBuilder()

Returns a builder for the default ExecutorProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html)` |   
  
### defaultGrpcApiClientHeaderProviderBuilder() (deprecated)
    
    
    public static ApiClientHeaderProvider.Builder defaultGrpcApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder() (deprecated)
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonApiClientHeaderProviderBuilder() (deprecated)
    
    
    public static ApiClientHeaderProvider.Builder defaultHttpJsonApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultHttpJsonTransportProviderBuilder() (deprecated)
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a builder for the default REST ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider() (deprecated)
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint() (deprecated)
    
    
    public static String getDefaultEndpoint()

**Obsolete**

_Use getEndpoint() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultMtlsEndpoint() (deprecated)
    
    
    public static String getDefaultMtlsEndpoint()

Returns the default mTLS service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultServiceScopes() (deprecated)
    
    
    public static List<String> getDefaultServiceScopes()

Returns the default service scopes.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### newBuilder() (deprecated)
    
    
    public static DataCatalogStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DataCatalogStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext) (deprecated)
    
    
    public static DataCatalogStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataCatalogStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings.Builder)` |   
  
### newHttpJsonBuilder() (deprecated)
    
    
    public static DataCatalogStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DataCatalogStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings.Builder)` |   
  
## Constructors 

### DataCatalogStubSettings(DataCatalogStubSettings.Builder settingsBuilder) (deprecated)
    
    
    protected DataCatalogStubSettings(DataCatalogStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[DataCatalogStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings.Builder)`  
  
  
## Methods 

### createEntryGroupSettings() (deprecated)
    
    
    public UnaryCallSettings<CreateEntryGroupRequest,EntryGroup> createEntryGroupSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to createEntryGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup)>` |   
  
### createEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<CreateEntryRequest,Entry> createEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to createEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry)>` |   
  
### createStub() (deprecated)
    
    
    public DataCatalogStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[DataCatalogStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### createTagSettings() (deprecated)
    
    
    public UnaryCallSettings<CreateTagRequest,Tag> createTagSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to createTag.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagRequest),[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag)>` |   
  
### createTagTemplateFieldSettings() (deprecated)
    
    
    public UnaryCallSettings<CreateTagTemplateFieldRequest,TagTemplateField> createTagTemplateFieldSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to createTagTemplateField.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTagTemplateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateFieldRequest),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField)>` |   
  
### createTagTemplateSettings() (deprecated)
    
    
    public UnaryCallSettings<CreateTagTemplateRequest,TagTemplate> createTagTemplateSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to createTagTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.CreateTagTemplateRequest),[TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate)>` |   
  
### deleteEntryGroupSettings() (deprecated)
    
    
    public UnaryCallSettings<DeleteEntryGroupRequest,Empty> deleteEntryGroupSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to deleteEntryGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteEntryGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<DeleteEntryRequest,Empty> deleteEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to deleteEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteEntryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTagSettings() (deprecated)
    
    
    public UnaryCallSettings<DeleteTagRequest,Empty> deleteTagSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to deleteTag.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteTagRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTagTemplateFieldSettings() (deprecated)
    
    
    public UnaryCallSettings<DeleteTagTemplateFieldRequest,Empty> deleteTagTemplateFieldSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to deleteTagTemplateField.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTagTemplateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteTagTemplateFieldRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTagTemplateSettings() (deprecated)
    
    
    public UnaryCallSettings<DeleteTagTemplateRequest,Empty> deleteTagTemplateSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to deleteTagTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DeleteTagTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getEntryGroupSettings() (deprecated)
    
    
    public UnaryCallSettings<GetEntryGroupRequest,EntryGroup> getEntryGroupSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to getEntryGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GetEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup)>` |   
  
### getEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<GetEntryRequest,Entry> getEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to getEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GetEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry)>` |   
  
### getIamPolicySettings() (deprecated)
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLibraryMetadata() (deprecated)
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getServiceName() (deprecated)
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getTagTemplateSettings() (deprecated)
    
    
    public UnaryCallSettings<GetTagTemplateRequest,TagTemplate> getTagTemplateSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to getTagTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.GetTagTemplateRequest),[TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate)>` |   
  
### importEntriesOperationSettings() (deprecated)
    
    
    public OperationCallSettings<ImportEntriesRequest,ImportEntriesResponse,ImportEntriesMetadata> importEntriesOperationSettings()

Returns the object with the settings used for calls to importEntries.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ImportEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportEntriesRequest),[ImportEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportEntriesResponse),[ImportEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportEntriesMetadata)>` |   
  
### importEntriesSettings() (deprecated)
    
    
    public UnaryCallSettings<ImportEntriesRequest,Operation> importEntriesSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to importEntries.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ImportEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ImportEntriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listEntriesSettings() (deprecated)
    
    
    public PagedCallSettings<ListEntriesRequest,ListEntriesResponse,DataCatalogClient.ListEntriesPagedResponse> listEntriesSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to listEntries.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntriesRequest),[ListEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntriesResponse),[ListEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.ListEntriesPagedResponse)>` |   
  
### listEntryGroupsSettings() (deprecated)
    
    
    public PagedCallSettings<ListEntryGroupsRequest,ListEntryGroupsResponse,DataCatalogClient.ListEntryGroupsPagedResponse> listEntryGroupsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to listEntryGroups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEntryGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntryGroupsRequest),[ListEntryGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListEntryGroupsResponse),[ListEntryGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.ListEntryGroupsPagedResponse)>` |   
  
### listTagsSettings() (deprecated)
    
    
    public PagedCallSettings<ListTagsRequest,ListTagsResponse,DataCatalogClient.ListTagsPagedResponse> listTagsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to listTags.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListTagsRequest),[ListTagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ListTagsResponse),[ListTagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.ListTagsPagedResponse)>` |   
  
### lookupEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<LookupEntryRequest,Entry> lookupEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to lookupEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[LookupEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.LookupEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry)>` |   
  
### modifyEntryContactsSettings() (deprecated)
    
    
    public UnaryCallSettings<ModifyEntryContactsRequest,Contacts> modifyEntryContactsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to modifyEntryContacts.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ModifyEntryContactsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ModifyEntryContactsRequest),[Contacts](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Contacts)>` |   
  
### modifyEntryOverviewSettings() (deprecated)
    
    
    public UnaryCallSettings<ModifyEntryOverviewRequest,EntryOverview> modifyEntryOverviewSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to modifyEntryOverview.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ModifyEntryOverviewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ModifyEntryOverviewRequest),[EntryOverview](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryOverview)>` |   
  
### reconcileTagsOperationSettings() (deprecated)
    
    
    public OperationCallSettings<ReconcileTagsRequest,ReconcileTagsResponse,ReconcileTagsMetadata> reconcileTagsOperationSettings()

Returns the object with the settings used for calls to reconcileTags.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReconcileTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ReconcileTagsRequest),[ReconcileTagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ReconcileTagsResponse),[ReconcileTagsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ReconcileTagsMetadata)>` |   
  
### reconcileTagsSettings() (deprecated)
    
    
    public UnaryCallSettings<ReconcileTagsRequest,Operation> reconcileTagsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to reconcileTags.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReconcileTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.ReconcileTagsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### renameTagTemplateFieldEnumValueSettings() (deprecated)
    
    
    public UnaryCallSettings<RenameTagTemplateFieldEnumValueRequest,TagTemplateField> renameTagTemplateFieldEnumValueSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to renameTagTemplateFieldEnumValue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RenameTagTemplateFieldEnumValueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.RenameTagTemplateFieldEnumValueRequest),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField)>` |   
  
### renameTagTemplateFieldSettings() (deprecated)
    
    
    public UnaryCallSettings<RenameTagTemplateFieldRequest,TagTemplateField> renameTagTemplateFieldSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to renameTagTemplateField.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RenameTagTemplateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.RenameTagTemplateFieldRequest),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField)>` |   
  
### retrieveConfigSettings() (deprecated)
    
    
    public UnaryCallSettings<RetrieveConfigRequest,OrganizationConfig> retrieveConfigSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to retrieveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RetrieveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.RetrieveConfigRequest),[OrganizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.OrganizationConfig)>` |   
  
### retrieveEffectiveConfigSettings() (deprecated)
    
    
    public UnaryCallSettings<RetrieveEffectiveConfigRequest,MigrationConfig> retrieveEffectiveConfigSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to retrieveEffectiveConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RetrieveEffectiveConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.RetrieveEffectiveConfigRequest),[MigrationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.MigrationConfig)>` |   
  
### searchCatalogSettings() (deprecated)
    
    
    public PagedCallSettings<SearchCatalogRequest,SearchCatalogResponse,DataCatalogClient.SearchCatalogPagedResponse> searchCatalogSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to searchCatalog.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogRequest),[SearchCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SearchCatalogResponse),[SearchCatalogPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.DataCatalogClient.SearchCatalogPagedResponse)>` |   
  
### setConfigSettings() (deprecated)
    
    
    public UnaryCallSettings<SetConfigRequest,MigrationConfig> setConfigSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to setConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.SetConfigRequest),[MigrationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.MigrationConfig)>` |   
  
### setIamPolicySettings() (deprecated)
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### starEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<StarEntryRequest,StarEntryResponse> starEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to starEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StarEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.StarEntryRequest),[StarEntryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.StarEntryResponse)>` |   
  
### testIamPermissionsSettings() (deprecated)
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder() (deprecated)
    
    
    public DataCatalogStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[DataCatalogStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.stub.DataCatalogStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### unstarEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<UnstarEntryRequest,UnstarEntryResponse> unstarEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to unstarEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UnstarEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UnstarEntryRequest),[UnstarEntryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UnstarEntryResponse)>` |   
  
### updateEntryGroupSettings() (deprecated)
    
    
    public UnaryCallSettings<UpdateEntryGroupRequest,EntryGroup> updateEntryGroupSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to updateEntryGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEntryGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateEntryGroupRequest),[EntryGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.EntryGroup)>` |   
  
### updateEntrySettings() (deprecated)
    
    
    public UnaryCallSettings<UpdateEntryRequest,Entry> updateEntrySettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to updateEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateEntryRequest),[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Entry)>` |   
  
### updateTagSettings() (deprecated)
    
    
    public UnaryCallSettings<UpdateTagRequest,Tag> updateTagSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to updateTag.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateTagRequest),[Tag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.Tag)>` |   
  
### updateTagTemplateFieldSettings() (deprecated)
    
    
    public UnaryCallSettings<UpdateTagTemplateFieldRequest,TagTemplateField> updateTagTemplateFieldSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to updateTagTemplateField.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTagTemplateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateTagTemplateFieldRequest),[TagTemplateField](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplateField)>` |   
  
### updateTagTemplateSettings() (deprecated)
    
    
    public UnaryCallSettings<UpdateTagTemplateRequest,TagTemplate> updateTagTemplateSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to updateTagTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTagTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.UpdateTagTemplateRequest),[TagTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagTemplate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
