---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings
title: Class CloudTasksStubSettings (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:39.902181+00:00
---

# Class CloudTasksStubSettings (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudTasksStubSettings (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.12  2.2.0  2.1.11 
    
    
    public class CloudTasksStubSettings extends StubSettings<CloudTasksStubSettings>

Settings class to configure an instance of [CloudTasksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStub).

The default instance has everything set to sensible defaults:

  * The default service address (cloudtasks.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getQueue:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudTasksStubSettings.Builder cloudTasksSettingsBuilder = CloudTasksStubSettings.newBuilder();
     cloudTasksSettingsBuilder
         .getQueueSettings()
         .setRetrySettings(
             cloudTasksSettingsBuilder
                 .getQueueSettings()
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
     CloudTasksStubSettings cloudTasksSettings = cloudTasksSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for batchCreateTasks:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudTasksStubSettings.Builder cloudTasksSettingsBuilder = CloudTasksStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     cloudTasksSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > CloudTasksStubSettings

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
    
    
    public static CloudTasksStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudTasksStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static CloudTasksStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudTasksStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static CloudTasksStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudTasksStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings.Builder)` |   
  
## Constructors 

### CloudTasksStubSettings(CloudTasksStubSettings.Builder settingsBuilder)
    
    
    protected CloudTasksStubSettings(CloudTasksStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[CloudTasksStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings.Builder)`  
  
  
## Methods 

### batchCreateTasksOperationSettings()
    
    
    public OperationCallSettings<BatchCreateTasksRequest,BatchCreateTasksResponse,BatchCreateTasksMetadata> batchCreateTasksOperationSettings()

Returns the object with the settings used for calls to batchCreateTasks.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[BatchCreateTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksRequest),[BatchCreateTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksResponse),[BatchCreateTasksMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksMetadata)>` |   
  
### batchCreateTasksSettings()
    
    
    public UnaryCallSettings<BatchCreateTasksRequest,Operation> batchCreateTasksSettings()

Returns the object with the settings used for calls to batchCreateTasks.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchCreateTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchCreateTasksRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchDeleteTasksOperationSettings()
    
    
    public OperationCallSettings<BatchDeleteTasksRequest,Empty,BatchDeleteTasksMetadata> batchDeleteTasksOperationSettings()

Returns the object with the settings used for calls to batchDeleteTasks.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[BatchDeleteTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchDeleteTasksRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[BatchDeleteTasksMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchDeleteTasksMetadata)>` |   
  
### batchDeleteTasksSettings()
    
    
    public UnaryCallSettings<BatchDeleteTasksRequest,Operation> batchDeleteTasksSettings()

Returns the object with the settings used for calls to batchDeleteTasks.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchDeleteTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.BatchDeleteTasksRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createQueueSettings()
    
    
    public UnaryCallSettings<CreateQueueRequest,Queue> createQueueSettings()

Returns the object with the settings used for calls to createQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CreateQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
### createStub()
    
    
    public CloudTasksStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudTasksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### createTaskSettings()
    
    
    public UnaryCallSettings<CreateTaskRequest,Task> createTaskSettings()

Returns the object with the settings used for calls to createTask.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CreateTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task)>` |   
  
### deleteQueueSettings()
    
    
    public UnaryCallSettings<DeleteQueueRequest,Empty> deleteQueueSettings()

Returns the object with the settings used for calls to deleteQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.DeleteQueueRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTaskSettings()
    
    
    public UnaryCallSettings<DeleteTaskRequest,Empty> deleteTaskSettings()

Returns the object with the settings used for calls to deleteTask.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.DeleteTaskRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCmekConfigSettings()
    
    
    public UnaryCallSettings<GetCmekConfigRequest,CmekConfig> getCmekConfigSettings()

Returns the object with the settings used for calls to getCmekConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.GetCmekConfigRequest),[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CmekConfig)>` |   
  
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
  
### getQueueSettings()
    
    
    public UnaryCallSettings<GetQueueRequest,Queue> getQueueSettings()

Returns the object with the settings used for calls to getQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.GetQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getTaskSettings()
    
    
    public UnaryCallSettings<GetTaskRequest,Task> getTaskSettings()

Returns the object with the settings used for calls to getTask.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.GetTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,CloudTasksClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.ListLocationsPagedResponse)>` |   
  
### listQueuesSettings()
    
    
    public PagedCallSettings<ListQueuesRequest,ListQueuesResponse,CloudTasksClient.ListQueuesPagedResponse> listQueuesSettings()

Returns the object with the settings used for calls to listQueues.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListQueuesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.ListQueuesRequest),[ListQueuesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.ListQueuesResponse),[ListQueuesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.ListQueuesPagedResponse)>` |   
  
### listTasksSettings()
    
    
    public PagedCallSettings<ListTasksRequest,ListTasksResponse,CloudTasksClient.ListTasksPagedResponse> listTasksSettings()

Returns the object with the settings used for calls to listTasks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.ListTasksRequest),[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.ListTasksResponse),[ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CloudTasksClient.ListTasksPagedResponse)>` |   
  
### pauseQueueSettings()
    
    
    public UnaryCallSettings<PauseQueueRequest,Queue> pauseQueueSettings()

Returns the object with the settings used for calls to pauseQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PauseQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.PauseQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
### purgeQueueSettings()
    
    
    public UnaryCallSettings<PurgeQueueRequest,Queue> purgeQueueSettings()

Returns the object with the settings used for calls to purgeQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PurgeQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.PurgeQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
### resumeQueueSettings()
    
    
    public UnaryCallSettings<ResumeQueueRequest,Queue> resumeQueueSettings()

Returns the object with the settings used for calls to resumeQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResumeQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.ResumeQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
### runTaskSettings()
    
    
    public UnaryCallSettings<RunTaskRequest,Task> runTaskSettings()

Returns the object with the settings used for calls to runTask.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RunTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RunTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Task)>` |   
  
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
    
    
    public CloudTasksStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[CloudTasksStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.stub.CloudTasksStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateCmekConfigSettings()
    
    
    public UnaryCallSettings<UpdateCmekConfigRequest,CmekConfig> updateCmekConfigSettings()

Returns the object with the settings used for calls to updateCmekConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCmekConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.UpdateCmekConfigRequest),[CmekConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.CmekConfig)>` |   
  
### updateQueueSettings()
    
    
    public UnaryCallSettings<UpdateQueueRequest,Queue> updateQueueSettings()

Returns the object with the settings used for calls to updateQueue.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateQueueRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.UpdateQueueRequest),[Queue](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.Queue)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
