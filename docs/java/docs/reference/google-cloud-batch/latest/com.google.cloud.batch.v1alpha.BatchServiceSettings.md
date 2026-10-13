---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings
title: Class BatchServiceSettings (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:21.780886+00:00
---

# Class BatchServiceSettings (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BatchServiceSettings (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class BatchServiceSettings extends ClientSettings<BatchServiceSettings>

Settings class to configure an instance of [BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (batch.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createJob:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BatchServiceSettings.Builder batchServiceSettingsBuilder = BatchServiceSettings.newBuilder();
     batchServiceSettingsBuilder
         .createJobSettings()
         .setRetrySettings(
             batchServiceSettingsBuilder
                 .createJobSettings()
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
     BatchServiceSettings batchServiceSettings = batchServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for deleteJob:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BatchServiceSettings.Builder batchServiceSettingsBuilder = BatchServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     batchServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > BatchServiceSettings

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

### create(BatchServiceStubSettings stub)
    
    
    public static final BatchServiceSettings create(BatchServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BatchServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.stub.BatchServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings)` |   
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
    
    
    public static BatchServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[BatchServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static BatchServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static BatchServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[BatchServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder)` |   
  
## Constructors 

### BatchServiceSettings(BatchServiceSettings.Builder settingsBuilder)
    
    
    protected BatchServiceSettings(BatchServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[BatchServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder)`  
  
  
## Methods 

### cancelJobOperationSettings()
    
    
    public OperationCallSettings<CancelJobRequest,CancelJobResponse,OperationMetadata> cancelJobOperationSettings()

Returns the object with the settings used for calls to cancelJob.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest),[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### cancelJobSettings()
    
    
    public UnaryCallSettings<CancelJobRequest,Operation> cancelJobSettings()

Returns the object with the settings used for calls to cancelJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createJobSettings()
    
    
    public UnaryCallSettings<CreateJobRequest,Job> createJobSettings()

Returns the object with the settings used for calls to createJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### createResourceAllowanceSettings()
    
    
    public UnaryCallSettings<CreateResourceAllowanceRequest,ResourceAllowance> createResourceAllowanceSettings()

Returns the object with the settings used for calls to createResourceAllowance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
### deleteJobOperationSettings()
    
    
    public OperationCallSettings<DeleteJobRequest,Empty,OperationMetadata> deleteJobOperationSettings()

Returns the object with the settings used for calls to deleteJob.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteJobSettings()
    
    
    public UnaryCallSettings<DeleteJobRequest,Operation> deleteJobSettings()

Returns the object with the settings used for calls to deleteJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteResourceAllowanceOperationSettings()
    
    
    public OperationCallSettings<DeleteResourceAllowanceRequest,Empty,OperationMetadata> deleteResourceAllowanceOperationSettings()

Returns the object with the settings used for calls to deleteResourceAllowance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteResourceAllowanceSettings()
    
    
    public UnaryCallSettings<DeleteResourceAllowanceRequest,Operation> deleteResourceAllowanceSettings()

Returns the object with the settings used for calls to deleteResourceAllowance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getJobSettings()
    
    
    public UnaryCallSettings<GetJobRequest,Job> getJobSettings()

Returns the object with the settings used for calls to getJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getResourceAllowanceSettings()
    
    
    public UnaryCallSettings<GetResourceAllowanceRequest,ResourceAllowance> getResourceAllowanceSettings()

Returns the object with the settings used for calls to getResourceAllowance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
### getTaskSettings()
    
    
    public UnaryCallSettings<GetTaskRequest,Task> getTaskSettings()

Returns the object with the settings used for calls to getTask.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task)>` |   
  
### listJobsSettings()
    
    
    public PagedCallSettings<ListJobsRequest,ListJobsResponse,BatchServiceClient.ListJobsPagedResponse> listJobsSettings()

Returns the object with the settings used for calls to listJobs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest),[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsResponse),[ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,BatchServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPagedResponse)>` |   
  
### listResourceAllowancesSettings()
    
    
    public PagedCallSettings<ListResourceAllowancesRequest,ListResourceAllowancesResponse,BatchServiceClient.ListResourceAllowancesPagedResponse> listResourceAllowancesSettings()

Returns the object with the settings used for calls to listResourceAllowances.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListResourceAllowancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest),[ListResourceAllowancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse),[ListResourceAllowancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse)>` |   
  
### listTasksSettings()
    
    
    public PagedCallSettings<ListTasksRequest,ListTasksResponse,BatchServiceClient.ListTasksPagedResponse> listTasksSettings()

Returns the object with the settings used for calls to listTasks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest),[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksResponse),[ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse)>` |   
  
### toBuilder()
    
    
    public BatchServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[BatchServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateJobSettings()
    
    
    public UnaryCallSettings<UpdateJobRequest,Job> updateJobSettings()

Returns the object with the settings used for calls to updateJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### updateResourceAllowanceSettings()
    
    
    public UnaryCallSettings<UpdateResourceAllowanceRequest,ResourceAllowance> updateResourceAllowanceSettings()

Returns the object with the settings used for calls to updateResourceAllowance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
