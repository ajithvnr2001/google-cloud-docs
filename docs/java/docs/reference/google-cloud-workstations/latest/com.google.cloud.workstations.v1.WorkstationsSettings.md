---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings
title: Class WorkstationsSettings (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:44.819006+00:00
---

# Class WorkstationsSettings (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkstationsSettings (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.0  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class WorkstationsSettings extends ClientSettings<WorkstationsSettings>

Settings class to configure an instance of [WorkstationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1beta.WorkstationsClient).

The default instance has everything set to sensible defaults:

  * The default service address (workstations.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getWorkstationCluster:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WorkstationsSettings.Builder workstationsSettingsBuilder = WorkstationsSettings.newBuilder();
     workstationsSettingsBuilder
         .getWorkstationClusterSettings()
         .setRetrySettings(
             workstationsSettingsBuilder
                 .getWorkstationClusterSettings()
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
     WorkstationsSettings workstationsSettings = workstationsSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createWorkstationCluster:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WorkstationsSettings.Builder workstationsSettingsBuilder = WorkstationsSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     workstationsSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > WorkstationsSettings

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

### create(WorkstationsStubSettings stub)
    
    
    public static final WorkstationsSettings create(WorkstationsStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[WorkstationsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.stub.WorkstationsStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings)` |   
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
    
    
    public static WorkstationsSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[WorkstationsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static WorkstationsSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkstationsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static WorkstationsSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[WorkstationsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings.Builder)` |   
  
## Constructors 

### WorkstationsSettings(WorkstationsSettings.Builder settingsBuilder)
    
    
    protected WorkstationsSettings(WorkstationsSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[WorkstationsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings.Builder)`  
  
  
## Methods 

### createWorkstationClusterOperationSettings()
    
    
    public OperationCallSettings<CreateWorkstationClusterRequest,WorkstationCluster,OperationMetadata> createWorkstationClusterOperationSettings()

Returns the object with the settings used for calls to createWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationClusterRequest),[WorkstationCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### createWorkstationClusterSettings()
    
    
    public UnaryCallSettings<CreateWorkstationClusterRequest,Operation> createWorkstationClusterSettings()

Returns the object with the settings used for calls to createWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWorkstationConfigOperationSettings()
    
    
    public OperationCallSettings<CreateWorkstationConfigRequest,WorkstationConfig,OperationMetadata> createWorkstationConfigOperationSettings()

Returns the object with the settings used for calls to createWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationConfigRequest),[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### createWorkstationConfigSettings()
    
    
    public UnaryCallSettings<CreateWorkstationConfigRequest,Operation> createWorkstationConfigSettings()

Returns the object with the settings used for calls to createWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWorkstationOperationSettings()
    
    
    public OperationCallSettings<CreateWorkstationRequest,Workstation,OperationMetadata> createWorkstationOperationSettings()

Returns the object with the settings used for calls to createWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### createWorkstationSettings()
    
    
    public UnaryCallSettings<CreateWorkstationRequest,Operation> createWorkstationSettings()

Returns the object with the settings used for calls to createWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.CreateWorkstationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWorkstationClusterOperationSettings()
    
    
    public OperationCallSettings<DeleteWorkstationClusterRequest,WorkstationCluster,OperationMetadata> deleteWorkstationClusterOperationSettings()

Returns the object with the settings used for calls to deleteWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationClusterRequest),[WorkstationCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### deleteWorkstationClusterSettings()
    
    
    public UnaryCallSettings<DeleteWorkstationClusterRequest,Operation> deleteWorkstationClusterSettings()

Returns the object with the settings used for calls to deleteWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWorkstationConfigOperationSettings()
    
    
    public OperationCallSettings<DeleteWorkstationConfigRequest,WorkstationConfig,OperationMetadata> deleteWorkstationConfigOperationSettings()

Returns the object with the settings used for calls to deleteWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationConfigRequest),[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### deleteWorkstationConfigSettings()
    
    
    public UnaryCallSettings<DeleteWorkstationConfigRequest,Operation> deleteWorkstationConfigSettings()

Returns the object with the settings used for calls to deleteWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWorkstationOperationSettings()
    
    
    public OperationCallSettings<DeleteWorkstationRequest,Workstation,OperationMetadata> deleteWorkstationOperationSettings()

Returns the object with the settings used for calls to deleteWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### deleteWorkstationSettings()
    
    
    public UnaryCallSettings<DeleteWorkstationRequest,Operation> deleteWorkstationSettings()

Returns the object with the settings used for calls to deleteWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.DeleteWorkstationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateAccessTokenSettings()
    
    
    public UnaryCallSettings<GenerateAccessTokenRequest,GenerateAccessTokenResponse> generateAccessTokenSettings()

Returns the object with the settings used for calls to generateAccessToken.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GenerateAccessTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.GenerateAccessTokenRequest),[GenerateAccessTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.GenerateAccessTokenResponse)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getWorkstationClusterSettings()
    
    
    public UnaryCallSettings<GetWorkstationClusterRequest,WorkstationCluster> getWorkstationClusterSettings()

Returns the object with the settings used for calls to getWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.GetWorkstationClusterRequest),[WorkstationCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationCluster)>` |   
  
### getWorkstationConfigSettings()
    
    
    public UnaryCallSettings<GetWorkstationConfigRequest,WorkstationConfig> getWorkstationConfigSettings()

Returns the object with the settings used for calls to getWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.GetWorkstationConfigRequest),[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig)>` |   
  
### getWorkstationSettings()
    
    
    public UnaryCallSettings<GetWorkstationRequest,Workstation> getWorkstationSettings()

Returns the object with the settings used for calls to getWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.GetWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation)>` |   
  
### listUsableWorkstationConfigsSettings()
    
    
    public PagedCallSettings<ListUsableWorkstationConfigsRequest,ListUsableWorkstationConfigsResponse,WorkstationsClient.ListUsableWorkstationConfigsPagedResponse> listUsableWorkstationConfigsSettings()

Returns the object with the settings used for calls to listUsableWorkstationConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUsableWorkstationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListUsableWorkstationConfigsRequest),[ListUsableWorkstationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListUsableWorkstationConfigsResponse),[ListUsableWorkstationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsClient.ListUsableWorkstationConfigsPagedResponse)>` |   
  
### listUsableWorkstationsSettings()
    
    
    public PagedCallSettings<ListUsableWorkstationsRequest,ListUsableWorkstationsResponse,WorkstationsClient.ListUsableWorkstationsPagedResponse> listUsableWorkstationsSettings()

Returns the object with the settings used for calls to listUsableWorkstations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUsableWorkstationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListUsableWorkstationsRequest),[ListUsableWorkstationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListUsableWorkstationsResponse),[ListUsableWorkstationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsClient.ListUsableWorkstationsPagedResponse)>` |   
  
### listWorkstationClustersSettings()
    
    
    public PagedCallSettings<ListWorkstationClustersRequest,ListWorkstationClustersResponse,WorkstationsClient.ListWorkstationClustersPagedResponse> listWorkstationClustersSettings()

Returns the object with the settings used for calls to listWorkstationClusters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkstationClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationClustersRequest),[ListWorkstationClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationClustersResponse),[ListWorkstationClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsClient.ListWorkstationClustersPagedResponse)>` |   
  
### listWorkstationConfigsSettings()
    
    
    public PagedCallSettings<ListWorkstationConfigsRequest,ListWorkstationConfigsResponse,WorkstationsClient.ListWorkstationConfigsPagedResponse> listWorkstationConfigsSettings()

Returns the object with the settings used for calls to listWorkstationConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkstationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationConfigsRequest),[ListWorkstationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationConfigsResponse),[ListWorkstationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsClient.ListWorkstationConfigsPagedResponse)>` |   
  
### listWorkstationsSettings()
    
    
    public PagedCallSettings<ListWorkstationsRequest,ListWorkstationsResponse,WorkstationsClient.ListWorkstationsPagedResponse> listWorkstationsSettings()

Returns the object with the settings used for calls to listWorkstations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkstationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationsRequest),[ListWorkstationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.ListWorkstationsResponse),[ListWorkstationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsClient.ListWorkstationsPagedResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### startWorkstationOperationSettings()
    
    
    public OperationCallSettings<StartWorkstationRequest,Workstation,OperationMetadata> startWorkstationOperationSettings()

Returns the object with the settings used for calls to startWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.StartWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### startWorkstationSettings()
    
    
    public UnaryCallSettings<StartWorkstationRequest,Operation> startWorkstationSettings()

Returns the object with the settings used for calls to startWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.StartWorkstationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopWorkstationOperationSettings()
    
    
    public OperationCallSettings<StopWorkstationRequest,Workstation,OperationMetadata> stopWorkstationOperationSettings()

Returns the object with the settings used for calls to stopWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.StopWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### stopWorkstationSettings()
    
    
    public UnaryCallSettings<StopWorkstationRequest,Operation> stopWorkstationSettings()

Returns the object with the settings used for calls to stopWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.StopWorkstationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public WorkstationsSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[WorkstationsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationsSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateWorkstationClusterOperationSettings()
    
    
    public OperationCallSettings<UpdateWorkstationClusterRequest,WorkstationCluster,OperationMetadata> updateWorkstationClusterOperationSettings()

Returns the object with the settings used for calls to updateWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationClusterRequest),[WorkstationCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### updateWorkstationClusterSettings()
    
    
    public UnaryCallSettings<UpdateWorkstationClusterRequest,Operation> updateWorkstationClusterSettings()

Returns the object with the settings used for calls to updateWorkstationCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateWorkstationClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWorkstationConfigOperationSettings()
    
    
    public OperationCallSettings<UpdateWorkstationConfigRequest,WorkstationConfig,OperationMetadata> updateWorkstationConfigOperationSettings()

Returns the object with the settings used for calls to updateWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationConfigRequest),[WorkstationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.WorkstationConfig),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### updateWorkstationConfigSettings()
    
    
    public UnaryCallSettings<UpdateWorkstationConfigRequest,Operation> updateWorkstationConfigSettings()

Returns the object with the settings used for calls to updateWorkstationConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateWorkstationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWorkstationOperationSettings()
    
    
    public OperationCallSettings<UpdateWorkstationRequest,Workstation,OperationMetadata> updateWorkstationOperationSettings()

Returns the object with the settings used for calls to updateWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationRequest),[Workstation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.Workstation),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.OperationMetadata)>` |   
  
### updateWorkstationSettings()
    
    
    public UnaryCallSettings<UpdateWorkstationRequest,Operation> updateWorkstationSettings()

Returns the object with the settings used for calls to updateWorkstation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateWorkstationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workstations/latest/com.google.cloud.workstations.v1.UpdateWorkstationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
