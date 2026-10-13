---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings
title: Class BackupForGKEStubSettings (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:53.173221+00:00
---

# Class BackupForGKEStubSettings (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackupForGKEStubSettings (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6  0.1.0 
    
    
    public class BackupForGKEStubSettings extends StubSettings<BackupForGKEStubSettings>

Settings class to configure an instance of [BackupForGKEStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStub).

The default instance has everything set to sensible defaults:

  * The default service address (gkebackup.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getBackupPlan:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackupForGKEStubSettings.Builder backupForGKESettingsBuilder =
         BackupForGKEStubSettings.newBuilder();
     backupForGKESettingsBuilder
         .getBackupPlanSettings()
         .setRetrySettings(
             backupForGKESettingsBuilder
                 .getBackupPlanSettings()
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
     BackupForGKEStubSettings backupForGKESettings = backupForGKESettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createBackupPlan:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BackupForGKEStubSettings.Builder backupForGKESettingsBuilder =
         BackupForGKEStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     backupForGKESettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > BackupForGKEStubSettings

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
    
    
    public static BackupForGKEStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[BackupForGKEStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static BackupForGKEStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupForGKEStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static BackupForGKEStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[BackupForGKEStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings.Builder)` |   
  
## Constructors 

### BackupForGKEStubSettings(BackupForGKEStubSettings.Builder settingsBuilder)
    
    
    protected BackupForGKEStubSettings(BackupForGKEStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[BackupForGKEStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings.Builder)`  
  
  
## Methods 

### createBackupChannelOperationSettings()
    
    
    public OperationCallSettings<CreateBackupChannelRequest,BackupChannel,OperationMetadata> createBackupChannelOperationSettings()

Returns the object with the settings used for calls to createBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupChannelRequest),[BackupChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupChannel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createBackupChannelSettings()
    
    
    public UnaryCallSettings<CreateBackupChannelRequest,Operation> createBackupChannelSettings()

Returns the object with the settings used for calls to createBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupOperationSettings()
    
    
    public OperationCallSettings<CreateBackupRequest,Backup,OperationMetadata> createBackupOperationSettings()

Returns the object with the settings used for calls to createBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createBackupPlanOperationSettings()
    
    
    public OperationCallSettings<CreateBackupPlanRequest,BackupPlan,OperationMetadata> createBackupPlanOperationSettings()

Returns the object with the settings used for calls to createBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createBackupPlanSettings()
    
    
    public UnaryCallSettings<CreateBackupPlanRequest,Operation> createBackupPlanSettings()

Returns the object with the settings used for calls to createBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupSettings()
    
    
    public UnaryCallSettings<CreateBackupRequest,Operation> createBackupSettings()

Returns the object with the settings used for calls to createBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRestoreChannelOperationSettings()
    
    
    public OperationCallSettings<CreateRestoreChannelRequest,RestoreChannel,OperationMetadata> createRestoreChannelOperationSettings()

Returns the object with the settings used for calls to createRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestoreChannelRequest),[RestoreChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreChannel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createRestoreChannelSettings()
    
    
    public UnaryCallSettings<CreateRestoreChannelRequest,Operation> createRestoreChannelSettings()

Returns the object with the settings used for calls to createRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestoreChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRestoreOperationSettings()
    
    
    public OperationCallSettings<CreateRestoreRequest,Restore,OperationMetadata> createRestoreOperationSettings()

Returns the object with the settings used for calls to createRestore.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestoreRequest),[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createRestorePlanOperationSettings()
    
    
    public OperationCallSettings<CreateRestorePlanRequest,RestorePlan,OperationMetadata> createRestorePlanOperationSettings()

Returns the object with the settings used for calls to createRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestorePlanRequest),[RestorePlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestorePlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### createRestorePlanSettings()
    
    
    public UnaryCallSettings<CreateRestorePlanRequest,Operation> createRestorePlanSettings()

Returns the object with the settings used for calls to createRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestorePlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRestoreSettings()
    
    
    public UnaryCallSettings<CreateRestoreRequest,Operation> createRestoreSettings()

Returns the object with the settings used for calls to createRestore.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.CreateRestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public BackupForGKEStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[BackupForGKEStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteBackupChannelOperationSettings()
    
    
    public OperationCallSettings<DeleteBackupChannelRequest,Empty,OperationMetadata> deleteBackupChannelOperationSettings()

Returns the object with the settings used for calls to deleteBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupChannelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteBackupChannelSettings()
    
    
    public UnaryCallSettings<DeleteBackupChannelRequest,Operation> deleteBackupChannelSettings()

Returns the object with the settings used for calls to deleteBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupOperationSettings()
    
    
    public OperationCallSettings<DeleteBackupRequest,Empty,OperationMetadata> deleteBackupOperationSettings()

Returns the object with the settings used for calls to deleteBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteBackupPlanOperationSettings()
    
    
    public OperationCallSettings<DeleteBackupPlanRequest,Empty,OperationMetadata> deleteBackupPlanOperationSettings()

Returns the object with the settings used for calls to deleteBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupPlanRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteBackupPlanSettings()
    
    
    public UnaryCallSettings<DeleteBackupPlanRequest,Operation> deleteBackupPlanSettings()

Returns the object with the settings used for calls to deleteBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupSettings()
    
    
    public UnaryCallSettings<DeleteBackupRequest,Operation> deleteBackupSettings()

Returns the object with the settings used for calls to deleteBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRestoreChannelOperationSettings()
    
    
    public OperationCallSettings<DeleteRestoreChannelRequest,Empty,OperationMetadata> deleteRestoreChannelOperationSettings()

Returns the object with the settings used for calls to deleteRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestoreChannelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteRestoreChannelSettings()
    
    
    public UnaryCallSettings<DeleteRestoreChannelRequest,Operation> deleteRestoreChannelSettings()

Returns the object with the settings used for calls to deleteRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestoreChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRestoreOperationSettings()
    
    
    public OperationCallSettings<DeleteRestoreRequest,Empty,OperationMetadata> deleteRestoreOperationSettings()

Returns the object with the settings used for calls to deleteRestore.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteRestorePlanOperationSettings()
    
    
    public OperationCallSettings<DeleteRestorePlanRequest,Empty,OperationMetadata> deleteRestorePlanOperationSettings()

Returns the object with the settings used for calls to deleteRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestorePlanRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### deleteRestorePlanSettings()
    
    
    public UnaryCallSettings<DeleteRestorePlanRequest,Operation> deleteRestorePlanSettings()

Returns the object with the settings used for calls to deleteRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestorePlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRestoreSettings()
    
    
    public UnaryCallSettings<DeleteRestoreRequest,Operation> deleteRestoreSettings()

Returns the object with the settings used for calls to deleteRestore.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.DeleteRestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getBackupChannelSettings()
    
    
    public UnaryCallSettings<GetBackupChannelRequest,BackupChannel> getBackupChannelSettings()

Returns the object with the settings used for calls to getBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupChannelRequest),[BackupChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupChannel)>` |   
  
### getBackupIndexDownloadUrlSettings()
    
    
    public UnaryCallSettings<GetBackupIndexDownloadUrlRequest,GetBackupIndexDownloadUrlResponse> getBackupIndexDownloadUrlSettings()

Returns the object with the settings used for calls to getBackupIndexDownloadUrl.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupIndexDownloadUrlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupIndexDownloadUrlRequest),[GetBackupIndexDownloadUrlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupIndexDownloadUrlResponse)>` |   
  
### getBackupPlanBindingSettings()
    
    
    public UnaryCallSettings<GetBackupPlanBindingRequest,BackupPlanBinding> getBackupPlanBindingSettings()

Returns the object with the settings used for calls to getBackupPlanBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupPlanBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupPlanBindingRequest),[BackupPlanBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlanBinding)>` |   
  
### getBackupPlanSettings()
    
    
    public UnaryCallSettings<GetBackupPlanRequest,BackupPlan> getBackupPlanSettings()

Returns the object with the settings used for calls to getBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan)>` |   
  
### getBackupSettings()
    
    
    public UnaryCallSettings<GetBackupRequest,Backup> getBackupSettings()

Returns the object with the settings used for calls to getBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Backup)>` |   
  
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

### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getRestoreChannelSettings()
    
    
    public UnaryCallSettings<GetRestoreChannelRequest,RestoreChannel> getRestoreChannelSettings()

Returns the object with the settings used for calls to getRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetRestoreChannelRequest),[RestoreChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreChannel)>` |   
  
### getRestorePlanBindingSettings()
    
    
    public UnaryCallSettings<GetRestorePlanBindingRequest,RestorePlanBinding> getRestorePlanBindingSettings()

Returns the object with the settings used for calls to getRestorePlanBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRestorePlanBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetRestorePlanBindingRequest),[RestorePlanBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestorePlanBinding)>` |   
  
### getRestorePlanSettings()
    
    
    public UnaryCallSettings<GetRestorePlanRequest,RestorePlan> getRestorePlanSettings()

Returns the object with the settings used for calls to getRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetRestorePlanRequest),[RestorePlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestorePlan)>` |   
  
### getRestoreSettings()
    
    
    public UnaryCallSettings<GetRestoreRequest,Restore> getRestoreSettings()

Returns the object with the settings used for calls to getRestore.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetRestoreRequest),[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Restore)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getVolumeBackupSettings()
    
    
    public UnaryCallSettings<GetVolumeBackupRequest,VolumeBackup> getVolumeBackupSettings()

Returns the object with the settings used for calls to getVolumeBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVolumeBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetVolumeBackupRequest),[VolumeBackup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.VolumeBackup)>` |   
  
### getVolumeRestoreSettings()
    
    
    public UnaryCallSettings<GetVolumeRestoreRequest,VolumeRestore> getVolumeRestoreSettings()

Returns the object with the settings used for calls to getVolumeRestore.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetVolumeRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.GetVolumeRestoreRequest),[VolumeRestore](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.VolumeRestore)>` |   
  
### listBackupChannelsSettings()
    
    
    public PagedCallSettings<ListBackupChannelsRequest,ListBackupChannelsResponse,BackupForGKEClient.ListBackupChannelsPagedResponse> listBackupChannelsSettings()

Returns the object with the settings used for calls to listBackupChannels.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBackupChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupChannelsRequest),[ListBackupChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupChannelsResponse),[ListBackupChannelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListBackupChannelsPagedResponse)>` |   
  
### listBackupPlanBindingsSettings()
    
    
    public PagedCallSettings<ListBackupPlanBindingsRequest,ListBackupPlanBindingsResponse,BackupForGKEClient.ListBackupPlanBindingsPagedResponse> listBackupPlanBindingsSettings()

Returns the object with the settings used for calls to listBackupPlanBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBackupPlanBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupPlanBindingsRequest),[ListBackupPlanBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupPlanBindingsResponse),[ListBackupPlanBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListBackupPlanBindingsPagedResponse)>` |   
  
### listBackupPlansSettings()
    
    
    public PagedCallSettings<ListBackupPlansRequest,ListBackupPlansResponse,BackupForGKEClient.ListBackupPlansPagedResponse> listBackupPlansSettings()

Returns the object with the settings used for calls to listBackupPlans.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupPlansRequest),[ListBackupPlansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupPlansResponse),[ListBackupPlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListBackupPlansPagedResponse)>` |   
  
### listBackupsSettings()
    
    
    public PagedCallSettings<ListBackupsRequest,ListBackupsResponse,BackupForGKEClient.ListBackupsPagedResponse> listBackupsSettings()

Returns the object with the settings used for calls to listBackups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListBackupsResponse),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListBackupsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,BackupForGKEClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListLocationsPagedResponse)>` |   
  
### listRestoreChannelsSettings()
    
    
    public PagedCallSettings<ListRestoreChannelsRequest,ListRestoreChannelsResponse,BackupForGKEClient.ListRestoreChannelsPagedResponse> listRestoreChannelsSettings()

Returns the object with the settings used for calls to listRestoreChannels.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRestoreChannelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestoreChannelsRequest),[ListRestoreChannelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestoreChannelsResponse),[ListRestoreChannelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListRestoreChannelsPagedResponse)>` |   
  
### listRestorePlanBindingsSettings()
    
    
    public PagedCallSettings<ListRestorePlanBindingsRequest,ListRestorePlanBindingsResponse,BackupForGKEClient.ListRestorePlanBindingsPagedResponse> listRestorePlanBindingsSettings()

Returns the object with the settings used for calls to listRestorePlanBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRestorePlanBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestorePlanBindingsRequest),[ListRestorePlanBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestorePlanBindingsResponse),[ListRestorePlanBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListRestorePlanBindingsPagedResponse)>` |   
  
### listRestorePlansSettings()
    
    
    public PagedCallSettings<ListRestorePlansRequest,ListRestorePlansResponse,BackupForGKEClient.ListRestorePlansPagedResponse> listRestorePlansSettings()

Returns the object with the settings used for calls to listRestorePlans.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRestorePlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestorePlansRequest),[ListRestorePlansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestorePlansResponse),[ListRestorePlansPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListRestorePlansPagedResponse)>` |   
  
### listRestoresSettings()
    
    
    public PagedCallSettings<ListRestoresRequest,ListRestoresResponse,BackupForGKEClient.ListRestoresPagedResponse> listRestoresSettings()

Returns the object with the settings used for calls to listRestores.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestoresRequest),[ListRestoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListRestoresResponse),[ListRestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListRestoresPagedResponse)>` |   
  
### listVolumeBackupsSettings()
    
    
    public PagedCallSettings<ListVolumeBackupsRequest,ListVolumeBackupsResponse,BackupForGKEClient.ListVolumeBackupsPagedResponse> listVolumeBackupsSettings()

Returns the object with the settings used for calls to listVolumeBackups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVolumeBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListVolumeBackupsRequest),[ListVolumeBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListVolumeBackupsResponse),[ListVolumeBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListVolumeBackupsPagedResponse)>` |   
  
### listVolumeRestoresSettings()
    
    
    public PagedCallSettings<ListVolumeRestoresRequest,ListVolumeRestoresResponse,BackupForGKEClient.ListVolumeRestoresPagedResponse> listVolumeRestoresSettings()

Returns the object with the settings used for calls to listVolumeRestores.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListVolumeRestoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListVolumeRestoresRequest),[ListVolumeRestoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.ListVolumeRestoresResponse),[ListVolumeRestoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupForGKEClient.ListVolumeRestoresPagedResponse)>` |   
  
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
    
    
    public BackupForGKEStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[BackupForGKEStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.stub.BackupForGKEStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateBackupChannelOperationSettings()
    
    
    public OperationCallSettings<UpdateBackupChannelRequest,BackupChannel,OperationMetadata> updateBackupChannelOperationSettings()

Returns the object with the settings used for calls to updateBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupChannelRequest),[BackupChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupChannel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateBackupChannelSettings()
    
    
    public UnaryCallSettings<UpdateBackupChannelRequest,Operation> updateBackupChannelSettings()

Returns the object with the settings used for calls to updateBackupChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBackupChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupOperationSettings()
    
    
    public OperationCallSettings<UpdateBackupRequest,Backup,OperationMetadata> updateBackupOperationSettings()

Returns the object with the settings used for calls to updateBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateBackupPlanOperationSettings()
    
    
    public OperationCallSettings<UpdateBackupPlanRequest,BackupPlan,OperationMetadata> updateBackupPlanOperationSettings()

Returns the object with the settings used for calls to updateBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupPlanRequest),[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.BackupPlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateBackupPlanSettings()
    
    
    public UnaryCallSettings<UpdateBackupPlanRequest,Operation> updateBackupPlanSettings()

Returns the object with the settings used for calls to updateBackupPlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateBackupSettings()
    
    
    public UnaryCallSettings<UpdateBackupRequest,Operation> updateBackupSettings()

Returns the object with the settings used for calls to updateBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRestoreChannelOperationSettings()
    
    
    public OperationCallSettings<UpdateRestoreChannelRequest,RestoreChannel,OperationMetadata> updateRestoreChannelOperationSettings()

Returns the object with the settings used for calls to updateRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestoreChannelRequest),[RestoreChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestoreChannel),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateRestoreChannelSettings()
    
    
    public UnaryCallSettings<UpdateRestoreChannelRequest,Operation> updateRestoreChannelSettings()

Returns the object with the settings used for calls to updateRestoreChannel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRestoreChannelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestoreChannelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRestoreOperationSettings()
    
    
    public OperationCallSettings<UpdateRestoreRequest,Restore,OperationMetadata> updateRestoreOperationSettings()

Returns the object with the settings used for calls to updateRestore.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestoreRequest),[Restore](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.Restore),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateRestorePlanOperationSettings()
    
    
    public OperationCallSettings<UpdateRestorePlanRequest,RestorePlan,OperationMetadata> updateRestorePlanOperationSettings()

Returns the object with the settings used for calls to updateRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestorePlanRequest),[RestorePlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.RestorePlan),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.OperationMetadata)>` |   
  
### updateRestorePlanSettings()
    
    
    public UnaryCallSettings<UpdateRestorePlanRequest,Operation> updateRestorePlanSettings()

Returns the object with the settings used for calls to updateRestorePlan.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRestorePlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestorePlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateRestoreSettings()
    
    
    public UnaryCallSettings<UpdateRestoreRequest,Operation> updateRestoreSettings()

Returns the object with the settings used for calls to updateRestore.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRestoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gke-backup/latest/com.google.cloud.gkebackup.v1.UpdateRestoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
