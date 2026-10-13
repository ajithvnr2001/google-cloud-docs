---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings
title: Class StorageControlStubSettings (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:18.807732+00:00
---

# Class StorageControlStubSettings (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageControlStubSettings (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public class StorageControlStubSettings extends StubSettings<StorageControlStubSettings>

Settings class to configure an instance of [StorageControlStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStub).

The default instance has everything set to sensible defaults:

  * The default service address (storage.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createFolder:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StorageControlStubSettings.Builder storageControlSettingsBuilder =
         StorageControlStubSettings.newBuilder();
     storageControlSettingsBuilder
         .createFolderSettings()
         .setRetrySettings(
             storageControlSettingsBuilder
                 .createFolderSettings()
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
     StorageControlStubSettings storageControlSettings = storageControlSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for renameFolder:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StorageControlStubSettings.Builder storageControlSettingsBuilder =
         StorageControlStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     storageControlSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > StorageControlStubSettings

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
    
    
    public static StorageControlStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[StorageControlStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static StorageControlStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageControlStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static StorageControlStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[StorageControlStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings.Builder)` |   
  
## Constructors 

### StorageControlStubSettings(StorageControlStubSettings.Builder settingsBuilder)
    
    
    protected StorageControlStubSettings(StorageControlStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[StorageControlStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings.Builder)`  
  
  
## Methods 

### createAnywhereCacheOperationSettings()
    
    
    public OperationCallSettings<CreateAnywhereCacheRequest,AnywhereCache,CreateAnywhereCacheMetadata> createAnywhereCacheOperationSettings()

Returns the object with the settings used for calls to createAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache),[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheMetadata)>` |   
  
### createAnywhereCacheSettings()
    
    
    public UnaryCallSettings<CreateAnywhereCacheRequest,Operation> createAnywhereCacheSettings()

Returns the object with the settings used for calls to createAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createFolderSettings()
    
    
    public UnaryCallSettings<CreateFolderRequest,Folder> createFolderSettings()

Returns the object with the settings used for calls to createFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder)>` |   
  
### createManagedFolderSettings()
    
    
    public UnaryCallSettings<CreateManagedFolderRequest,ManagedFolder> createManagedFolderSettings()

Returns the object with the settings used for calls to createManagedFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateManagedFolderRequest),[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder)>` |   
  
### createRapidCacheOperationSettings()
    
    
    public OperationCallSettings<CreateRapidCacheRequest,RapidCache,CreateRapidCacheMetadata> createRapidCacheOperationSettings()

Returns the object with the settings used for calls to createRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateRapidCacheRequest),[RapidCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RapidCache),[CreateRapidCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateRapidCacheMetadata)>` |   
  
### createRapidCacheSettings()
    
    
    public UnaryCallSettings<CreateRapidCacheRequest,Operation> createRapidCacheSettings()

Returns the object with the settings used for calls to createRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateRapidCacheRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public StorageControlStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[StorageControlStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteFolderRecursiveOperationSettings()
    
    
    public OperationCallSettings<DeleteFolderRecursiveRequest,Empty,DeleteFolderRecursiveMetadata> deleteFolderRecursiveOperationSettings()

Returns the object with the settings used for calls to deleteFolderRecursive.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRecursiveRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderRecursiveMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRecursiveMetadata)>` |   
  
### deleteFolderRecursiveSettings()
    
    
    public UnaryCallSettings<DeleteFolderRecursiveRequest,Operation> deleteFolderRecursiveSettings()

Returns the object with the settings used for calls to deleteFolderRecursive.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteFolderRecursiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRecursiveRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteFolderSettings()
    
    
    public UnaryCallSettings<DeleteFolderRequest,Empty> deleteFolderSettings()

Returns the object with the settings used for calls to deleteFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteManagedFolderSettings()
    
    
    public UnaryCallSettings<DeleteManagedFolderRequest,Empty> deleteManagedFolderSettings()

Returns the object with the settings used for calls to deleteManagedFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteManagedFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### disableAnywhereCacheSettings()
    
    
    public UnaryCallSettings<DisableAnywhereCacheRequest,AnywhereCache> disableAnywhereCacheSettings()

Returns the object with the settings used for calls to disableAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DisableAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache)>` |   
  
### disableRapidCacheOperationSettings()
    
    
    public OperationCallSettings<DisableRapidCacheRequest,RapidCache,DisableRapidCacheMetadata> disableRapidCacheOperationSettings()

Returns the object with the settings used for calls to disableRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DisableRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableRapidCacheRequest),[RapidCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RapidCache),[DisableRapidCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableRapidCacheMetadata)>` |   
  
### disableRapidCacheSettings()
    
    
    public UnaryCallSettings<DisableRapidCacheRequest,Operation> disableRapidCacheSettings()

Returns the object with the settings used for calls to disableRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DisableRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableRapidCacheRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAnywhereCacheSettings()
    
    
    public UnaryCallSettings<GetAnywhereCacheRequest,AnywhereCache> getAnywhereCacheSettings()

Returns the object with the settings used for calls to getAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache)>` |   
  
### getFolderIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<GetFolderIntelligenceConfigRequest,IntelligenceConfig> getFolderIntelligenceConfigSettings()

Returns the object with the settings used for calls to getFolderIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetFolderIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetFolderIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### getFolderSettings()
    
    
    public UnaryCallSettings<GetFolderRequest,Folder> getFolderSettings()

Returns the object with the settings used for calls to getFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getIntelligenceFindingRevisionSettings()
    
    
    public UnaryCallSettings<GetIntelligenceFindingRevisionRequest,IntelligenceFindingRevision> getIntelligenceFindingRevisionSettings()

Returns the object with the settings used for calls to getIntelligenceFindingRevision.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetIntelligenceFindingRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetIntelligenceFindingRevisionRequest),[IntelligenceFindingRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceFindingRevision)>` |   
  
### getIntelligenceFindingSettings()
    
    
    public UnaryCallSettings<GetIntelligenceFindingRequest,IntelligenceFinding> getIntelligenceFindingSettings()

Returns the object with the settings used for calls to getIntelligenceFinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetIntelligenceFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetIntelligenceFindingRequest),[IntelligenceFinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceFinding)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getManagedFolderSettings()
    
    
    public UnaryCallSettings<GetManagedFolderRequest,ManagedFolder> getManagedFolderSettings()

Returns the object with the settings used for calls to getManagedFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetManagedFolderRequest),[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder)>` |   
  
### getOrganizationIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<GetOrganizationIntelligenceConfigRequest,IntelligenceConfig> getOrganizationIntelligenceConfigSettings()

Returns the object with the settings used for calls to getOrganizationIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetOrganizationIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### getProjectIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<GetProjectIntelligenceConfigRequest,IntelligenceConfig> getProjectIntelligenceConfigSettings()

Returns the object with the settings used for calls to getProjectIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetProjectIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetProjectIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### getRapidCacheSettings()
    
    
    public UnaryCallSettings<GetRapidCacheRequest,RapidCache> getRapidCacheSettings()

Returns the object with the settings used for calls to getRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetRapidCacheRequest),[RapidCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RapidCache)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getStorageLayoutSettings()
    
    
    public UnaryCallSettings<GetStorageLayoutRequest,StorageLayout> getStorageLayoutSettings()

Returns the object with the settings used for calls to getStorageLayout.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetStorageLayoutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetStorageLayoutRequest),[StorageLayout](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayout)>` |   
  
### listAnywhereCachesSettings()
    
    
    public PagedCallSettings<ListAnywhereCachesRequest,ListAnywhereCachesResponse,StorageControlClient.ListAnywhereCachesPagedResponse> listAnywhereCachesSettings()

Returns the object with the settings used for calls to listAnywhereCaches.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAnywhereCachesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListAnywhereCachesRequest),[ListAnywhereCachesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListAnywhereCachesResponse),[ListAnywhereCachesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListAnywhereCachesPagedResponse)>` |   
  
### listFoldersSettings()
    
    
    public PagedCallSettings<ListFoldersRequest,ListFoldersResponse,StorageControlClient.ListFoldersPagedResponse> listFoldersSettings()

Returns the object with the settings used for calls to listFolders.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListFoldersRequest),[ListFoldersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListFoldersResponse),[ListFoldersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListFoldersPagedResponse)>` |   
  
### listIntelligenceFindingRevisionsSettings()
    
    
    public PagedCallSettings<ListIntelligenceFindingRevisionsRequest,ListIntelligenceFindingRevisionsResponse,StorageControlClient.ListIntelligenceFindingRevisionsPagedResponse> listIntelligenceFindingRevisionsSettings()

Returns the object with the settings used for calls to listIntelligenceFindingRevisions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListIntelligenceFindingRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListIntelligenceFindingRevisionsRequest),[ListIntelligenceFindingRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListIntelligenceFindingRevisionsResponse),[ListIntelligenceFindingRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListIntelligenceFindingRevisionsPagedResponse)>` |   
  
### listIntelligenceFindingsSettings()
    
    
    public PagedCallSettings<ListIntelligenceFindingsRequest,ListIntelligenceFindingsResponse,StorageControlClient.ListIntelligenceFindingsPagedResponse> listIntelligenceFindingsSettings()

Returns the object with the settings used for calls to listIntelligenceFindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListIntelligenceFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListIntelligenceFindingsRequest),[ListIntelligenceFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListIntelligenceFindingsResponse),[ListIntelligenceFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListIntelligenceFindingsPagedResponse)>` |   
  
### listManagedFoldersSettings()
    
    
    public PagedCallSettings<ListManagedFoldersRequest,ListManagedFoldersResponse,StorageControlClient.ListManagedFoldersPagedResponse> listManagedFoldersSettings()

Returns the object with the settings used for calls to listManagedFolders.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListManagedFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListManagedFoldersRequest),[ListManagedFoldersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListManagedFoldersResponse),[ListManagedFoldersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListManagedFoldersPagedResponse)>` |   
  
### listRapidCachesSettings()
    
    
    public PagedCallSettings<ListRapidCachesRequest,ListRapidCachesResponse,StorageControlClient.ListRapidCachesPagedResponse> listRapidCachesSettings()

Returns the object with the settings used for calls to listRapidCaches.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRapidCachesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListRapidCachesRequest),[ListRapidCachesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListRapidCachesResponse),[ListRapidCachesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListRapidCachesPagedResponse)>` |   
  
### pauseAnywhereCacheSettings()
    
    
    public UnaryCallSettings<PauseAnywhereCacheRequest,AnywhereCache> pauseAnywhereCacheSettings()

Returns the object with the settings used for calls to pauseAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PauseAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.PauseAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache)>` |   
  
### renameFolderOperationSettings()
    
    
    public OperationCallSettings<RenameFolderRequest,Folder,RenameFolderMetadata> renameFolderOperationSettings()

Returns the object with the settings used for calls to renameFolder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RenameFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder),[RenameFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderMetadata)>` |   
  
### renameFolderSettings()
    
    
    public UnaryCallSettings<RenameFolderRequest,Operation> renameFolderSettings()

Returns the object with the settings used for calls to renameFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RenameFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resumeAnywhereCacheSettings()
    
    
    public UnaryCallSettings<ResumeAnywhereCacheRequest,AnywhereCache> resumeAnywhereCacheSettings()

Returns the object with the settings used for calls to resumeAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResumeAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ResumeAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### summarizeIntelligenceFindingsSettings()
    
    
    public PagedCallSettings<SummarizeIntelligenceFindingsRequest,SummarizeIntelligenceFindingsResponse,StorageControlClient.SummarizeIntelligenceFindingsPagedResponse> summarizeIntelligenceFindingsSettings()

Returns the object with the settings used for calls to summarizeIntelligenceFindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SummarizeIntelligenceFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.SummarizeIntelligenceFindingsRequest),[SummarizeIntelligenceFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.SummarizeIntelligenceFindingsResponse),[SummarizeIntelligenceFindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.SummarizeIntelligenceFindingsPagedResponse)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public StorageControlStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[StorageControlStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.stub.StorageControlStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateAnywhereCacheOperationSettings()
    
    
    public OperationCallSettings<UpdateAnywhereCacheRequest,AnywhereCache,UpdateAnywhereCacheMetadata> updateAnywhereCacheOperationSettings()

Returns the object with the settings used for calls to updateAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheRequest),[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache),[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheMetadata)>` |   
  
### updateAnywhereCacheSettings()
    
    
    public UnaryCallSettings<UpdateAnywhereCacheRequest,Operation> updateAnywhereCacheSettings()

Returns the object with the settings used for calls to updateAnywhereCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFolderIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<UpdateFolderIntelligenceConfigRequest,IntelligenceConfig> updateFolderIntelligenceConfigSettings()

Returns the object with the settings used for calls to updateFolderIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateFolderIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateFolderIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### updateManagedFolderSettings()
    
    
    public UnaryCallSettings<UpdateManagedFolderRequest,ManagedFolder> updateManagedFolderSettings()

Returns the object with the settings used for calls to updateManagedFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateManagedFolderRequest),[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder)>` |   
  
### updateOrganizationIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<UpdateOrganizationIntelligenceConfigRequest,IntelligenceConfig> updateOrganizationIntelligenceConfigSettings()

Returns the object with the settings used for calls to updateOrganizationIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateOrganizationIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### updateProjectIntelligenceConfigSettings()
    
    
    public UnaryCallSettings<UpdateProjectIntelligenceConfigRequest,IntelligenceConfig> updateProjectIntelligenceConfigSettings()

Returns the object with the settings used for calls to updateProjectIntelligenceConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateProjectIntelligenceConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateProjectIntelligenceConfigRequest),[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)>` |   
  
### updateRapidCacheOperationSettings()
    
    
    public OperationCallSettings<UpdateRapidCacheRequest,RapidCache,UpdateRapidCacheMetadata> updateRapidCacheOperationSettings()

Returns the object with the settings used for calls to updateRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateRapidCacheRequest),[RapidCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RapidCache),[UpdateRapidCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateRapidCacheMetadata)>` |   
  
### updateRapidCacheSettings()
    
    
    public UnaryCallSettings<UpdateRapidCacheRequest,Operation> updateRapidCacheSettings()

Returns the object with the settings used for calls to updateRapidCache.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRapidCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateRapidCacheRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### viewObjectFullContextSettings()
    
    
    public UnaryCallSettings<ViewObjectFullContextRequest,ObjectFullContext> viewObjectFullContextSettings()

Returns the object with the settings used for calls to viewObjectFullContext.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ViewObjectFullContextRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ViewObjectFullContextRequest),[ObjectFullContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ObjectFullContext)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
