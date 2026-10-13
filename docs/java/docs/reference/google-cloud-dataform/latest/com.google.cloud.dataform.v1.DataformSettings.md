---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings
title: Class DataformSettings (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:20:33.954611+00:00
---

# Class DataformSettings (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataformSettings (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public class DataformSettings extends ClientSettings<DataformSettings>

Settings class to configure an instance of [DataformClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1beta1.DataformClient).

The default instance has everything set to sensible defaults:

  * The default service address (dataform.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getTeamFolder:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataformSettings.Builder dataformSettingsBuilder = DataformSettings.newBuilder();
     dataformSettingsBuilder
         .getTeamFolderSettings()
         .setRetrySettings(
             dataformSettingsBuilder
                 .getTeamFolderSettings()
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
     DataformSettings dataformSettings = dataformSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for deleteTeamFolderTree:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataformSettings.Builder dataformSettingsBuilder = DataformSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     dataformSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > DataformSettings

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

### create(DataformStubSettings stub)
    
    
    public static final DataformSettings create(DataformStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataformStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.stub.DataformStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataformSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings)` |   
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
    
    
    public static DataformSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DataformSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static DataformSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataformSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static DataformSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DataformSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings.Builder)` |   
  
## Constructors 

### DataformSettings(DataformSettings.Builder settingsBuilder)
    
    
    protected DataformSettings(DataformSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[DataformSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings.Builder)`  
  
  
## Methods 

### cancelWorkflowInvocationSettings()
    
    
    public UnaryCallSettings<CancelWorkflowInvocationRequest,CancelWorkflowInvocationResponse> cancelWorkflowInvocationSettings()

Returns the object with the settings used for calls to cancelWorkflowInvocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CancelWorkflowInvocationRequest),[CancelWorkflowInvocationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CancelWorkflowInvocationResponse)>` |   
  
### commitRepositoryChangesSettings()
    
    
    public UnaryCallSettings<CommitRepositoryChangesRequest,CommitRepositoryChangesResponse> commitRepositoryChangesSettings()

Returns the object with the settings used for calls to commitRepositoryChanges.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CommitRepositoryChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitRepositoryChangesRequest),[CommitRepositoryChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitRepositoryChangesResponse)>` |   
  
### commitWorkspaceChangesSettings()
    
    
    public UnaryCallSettings<CommitWorkspaceChangesRequest,CommitWorkspaceChangesResponse> commitWorkspaceChangesSettings()

Returns the object with the settings used for calls to commitWorkspaceChanges.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitWorkspaceChangesRequest),[CommitWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CommitWorkspaceChangesResponse)>` |   
  
### computeRepositoryAccessTokenStatusSettings()
    
    
    public UnaryCallSettings<ComputeRepositoryAccessTokenStatusRequest,ComputeRepositoryAccessTokenStatusResponse> computeRepositoryAccessTokenStatusSettings()

Returns the object with the settings used for calls to computeRepositoryAccessTokenStatus.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ComputeRepositoryAccessTokenStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusRequest),[ComputeRepositoryAccessTokenStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ComputeRepositoryAccessTokenStatusResponse)>` |   
  
### createCompilationResultSettings()
    
    
    public UnaryCallSettings<CreateCompilationResultRequest,CompilationResult> createCompilationResultSettings()

Returns the object with the settings used for calls to createCompilationResult.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateCompilationResultRequest),[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CompilationResult)>` |   
  
### createFolderSettings()
    
    
    public UnaryCallSettings<CreateFolderRequest,Folder> createFolderSettings()

Returns the object with the settings used for calls to createFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>` |   
  
### createReleaseConfigSettings()
    
    
    public UnaryCallSettings<CreateReleaseConfigRequest,ReleaseConfig> createReleaseConfigSettings()

Returns the object with the settings used for calls to createReleaseConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>` |   
  
### createRepositorySettings()
    
    
    public UnaryCallSettings<CreateRepositoryRequest,Repository> createRepositorySettings()

Returns the object with the settings used for calls to createRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>` |   
  
### createTeamFolderSettings()
    
    
    public UnaryCallSettings<CreateTeamFolderRequest,TeamFolder> createTeamFolderSettings()

Returns the object with the settings used for calls to createTeamFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>` |   
  
### createWorkflowConfigSettings()
    
    
    public UnaryCallSettings<CreateWorkflowConfigRequest,WorkflowConfig> createWorkflowConfigSettings()

Returns the object with the settings used for calls to createWorkflowConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>` |   
  
### createWorkflowInvocationSettings()
    
    
    public UnaryCallSettings<CreateWorkflowInvocationRequest,WorkflowInvocation> createWorkflowInvocationSettings()

Returns the object with the settings used for calls to createWorkflowInvocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkflowInvocationRequest),[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation)>` |   
  
### createWorkspaceSettings()
    
    
    public UnaryCallSettings<CreateWorkspaceRequest,Workspace> createWorkspaceSettings()

Returns the object with the settings used for calls to createWorkspace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CreateWorkspaceRequest),[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Workspace)>` |   
  
### deleteFolderSettings()
    
    
    public UnaryCallSettings<DeleteFolderRequest,Empty> deleteFolderSettings()

Returns the object with the settings used for calls to deleteFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteFolderTreeOperationSettings()
    
    
    public OperationCallSettings<DeleteFolderTreeRequest,Empty,DeleteFolderTreeMetadata> deleteFolderTreeOperationSettings()

Returns the object with the settings used for calls to deleteFolderTree.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderTreeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderTreeMetadata)>` |   
  
### deleteFolderTreeSettings()
    
    
    public UnaryCallSettings<DeleteFolderTreeRequest,Operation> deleteFolderTreeSettings()

Returns the object with the settings used for calls to deleteFolderTree.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderTreeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteReleaseConfigSettings()
    
    
    public UnaryCallSettings<DeleteReleaseConfigRequest,Empty> deleteReleaseConfigSettings()

Returns the object with the settings used for calls to deleteReleaseConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteReleaseConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteRepositorySettings()
    
    
    public UnaryCallSettings<DeleteRepositoryRequest,Empty> deleteRepositorySettings()

Returns the object with the settings used for calls to deleteRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTeamFolderSettings()
    
    
    public UnaryCallSettings<DeleteTeamFolderRequest,Empty> deleteTeamFolderSettings()

Returns the object with the settings used for calls to deleteTeamFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteTeamFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTeamFolderTreeOperationSettings()
    
    
    public OperationCallSettings<DeleteTeamFolderTreeRequest,Empty,DeleteFolderTreeMetadata> deleteTeamFolderTreeOperationSettings()

Returns the object with the settings used for calls to deleteTeamFolderTree.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteTeamFolderTreeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteFolderTreeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteFolderTreeMetadata)>` |   
  
### deleteTeamFolderTreeSettings()
    
    
    public UnaryCallSettings<DeleteTeamFolderTreeRequest,Operation> deleteTeamFolderTreeSettings()

Returns the object with the settings used for calls to deleteTeamFolderTree.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTeamFolderTreeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteTeamFolderTreeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWorkflowConfigSettings()
    
    
    public UnaryCallSettings<DeleteWorkflowConfigRequest,Empty> deleteWorkflowConfigSettings()

Returns the object with the settings used for calls to deleteWorkflowConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkflowConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteWorkflowInvocationSettings()
    
    
    public UnaryCallSettings<DeleteWorkflowInvocationRequest,Empty> deleteWorkflowInvocationSettings()

Returns the object with the settings used for calls to deleteWorkflowInvocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkflowInvocationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteWorkspaceSettings()
    
    
    public UnaryCallSettings<DeleteWorkspaceRequest,Empty> deleteWorkspaceSettings()

Returns the object with the settings used for calls to deleteWorkspace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DeleteWorkspaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### fetchFileDiffSettings()
    
    
    public UnaryCallSettings<FetchFileDiffRequest,FetchFileDiffResponse> fetchFileDiffSettings()

Returns the object with the settings used for calls to fetchFileDiff.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchFileDiffRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileDiffRequest),[FetchFileDiffResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileDiffResponse)>` |   
  
### fetchFileGitStatusesSettings()
    
    
    public UnaryCallSettings<FetchFileGitStatusesRequest,FetchFileGitStatusesResponse> fetchFileGitStatusesSettings()

Returns the object with the settings used for calls to fetchFileGitStatuses.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchFileGitStatusesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileGitStatusesRequest),[FetchFileGitStatusesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchFileGitStatusesResponse)>` |   
  
### fetchGitAheadBehindSettings()
    
    
    public UnaryCallSettings<FetchGitAheadBehindRequest,FetchGitAheadBehindResponse> fetchGitAheadBehindSettings()

Returns the object with the settings used for calls to fetchGitAheadBehind.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchGitAheadBehindRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchGitAheadBehindRequest),[FetchGitAheadBehindResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchGitAheadBehindResponse)>` |   
  
### fetchRemoteBranchesSettings()
    
    
    public UnaryCallSettings<FetchRemoteBranchesRequest,FetchRemoteBranchesResponse> fetchRemoteBranchesSettings()

Returns the object with the settings used for calls to fetchRemoteBranches.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchRemoteBranchesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRemoteBranchesRequest),[FetchRemoteBranchesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRemoteBranchesResponse)>` |   
  
### fetchRepositoryHistorySettings()
    
    
    public PagedCallSettings<FetchRepositoryHistoryRequest,FetchRepositoryHistoryResponse,DataformClient.FetchRepositoryHistoryPagedResponse> fetchRepositoryHistorySettings()

Returns the object with the settings used for calls to fetchRepositoryHistory.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FetchRepositoryHistoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRepositoryHistoryRequest),[FetchRepositoryHistoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.FetchRepositoryHistoryResponse),[FetchRepositoryHistoryPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.FetchRepositoryHistoryPagedResponse)>` |   
  
### getCompilationResultSettings()
    
    
    public UnaryCallSettings<GetCompilationResultRequest,CompilationResult> getCompilationResultSettings()

Returns the object with the settings used for calls to getCompilationResult.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCompilationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetCompilationResultRequest),[CompilationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CompilationResult)>` |   
  
### getConfigSettings()
    
    
    public UnaryCallSettings<GetConfigRequest,Config> getConfigSettings()

Returns the object with the settings used for calls to getConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Config)>` |   
  
### getFolderSettings()
    
    
    public UnaryCallSettings<GetFolderRequest,Folder> getFolderSettings()

Returns the object with the settings used for calls to getFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getReleaseConfigSettings()
    
    
    public UnaryCallSettings<GetReleaseConfigRequest,ReleaseConfig> getReleaseConfigSettings()

Returns the object with the settings used for calls to getReleaseConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>` |   
  
### getRepositorySettings()
    
    
    public UnaryCallSettings<GetRepositoryRequest,Repository> getRepositorySettings()

Returns the object with the settings used for calls to getRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>` |   
  
### getTeamFolderSettings()
    
    
    public UnaryCallSettings<GetTeamFolderRequest,TeamFolder> getTeamFolderSettings()

Returns the object with the settings used for calls to getTeamFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>` |   
  
### getWorkflowConfigSettings()
    
    
    public UnaryCallSettings<GetWorkflowConfigRequest,WorkflowConfig> getWorkflowConfigSettings()

Returns the object with the settings used for calls to getWorkflowConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>` |   
  
### getWorkflowInvocationSettings()
    
    
    public UnaryCallSettings<GetWorkflowInvocationRequest,WorkflowInvocation> getWorkflowInvocationSettings()

Returns the object with the settings used for calls to getWorkflowInvocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkflowInvocationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkflowInvocationRequest),[WorkflowInvocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowInvocation)>` |   
  
### getWorkspaceSettings()
    
    
    public UnaryCallSettings<GetWorkspaceRequest,Workspace> getWorkspaceSettings()

Returns the object with the settings used for calls to getWorkspace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkspaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.GetWorkspaceRequest),[Workspace](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Workspace)>` |   
  
### installNpmPackagesSettings()
    
    
    public UnaryCallSettings<InstallNpmPackagesRequest,InstallNpmPackagesResponse> installNpmPackagesSettings()

Returns the object with the settings used for calls to installNpmPackages.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[InstallNpmPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InstallNpmPackagesRequest),[InstallNpmPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.InstallNpmPackagesResponse)>` |   
  
### listCompilationResultsSettings()
    
    
    public PagedCallSettings<ListCompilationResultsRequest,ListCompilationResultsResponse,DataformClient.ListCompilationResultsPagedResponse> listCompilationResultsSettings()

Returns the object with the settings used for calls to listCompilationResults.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCompilationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListCompilationResultsRequest),[ListCompilationResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListCompilationResultsResponse),[ListCompilationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListCompilationResultsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,DataformClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListLocationsPagedResponse)>` |   
  
### listReleaseConfigsSettings()
    
    
    public PagedCallSettings<ListReleaseConfigsRequest,ListReleaseConfigsResponse,DataformClient.ListReleaseConfigsPagedResponse> listReleaseConfigsSettings()

Returns the object with the settings used for calls to listReleaseConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListReleaseConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListReleaseConfigsRequest),[ListReleaseConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListReleaseConfigsResponse),[ListReleaseConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListReleaseConfigsPagedResponse)>` |   
  
### listRepositoriesSettings()
    
    
    public PagedCallSettings<ListRepositoriesRequest,ListRepositoriesResponse,DataformClient.ListRepositoriesPagedResponse> listRepositoriesSettings()

Returns the object with the settings used for calls to listRepositories.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListRepositoriesRequest),[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListRepositoriesResponse),[ListRepositoriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListRepositoriesPagedResponse)>` |   
  
### listWorkflowConfigsSettings()
    
    
    public PagedCallSettings<ListWorkflowConfigsRequest,ListWorkflowConfigsResponse,DataformClient.ListWorkflowConfigsPagedResponse> listWorkflowConfigsSettings()

Returns the object with the settings used for calls to listWorkflowConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkflowConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowConfigsRequest),[ListWorkflowConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowConfigsResponse),[ListWorkflowConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListWorkflowConfigsPagedResponse)>` |   
  
### listWorkflowInvocationsSettings()
    
    
    public PagedCallSettings<ListWorkflowInvocationsRequest,ListWorkflowInvocationsResponse,DataformClient.ListWorkflowInvocationsPagedResponse> listWorkflowInvocationsSettings()

Returns the object with the settings used for calls to listWorkflowInvocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkflowInvocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowInvocationsRequest),[ListWorkflowInvocationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkflowInvocationsResponse),[ListWorkflowInvocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListWorkflowInvocationsPagedResponse)>` |   
  
### listWorkspacesSettings()
    
    
    public PagedCallSettings<ListWorkspacesRequest,ListWorkspacesResponse,DataformClient.ListWorkspacesPagedResponse> listWorkspacesSettings()

Returns the object with the settings used for calls to listWorkspaces.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkspacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkspacesRequest),[ListWorkspacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ListWorkspacesResponse),[ListWorkspacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.ListWorkspacesPagedResponse)>` |   
  
### makeDirectorySettings()
    
    
    public UnaryCallSettings<MakeDirectoryRequest,MakeDirectoryResponse> makeDirectorySettings()

Returns the object with the settings used for calls to makeDirectory.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MakeDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MakeDirectoryRequest),[MakeDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MakeDirectoryResponse)>` |   
  
### moveDirectorySettings()
    
    
    public UnaryCallSettings<MoveDirectoryRequest,MoveDirectoryResponse> moveDirectorySettings()

Returns the object with the settings used for calls to moveDirectory.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveDirectoryRequest),[MoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveDirectoryResponse)>` |   
  
### moveFileSettings()
    
    
    public UnaryCallSettings<MoveFileRequest,MoveFileResponse> moveFileSettings()

Returns the object with the settings used for calls to moveFile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFileRequest),[MoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFileResponse)>` |   
  
### moveFolderOperationSettings()
    
    
    public OperationCallSettings<MoveFolderRequest,Empty,MoveFolderMetadata> moveFolderOperationSettings()

Returns the object with the settings used for calls to moveFolder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFolderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFolderMetadata)>` |   
  
### moveFolderSettings()
    
    
    public UnaryCallSettings<MoveFolderRequest,Operation> moveFolderSettings()

Returns the object with the settings used for calls to moveFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveFolderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### moveRepositoryOperationSettings()
    
    
    public OperationCallSettings<MoveRepositoryRequest,Empty,MoveRepositoryMetadata> moveRepositoryOperationSettings()

Returns the object with the settings used for calls to moveRepository.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveRepositoryRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[MoveRepositoryMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveRepositoryMetadata)>` |   
  
### moveRepositorySettings()
    
    
    public UnaryCallSettings<MoveRepositoryRequest,Operation> moveRepositorySettings()

Returns the object with the settings used for calls to moveRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.MoveRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### pullGitCommitsSettings()
    
    
    public UnaryCallSettings<PullGitCommitsRequest,PullGitCommitsResponse> pullGitCommitsSettings()

Returns the object with the settings used for calls to pullGitCommits.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PullGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PullGitCommitsRequest),[PullGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PullGitCommitsResponse)>` |   
  
### pushGitCommitsSettings()
    
    
    public UnaryCallSettings<PushGitCommitsRequest,PushGitCommitsResponse> pushGitCommitsSettings()

Returns the object with the settings used for calls to pushGitCommits.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PushGitCommitsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PushGitCommitsRequest),[PushGitCommitsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.PushGitCommitsResponse)>` |   
  
### queryCompilationResultActionsSettings()
    
    
    public PagedCallSettings<QueryCompilationResultActionsRequest,QueryCompilationResultActionsResponse,DataformClient.QueryCompilationResultActionsPagedResponse> queryCompilationResultActionsSettings()

Returns the object with the settings used for calls to queryCompilationResultActions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryCompilationResultActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryCompilationResultActionsRequest),[QueryCompilationResultActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryCompilationResultActionsResponse),[QueryCompilationResultActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryCompilationResultActionsPagedResponse)>` |   
  
### queryDirectoryContentsSettings()
    
    
    public PagedCallSettings<QueryDirectoryContentsRequest,QueryDirectoryContentsResponse,DataformClient.QueryDirectoryContentsPagedResponse> queryDirectoryContentsSettings()

Returns the object with the settings used for calls to queryDirectoryContents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryDirectoryContentsRequest),[QueryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryDirectoryContentsResponse),[QueryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryDirectoryContentsPagedResponse)>` |   
  
### queryFolderContentsSettings()
    
    
    public PagedCallSettings<QueryFolderContentsRequest,QueryFolderContentsResponse,DataformClient.QueryFolderContentsPagedResponse> queryFolderContentsSettings()

Returns the object with the settings used for calls to queryFolderContents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryFolderContentsRequest),[QueryFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryFolderContentsResponse),[QueryFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryFolderContentsPagedResponse)>` |   
  
### queryRepositoryDirectoryContentsSettings()
    
    
    public PagedCallSettings<QueryRepositoryDirectoryContentsRequest,QueryRepositoryDirectoryContentsResponse,DataformClient.QueryRepositoryDirectoryContentsPagedResponse> queryRepositoryDirectoryContentsSettings()

Returns the object with the settings used for calls to queryRepositoryDirectoryContents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryRepositoryDirectoryContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryRepositoryDirectoryContentsRequest),[QueryRepositoryDirectoryContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryRepositoryDirectoryContentsResponse),[QueryRepositoryDirectoryContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryRepositoryDirectoryContentsPagedResponse)>` |   
  
### queryTeamFolderContentsSettings()
    
    
    public PagedCallSettings<QueryTeamFolderContentsRequest,QueryTeamFolderContentsResponse,DataformClient.QueryTeamFolderContentsPagedResponse> queryTeamFolderContentsSettings()

Returns the object with the settings used for calls to queryTeamFolderContents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryTeamFolderContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryTeamFolderContentsRequest),[QueryTeamFolderContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryTeamFolderContentsResponse),[QueryTeamFolderContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryTeamFolderContentsPagedResponse)>` |   
  
### queryUserRootContentsSettings()
    
    
    public PagedCallSettings<QueryUserRootContentsRequest,QueryUserRootContentsResponse,DataformClient.QueryUserRootContentsPagedResponse> queryUserRootContentsSettings()

Returns the object with the settings used for calls to queryUserRootContents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryUserRootContentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryUserRootContentsRequest),[QueryUserRootContentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryUserRootContentsResponse),[QueryUserRootContentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryUserRootContentsPagedResponse)>` |   
  
### queryWorkflowInvocationActionsSettings()
    
    
    public PagedCallSettings<QueryWorkflowInvocationActionsRequest,QueryWorkflowInvocationActionsResponse,DataformClient.QueryWorkflowInvocationActionsPagedResponse> queryWorkflowInvocationActionsSettings()

Returns the object with the settings used for calls to queryWorkflowInvocationActions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[QueryWorkflowInvocationActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryWorkflowInvocationActionsRequest),[QueryWorkflowInvocationActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.QueryWorkflowInvocationActionsResponse),[QueryWorkflowInvocationActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.QueryWorkflowInvocationActionsPagedResponse)>` |   
  
### readFileSettings()
    
    
    public UnaryCallSettings<ReadFileRequest,ReadFileResponse> readFileSettings()

Returns the object with the settings used for calls to readFile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReadFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadFileRequest),[ReadFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadFileResponse)>` |   
  
### readRepositoryFileSettings()
    
    
    public UnaryCallSettings<ReadRepositoryFileRequest,ReadRepositoryFileResponse> readRepositoryFileSettings()

Returns the object with the settings used for calls to readRepositoryFile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReadRepositoryFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadRepositoryFileRequest),[ReadRepositoryFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReadRepositoryFileResponse)>` |   
  
### removeDirectorySettings()
    
    
    public UnaryCallSettings<RemoveDirectoryRequest,RemoveDirectoryResponse> removeDirectorySettings()

Returns the object with the settings used for calls to removeDirectory.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveDirectoryRequest),[RemoveDirectoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveDirectoryResponse)>` |   
  
### removeFileSettings()
    
    
    public UnaryCallSettings<RemoveFileRequest,RemoveFileResponse> removeFileSettings()

Returns the object with the settings used for calls to removeFile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveFileRequest),[RemoveFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.RemoveFileResponse)>` |   
  
### resetWorkspaceChangesSettings()
    
    
    public UnaryCallSettings<ResetWorkspaceChangesRequest,ResetWorkspaceChangesResponse> resetWorkspaceChangesSettings()

Returns the object with the settings used for calls to resetWorkspaceChanges.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetWorkspaceChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ResetWorkspaceChangesRequest),[ResetWorkspaceChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ResetWorkspaceChangesResponse)>` |   
  
### searchFilesSettings()
    
    
    public PagedCallSettings<SearchFilesRequest,SearchFilesResponse,DataformClient.SearchFilesPagedResponse> searchFilesSettings()

Returns the object with the settings used for calls to searchFiles.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchFilesRequest),[SearchFilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchFilesResponse),[SearchFilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.SearchFilesPagedResponse)>` |   
  
### searchTeamFoldersSettings()
    
    
    public PagedCallSettings<SearchTeamFoldersRequest,SearchTeamFoldersResponse,DataformClient.SearchTeamFoldersPagedResponse> searchTeamFoldersSettings()

Returns the object with the settings used for calls to searchTeamFolders.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchTeamFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchTeamFoldersRequest),[SearchTeamFoldersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.SearchTeamFoldersResponse),[SearchTeamFoldersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformClient.SearchTeamFoldersPagedResponse)>` |   
  
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
    
    
    public DataformSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[DataformSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.DataformSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateConfigSettings()
    
    
    public UnaryCallSettings<UpdateConfigRequest,Config> updateConfigSettings()

Returns the object with the settings used for calls to updateConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateConfigRequest),[Config](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Config)>` |   
  
### updateFolderSettings()
    
    
    public UnaryCallSettings<UpdateFolderRequest,Folder> updateFolderSettings()

Returns the object with the settings used for calls to updateFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateFolderRequest),[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Folder)>` |   
  
### updateReleaseConfigSettings()
    
    
    public UnaryCallSettings<UpdateReleaseConfigRequest,ReleaseConfig> updateReleaseConfigSettings()

Returns the object with the settings used for calls to updateReleaseConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateReleaseConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateReleaseConfigRequest),[ReleaseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig)>` |   
  
### updateRepositorySettings()
    
    
    public UnaryCallSettings<UpdateRepositoryRequest,Repository> updateRepositorySettings()

Returns the object with the settings used for calls to updateRepository.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.Repository)>` |   
  
### updateTeamFolderSettings()
    
    
    public UnaryCallSettings<UpdateTeamFolderRequest,TeamFolder> updateTeamFolderSettings()

Returns the object with the settings used for calls to updateTeamFolder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTeamFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateTeamFolderRequest),[TeamFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.TeamFolder)>` |   
  
### updateWorkflowConfigSettings()
    
    
    public UnaryCallSettings<UpdateWorkflowConfigRequest,WorkflowConfig> updateWorkflowConfigSettings()

Returns the object with the settings used for calls to updateWorkflowConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateWorkflowConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.UpdateWorkflowConfigRequest),[WorkflowConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WorkflowConfig)>` |   
  
### writeFileSettings()
    
    
    public UnaryCallSettings<WriteFileRequest,WriteFileResponse> writeFileSettings()

Returns the object with the settings used for calls to writeFile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[WriteFileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WriteFileRequest),[WriteFileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.WriteFileResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
