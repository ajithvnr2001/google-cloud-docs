---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings
title: Class RepositoryManagerStubSettings (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:29.136208+00:00
---

# Class RepositoryManagerStubSettings (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RepositoryManagerStubSettings (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public class RepositoryManagerStubSettings extends StubSettings<RepositoryManagerStubSettings>

Settings class to configure an instance of [RepositoryManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStub).

The default instance has everything set to sensible defaults:

  * The default service address (cloudbuild.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getConnection:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RepositoryManagerStubSettings.Builder repositoryManagerSettingsBuilder =
         RepositoryManagerStubSettings.newBuilder();
     repositoryManagerSettingsBuilder
         .getConnectionSettings()
         .setRetrySettings(
             repositoryManagerSettingsBuilder
                 .getConnectionSettings()
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
     RepositoryManagerStubSettings repositoryManagerSettings =
         repositoryManagerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createConnection:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RepositoryManagerStubSettings.Builder repositoryManagerSettingsBuilder =
         RepositoryManagerStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     repositoryManagerSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > RepositoryManagerStubSettings

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
    
    
    public static RepositoryManagerStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static RepositoryManagerStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static RepositoryManagerStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings.Builder)` |   
  
## Constructors 

### RepositoryManagerStubSettings(RepositoryManagerStubSettings.Builder settingsBuilder)
    
    
    protected RepositoryManagerStubSettings(RepositoryManagerStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[RepositoryManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings.Builder)`  
  
  
## Methods 

### batchCreateRepositoriesOperationSettings()
    
    
    public OperationCallSettings<BatchCreateRepositoriesRequest,BatchCreateRepositoriesResponse,OperationMetadata> batchCreateRepositoriesOperationSettings()

Returns the object with the settings used for calls to batchCreateRepositories.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[BatchCreateRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesRequest),[BatchCreateRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### batchCreateRepositoriesSettings()
    
    
    public UnaryCallSettings<BatchCreateRepositoriesRequest,Operation> batchCreateRepositoriesSettings()

Returns the object with the settings used for calls to batchCreateRepositories.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchCreateRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createConnectionOperationSettings()
    
    
    public OperationCallSettings<CreateConnectionRequest,Connection,OperationMetadata> createConnectionOperationSettings()

Returns the object with the settings used for calls to createConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### createConnectionSettings()
    
    
    public UnaryCallSettings<CreateConnectionRequest,Operation> createConnectionSettings()

Returns the object with the settings used for calls to createConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRepositoryOperationSettings()
    
    
    public OperationCallSettings<CreateRepositoryRequest,Repository,OperationMetadata> createRepositoryOperationSettings()

Returns the object with the settings used for calls to createRepository.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Repository),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### createRepositorySettings()
    
    
    public UnaryCallSettings<CreateRepositoryRequest,Operation> createRepositorySettings()

Returns the object with the settings used for calls to createRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public RepositoryManagerStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteConnectionOperationSettings()
    
    
    public OperationCallSettings<DeleteConnectionRequest,Empty,OperationMetadata> deleteConnectionOperationSettings()

Returns the object with the settings used for calls to deleteConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### deleteConnectionSettings()
    
    
    public UnaryCallSettings<DeleteConnectionRequest,Operation> deleteConnectionSettings()

Returns the object with the settings used for calls to deleteConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRepositoryOperationSettings()
    
    
    public OperationCallSettings<DeleteRepositoryRequest,Empty,OperationMetadata> deleteRepositoryOperationSettings()

Returns the object with the settings used for calls to deleteRepository.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### deleteRepositorySettings()
    
    
    public UnaryCallSettings<DeleteRepositoryRequest,Operation> deleteRepositorySettings()

Returns the object with the settings used for calls to deleteRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### fetchGitRefsSettings()
    
    
    public UnaryCallSettings<FetchGitRefsRequest,FetchGitRefsResponse> fetchGitRefsSettings()

Returns the object with the settings used for calls to fetchGitRefs.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchGitRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsRequest),[FetchGitRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsResponse)>` |   
  
### fetchLinkableRepositoriesSettings()
    
    
    public PagedCallSettings<FetchLinkableRepositoriesRequest,FetchLinkableRepositoriesResponse,RepositoryManagerClient.FetchLinkableRepositoriesPagedResponse> fetchLinkableRepositoriesSettings()

Returns the object with the settings used for calls to fetchLinkableRepositories.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesRequest),[FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesResponse),[FetchLinkableRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.RepositoryManagerClient.FetchLinkableRepositoriesPagedResponse)>` |   
  
### fetchReadTokenSettings()
    
    
    public UnaryCallSettings<FetchReadTokenRequest,FetchReadTokenResponse> fetchReadTokenSettings()

Returns the object with the settings used for calls to fetchReadToken.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchReadTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenRequest),[FetchReadTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenResponse)>` |   
  
### fetchReadWriteTokenSettings()
    
    
    public UnaryCallSettings<FetchReadWriteTokenRequest,FetchReadWriteTokenResponse> fetchReadWriteTokenSettings()

Returns the object with the settings used for calls to fetchReadWriteToken.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchReadWriteTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenRequest),[FetchReadWriteTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenResponse)>` |   
  
### getConnectionSettings()
    
    
    public UnaryCallSettings<GetConnectionRequest,Connection> getConnectionSettings()

Returns the object with the settings used for calls to getConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getRepositorySettings()
    
    
    public UnaryCallSettings<GetRepositoryRequest,Repository> getRepositorySettings()

Returns the object with the settings used for calls to getRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Repository)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listConnectionsSettings()
    
    
    public PagedCallSettings<ListConnectionsRequest,ListConnectionsResponse,RepositoryManagerClient.ListConnectionsPagedResponse> listConnectionsSettings()

Returns the object with the settings used for calls to listConnections.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsRequest),[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsResponse),[ListConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.RepositoryManagerClient.ListConnectionsPagedResponse)>` |   
  
### listRepositoriesSettings()
    
    
    public PagedCallSettings<ListRepositoriesRequest,ListRepositoriesResponse,RepositoryManagerClient.ListRepositoriesPagedResponse> listRepositoriesSettings()

Returns the object with the settings used for calls to listRepositories.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesRequest),[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesResponse),[ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.RepositoryManagerClient.ListRepositoriesPagedResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public RepositoryManagerStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v2.stub.RepositoryManagerStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateConnectionOperationSettings()
    
    
    public OperationCallSettings<UpdateConnectionRequest,Connection,OperationMetadata> updateConnectionOperationSettings()

Returns the object with the settings used for calls to updateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.OperationMetadata)>` |   
  
### updateConnectionSettings()
    
    
    public UnaryCallSettings<UpdateConnectionRequest,Operation> updateConnectionSettings()

Returns the object with the settings used for calls to updateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
