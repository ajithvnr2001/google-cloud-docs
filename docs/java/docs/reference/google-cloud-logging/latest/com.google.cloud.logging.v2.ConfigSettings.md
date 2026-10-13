---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings
title: Class ConfigSettings (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:09.878744+00:00
---

# Class ConfigSettings (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfigSettings (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class ConfigSettings extends ClientSettings<ConfigSettings>

Settings class to configure an instance of [ConfigClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient).

The default instance has everything set to sensible defaults:

  * The default service address (logging.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getBucket:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings.Builder configSettingsBuilder = ConfigSettings.newBuilder();
     configSettingsBuilder
         .getBucketSettings()
         .setRetrySettings(
             configSettingsBuilder
                 .getBucketSettings()
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
     ConfigSettings configSettings = configSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createBucketAsync:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ConfigSettings.Builder configSettingsBuilder = ConfigSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     configSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > ConfigSettings

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

### create(ConfigServiceV2StubSettings stub)
    
    
    public static final ConfigSettings create(ConfigServiceV2StubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ConfigServiceV2StubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.stub.ConfigServiceV2StubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings)` |   
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
    
    
    public static ConfigSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ConfigSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static ConfigSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings.Builder)` |   
  
## Constructors 

### ConfigSettings(ConfigSettings.Builder settingsBuilder)
    
    
    protected ConfigSettings(ConfigSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[ConfigSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings.Builder)`  
  
  
## Methods 

### copyLogEntriesOperationSettings()
    
    
    public OperationCallSettings<CopyLogEntriesRequest,CopyLogEntriesResponse,CopyLogEntriesMetadata> copyLogEntriesOperationSettings()

Returns the object with the settings used for calls to copyLogEntries.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CopyLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesRequest),[CopyLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesResponse),[CopyLogEntriesMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesMetadata)>` |   
  
### copyLogEntriesSettings()
    
    
    public UnaryCallSettings<CopyLogEntriesRequest,Operation> copyLogEntriesSettings()

Returns the object with the settings used for calls to copyLogEntries.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CopyLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CopyLogEntriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBucketAsyncOperationSettings()
    
    
    public OperationCallSettings<CreateBucketRequest,LogBucket,BucketMetadata> createBucketAsyncOperationSettings()

Returns the object with the settings used for calls to createBucketAsync.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### createBucketAsyncSettings()
    
    
    public UnaryCallSettings<CreateBucketRequest,Operation> createBucketAsyncSettings()

Returns the object with the settings used for calls to createBucketAsync.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBucketSettings()
    
    
    public UnaryCallSettings<CreateBucketRequest,LogBucket> createBucketSettings()

Returns the object with the settings used for calls to createBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### createExclusionSettings()
    
    
    public UnaryCallSettings<CreateExclusionRequest,LogExclusion> createExclusionSettings()

Returns the object with the settings used for calls to createExclusion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### createLinkOperationSettings()
    
    
    public OperationCallSettings<CreateLinkRequest,Link,LinkMetadata> createLinkOperationSettings()

Returns the object with the settings used for calls to createLink.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLinkRequest),[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### createLinkSettings()
    
    
    public UnaryCallSettings<CreateLinkRequest,Operation> createLinkSettings()

Returns the object with the settings used for calls to createLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateLinkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSinkSettings()
    
    
    public UnaryCallSettings<CreateSinkRequest,LogSink> createSinkSettings()

Returns the object with the settings used for calls to createSink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### createViewSettings()
    
    
    public UnaryCallSettings<CreateViewRequest,LogView> createViewSettings()

Returns the object with the settings used for calls to createView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CreateViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
### deleteBucketSettings()
    
    
    public UnaryCallSettings<DeleteBucketRequest,Empty> deleteBucketSettings()

Returns the object with the settings used for calls to deleteBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteBucketRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteExclusionSettings()
    
    
    public UnaryCallSettings<DeleteExclusionRequest,Empty> deleteExclusionSettings()

Returns the object with the settings used for calls to deleteExclusion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteExclusionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteLinkOperationSettings()
    
    
    public OperationCallSettings<DeleteLinkRequest,Empty,LinkMetadata> deleteLinkOperationSettings()

Returns the object with the settings used for calls to deleteLink.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[LinkMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LinkMetadata)>` |   
  
### deleteLinkSettings()
    
    
    public UnaryCallSettings<DeleteLinkRequest,Operation> deleteLinkSettings()

Returns the object with the settings used for calls to deleteLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteLinkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSinkSettings()
    
    
    public UnaryCallSettings<DeleteSinkRequest,Empty> deleteSinkSettings()

Returns the object with the settings used for calls to deleteSink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteSinkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteViewSettings()
    
    
    public UnaryCallSettings<DeleteViewRequest,Empty> deleteViewSettings()

Returns the object with the settings used for calls to deleteView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.DeleteViewRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getBucketSettings()
    
    
    public UnaryCallSettings<GetBucketRequest,LogBucket> getBucketSettings()

Returns the object with the settings used for calls to getBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### getCmekSettingsSettings()
    
    
    public UnaryCallSettings<GetCmekSettingsRequest,CmekSettings> getCmekSettingsSettings()

Returns the object with the settings used for calls to getCmekSettings.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetCmekSettingsRequest),[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)>` |   
  
### getExclusionSettings()
    
    
    public UnaryCallSettings<GetExclusionRequest,LogExclusion> getExclusionSettings()

Returns the object with the settings used for calls to getExclusion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### getLinkSettings()
    
    
    public UnaryCallSettings<GetLinkRequest,Link> getLinkSettings()

Returns the object with the settings used for calls to getLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetLinkRequest),[Link](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Link)>` |   
  
### getSettingsSettings()
    
    
    public UnaryCallSettings<GetSettingsRequest,Settings> getSettingsSettings()

Returns the object with the settings used for calls to getSettings.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)>` |   
  
### getSinkSettings()
    
    
    public UnaryCallSettings<GetSinkRequest,LogSink> getSinkSettings()

Returns the object with the settings used for calls to getSink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### getViewSettings()
    
    
    public UnaryCallSettings<GetViewRequest,LogView> getViewSettings()

Returns the object with the settings used for calls to getView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.GetViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
### listBucketsSettings()
    
    
    public PagedCallSettings<ListBucketsRequest,ListBucketsResponse,ConfigClient.ListBucketsPagedResponse> listBucketsSettings()

Returns the object with the settings used for calls to listBuckets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsRequest),[ListBucketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListBucketsResponse),[ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListBucketsPagedResponse)>` |   
  
### listExclusionsSettings()
    
    
    public PagedCallSettings<ListExclusionsRequest,ListExclusionsResponse,ConfigClient.ListExclusionsPagedResponse> listExclusionsSettings()

Returns the object with the settings used for calls to listExclusions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListExclusionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsRequest),[ListExclusionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListExclusionsResponse),[ListExclusionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListExclusionsPagedResponse)>` |   
  
### listLinksSettings()
    
    
    public PagedCallSettings<ListLinksRequest,ListLinksResponse,ConfigClient.ListLinksPagedResponse> listLinksSettings()

Returns the object with the settings used for calls to listLinks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksRequest),[ListLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListLinksResponse),[ListLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListLinksPagedResponse)>` |   
  
### listSinksSettings()
    
    
    public PagedCallSettings<ListSinksRequest,ListSinksResponse,ConfigClient.ListSinksPagedResponse> listSinksSettings()

Returns the object with the settings used for calls to listSinks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksRequest),[ListSinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListSinksResponse),[ListSinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListSinksPagedResponse)>` |   
  
### listViewsSettings()
    
    
    public PagedCallSettings<ListViewsRequest,ListViewsResponse,ConfigClient.ListViewsPagedResponse> listViewsSettings()

Returns the object with the settings used for calls to listViews.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsRequest),[ListViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.ListViewsResponse),[ListViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigClient.ListViewsPagedResponse)>` |   
  
### toBuilder()
    
    
    public ConfigSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[ConfigSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.v2.ConfigSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### undeleteBucketSettings()
    
    
    public UnaryCallSettings<UndeleteBucketRequest,Empty> undeleteBucketSettings()

Returns the object with the settings used for calls to undeleteBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UndeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UndeleteBucketRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### updateBucketAsyncOperationSettings()
    
    
    public OperationCallSettings<UpdateBucketRequest,LogBucket,BucketMetadata> updateBucketAsyncOperationSettings()

Returns the object with the settings used for calls to updateBucketAsync.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket),[BucketMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.BucketMetadata)>` |   
  
### updateBucketAsyncSettings()
    
    
    public UnaryCallSettings<UpdateBucketRequest,Operation> updateBucketAsyncSettings()

Returns the object with the settings used for calls to updateBucketAsync.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBucketSettings()
    
    
    public UnaryCallSettings<UpdateBucketRequest,LogBucket> updateBucketSettings()

Returns the object with the settings used for calls to updateBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateBucketRequest),[LogBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogBucket)>` |   
  
### updateCmekSettingsSettings()
    
    
    public UnaryCallSettings<UpdateCmekSettingsRequest,CmekSettings> updateCmekSettingsSettings()

Returns the object with the settings used for calls to updateCmekSettings.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCmekSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateCmekSettingsRequest),[CmekSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.CmekSettings)>` |   
  
### updateExclusionSettings()
    
    
    public UnaryCallSettings<UpdateExclusionRequest,LogExclusion> updateExclusionSettings()

Returns the object with the settings used for calls to updateExclusion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateExclusionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateExclusionRequest),[LogExclusion](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogExclusion)>` |   
  
### updateSettingsSettings()
    
    
    public UnaryCallSettings<UpdateSettingsRequest,Settings> updateSettingsSettings()

Returns the object with the settings used for calls to updateSettings.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSettingsRequest),[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.Settings)>` |   
  
### updateSinkSettings()
    
    
    public UnaryCallSettings<UpdateSinkRequest,LogSink> updateSinkSettings()

Returns the object with the settings used for calls to updateSink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateSinkRequest),[LogSink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSink)>` |   
  
### updateViewSettings()
    
    
    public UnaryCallSettings<UpdateViewRequest,LogView> updateViewSettings()

Returns the object with the settings used for calls to updateView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.UpdateViewRequest),[LogView](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogView)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
