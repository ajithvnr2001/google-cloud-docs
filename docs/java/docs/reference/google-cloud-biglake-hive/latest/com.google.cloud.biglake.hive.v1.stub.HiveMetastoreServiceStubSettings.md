---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings
title: Class HiveMetastoreServiceStubSettings (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:42.745201+00:00
---

# Class HiveMetastoreServiceStubSettings (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HiveMetastoreServiceStubSettings (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class HiveMetastoreServiceStubSettings extends StubSettings<HiveMetastoreServiceStubSettings>

Settings class to configure an instance of [HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (biglake.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createHiveCatalog:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HiveMetastoreServiceStubSettings.Builder hiveMetastoreServiceSettingsBuilder =
         HiveMetastoreServiceStubSettings.newBuilder();
     hiveMetastoreServiceSettingsBuilder
         .createHiveCatalogSettings()
         .setRetrySettings(
             hiveMetastoreServiceSettingsBuilder
                 .createHiveCatalogSettings()
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
     HiveMetastoreServiceStubSettings hiveMetastoreServiceSettings =
         hiveMetastoreServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > HiveMetastoreServiceStubSettings

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
    
    
    public static HiveMetastoreServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static HiveMetastoreServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static HiveMetastoreServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings.Builder)` |   
  
## Constructors 

### HiveMetastoreServiceStubSettings(HiveMetastoreServiceStubSettings.Builder settingsBuilder)
    
    
    protected HiveMetastoreServiceStubSettings(HiveMetastoreServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[HiveMetastoreServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings.Builder)`  
  
  
## Methods 

### batchCreatePartitionsSettings()
    
    
    public UnaryCallSettings<BatchCreatePartitionsRequest,BatchCreatePartitionsResponse> batchCreatePartitionsSettings()

Returns the object with the settings used for calls to batchCreatePartitions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchCreatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.BatchCreatePartitionsRequest),[BatchCreatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.BatchCreatePartitionsResponse)>` |   
  
### batchDeletePartitionsSettings()
    
    
    public UnaryCallSettings<BatchDeletePartitionsRequest,Empty> batchDeletePartitionsSettings()

Returns the object with the settings used for calls to batchDeletePartitions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchDeletePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.BatchDeletePartitionsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchUpdatePartitionsSettings()
    
    
    public UnaryCallSettings<BatchUpdatePartitionsRequest,BatchUpdatePartitionsResponse> batchUpdatePartitionsSettings()

Returns the object with the settings used for calls to batchUpdatePartitions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchUpdatePartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.BatchUpdatePartitionsRequest),[BatchUpdatePartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.BatchUpdatePartitionsResponse)>` |   
  
### createHiveCatalogSettings()
    
    
    public UnaryCallSettings<CreateHiveCatalogRequest,HiveCatalog> createHiveCatalogSettings()

Returns the object with the settings used for calls to createHiveCatalog.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveCatalog)>` |   
  
### createHiveDatabaseSettings()
    
    
    public UnaryCallSettings<CreateHiveDatabaseRequest,HiveDatabase> createHiveDatabaseSettings()

Returns the object with the settings used for calls to createHiveDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveDatabase)>` |   
  
### createHiveTableSettings()
    
    
    public UnaryCallSettings<CreateHiveTableRequest,HiveTable> createHiveTableSettings()

Returns the object with the settings used for calls to createHiveTable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveTable)>` |   
  
### createStub()
    
    
    public HiveMetastoreServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteHiveCatalogSettings()
    
    
    public UnaryCallSettings<DeleteHiveCatalogRequest,Empty> deleteHiveCatalogSettings()

Returns the object with the settings used for calls to deleteHiveCatalog.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.DeleteHiveCatalogRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteHiveDatabaseSettings()
    
    
    public UnaryCallSettings<DeleteHiveDatabaseRequest,Empty> deleteHiveDatabaseSettings()

Returns the object with the settings used for calls to deleteHiveDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.DeleteHiveDatabaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteHiveTableSettings()
    
    
    public UnaryCallSettings<DeleteHiveTableRequest,Empty> deleteHiveTableSettings()

Returns the object with the settings used for calls to deleteHiveTable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.DeleteHiveTableRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### failoverHiveCatalogSettings()
    
    
    public UnaryCallSettings<FailoverHiveCatalogRequest,FailoverHiveCatalogResponse> failoverHiveCatalogSettings()

Returns the object with the settings used for calls to failoverHiveCatalog.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FailoverHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.FailoverHiveCatalogRequest),[FailoverHiveCatalogResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.FailoverHiveCatalogResponse)>` |   
  
### getHiveCatalogSettings()
    
    
    public UnaryCallSettings<GetHiveCatalogRequest,HiveCatalog> getHiveCatalogSettings()

Returns the object with the settings used for calls to getHiveCatalog.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.GetHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveCatalog)>` |   
  
### getHiveDatabaseSettings()
    
    
    public UnaryCallSettings<GetHiveDatabaseRequest,HiveDatabase> getHiveDatabaseSettings()

Returns the object with the settings used for calls to getHiveDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.GetHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveDatabase)>` |   
  
### getHiveTableSettings()
    
    
    public UnaryCallSettings<GetHiveTableRequest,HiveTable> getHiveTableSettings()

Returns the object with the settings used for calls to getHiveTable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.GetHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveTable)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listHiveCatalogsSettings()
    
    
    public PagedCallSettings<ListHiveCatalogsRequest,ListHiveCatalogsResponse,HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse> listHiveCatalogsSettings()

Returns the object with the settings used for calls to listHiveCatalogs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHiveCatalogsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveCatalogsRequest),[ListHiveCatalogsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveCatalogsResponse),[ListHiveCatalogsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse)>` |   
  
### listHiveDatabasesSettings()
    
    
    public PagedCallSettings<ListHiveDatabasesRequest,ListHiveDatabasesResponse,HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse> listHiveDatabasesSettings()

Returns the object with the settings used for calls to listHiveDatabases.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHiveDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveDatabasesRequest),[ListHiveDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveDatabasesResponse),[ListHiveDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse)>` |   
  
### listHiveTablesSettings()
    
    
    public PagedCallSettings<ListHiveTablesRequest,ListHiveTablesResponse,HiveMetastoreServiceClient.ListHiveTablesPagedResponse> listHiveTablesSettings()

Returns the object with the settings used for calls to listHiveTables.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHiveTablesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveTablesRequest),[ListHiveTablesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListHiveTablesResponse),[ListHiveTablesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveMetastoreServiceClient.ListHiveTablesPagedResponse)>` |   
  
### listPartitionsSettings()
    
    
    public ServerStreamingCallSettings<ListPartitionsRequest,ListPartitionsResponse> listPartitionsSettings()

Returns the object with the settings used for calls to listPartitions.

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings.html)<[ListPartitionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListPartitionsRequest),[ListPartitionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.ListPartitionsResponse)>` |   
  
### toBuilder()
    
    
    public HiveMetastoreServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.stub.HiveMetastoreServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateHiveCatalogSettings()
    
    
    public UnaryCallSettings<UpdateHiveCatalogRequest,HiveCatalog> updateHiveCatalogSettings()

Returns the object with the settings used for calls to updateHiveCatalog.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHiveCatalogRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.UpdateHiveCatalogRequest),[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveCatalog)>` |   
  
### updateHiveDatabaseSettings()
    
    
    public UnaryCallSettings<UpdateHiveDatabaseRequest,HiveDatabase> updateHiveDatabaseSettings()

Returns the object with the settings used for calls to updateHiveDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHiveDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.UpdateHiveDatabaseRequest),[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveDatabase)>` |   
  
### updateHiveTableSettings()
    
    
    public UnaryCallSettings<UpdateHiveTableRequest,HiveTable> updateHiveTableSettings()

Returns the object with the settings used for calls to updateHiveTable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHiveTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.UpdateHiveTableRequest),[HiveTable](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveTable)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
