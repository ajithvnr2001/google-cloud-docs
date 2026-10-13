---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings
title: Class ManagedNotebookServiceStubSettings (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:27.630556+00:00
---

# Class ManagedNotebookServiceStubSettings (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ManagedNotebookServiceStubSettings (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.3  1.0.6  0.6.2 
    
    
    public class ManagedNotebookServiceStubSettings extends StubSettings<ManagedNotebookServiceStubSettings>

Settings class to configure an instance of [ManagedNotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (notebooks.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getRuntime:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ManagedNotebookServiceStubSettings.Builder managedNotebookServiceSettingsBuilder =
         ManagedNotebookServiceStubSettings.newBuilder();
     managedNotebookServiceSettingsBuilder
         .getRuntimeSettings()
         .setRetrySettings(
             managedNotebookServiceSettingsBuilder
                 .getRuntimeSettings()
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
     ManagedNotebookServiceStubSettings managedNotebookServiceSettings =
         managedNotebookServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createRuntime:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ManagedNotebookServiceStubSettings.Builder managedNotebookServiceSettingsBuilder =
         ManagedNotebookServiceStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     managedNotebookServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > ManagedNotebookServiceStubSettings

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
    
    
    public static ManagedNotebookServiceStubSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ManagedNotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static ManagedNotebookServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagedNotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings.Builder)` |   
  
## Constructors 

### ManagedNotebookServiceStubSettings(ManagedNotebookServiceStubSettings.Builder settingsBuilder)
    
    
    protected ManagedNotebookServiceStubSettings(ManagedNotebookServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[ManagedNotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings.Builder)`  
  
  
## Methods 

### createRuntimeOperationSettings()
    
    
    public OperationCallSettings<CreateRuntimeRequest,Runtime,OperationMetadata> createRuntimeOperationSettings()

Returns the object with the settings used for calls to createRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.CreateRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### createRuntimeSettings()
    
    
    public UnaryCallSettings<CreateRuntimeRequest,Operation> createRuntimeSettings()

Returns the object with the settings used for calls to createRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.CreateRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public ManagedNotebookServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[ManagedNotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteRuntimeOperationSettings()
    
    
    public OperationCallSettings<DeleteRuntimeRequest,Empty,OperationMetadata> deleteRuntimeOperationSettings()

Returns the object with the settings used for calls to deleteRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.DeleteRuntimeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### deleteRuntimeSettings()
    
    
    public UnaryCallSettings<DeleteRuntimeRequest,Operation> deleteRuntimeSettings()

Returns the object with the settings used for calls to deleteRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.DeleteRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### diagnoseRuntimeOperationSettings()
    
    
    public OperationCallSettings<DiagnoseRuntimeRequest,Runtime,OperationMetadata> diagnoseRuntimeOperationSettings()

Returns the object with the settings used for calls to diagnoseRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DiagnoseRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.DiagnoseRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### diagnoseRuntimeSettings()
    
    
    public UnaryCallSettings<DiagnoseRuntimeRequest,Operation> diagnoseRuntimeSettings()

Returns the object with the settings used for calls to diagnoseRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DiagnoseRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.DiagnoseRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
  
### getRuntimeSettings()
    
    
    public UnaryCallSettings<GetRuntimeRequest,Runtime> getRuntimeSettings()

Returns the object with the settings used for calls to getRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.GetRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,ManagedNotebookServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ManagedNotebookServiceClient.ListLocationsPagedResponse)>` |   
  
### listRuntimesSettings()
    
    
    public PagedCallSettings<ListRuntimesRequest,ListRuntimesResponse,ManagedNotebookServiceClient.ListRuntimesPagedResponse> listRuntimesSettings()

Returns the object with the settings used for calls to listRuntimes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRuntimesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ListRuntimesRequest),[ListRuntimesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ListRuntimesResponse),[ListRuntimesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ManagedNotebookServiceClient.ListRuntimesPagedResponse)>` |   
  
### refreshRuntimeTokenInternalSettings()
    
    
    public UnaryCallSettings<RefreshRuntimeTokenInternalRequest,RefreshRuntimeTokenInternalResponse> refreshRuntimeTokenInternalSettings()

Returns the object with the settings used for calls to refreshRuntimeTokenInternal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.RefreshRuntimeTokenInternalRequest),[RefreshRuntimeTokenInternalResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.RefreshRuntimeTokenInternalResponse)>` |   
  
### reportRuntimeEventOperationSettings()
    
    
    public OperationCallSettings<ReportRuntimeEventRequest,Runtime,OperationMetadata> reportRuntimeEventOperationSettings()

Returns the object with the settings used for calls to reportRuntimeEvent.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReportRuntimeEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ReportRuntimeEventRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### reportRuntimeEventSettings()
    
    
    public UnaryCallSettings<ReportRuntimeEventRequest,Operation> reportRuntimeEventSettings()

Returns the object with the settings used for calls to reportRuntimeEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReportRuntimeEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ReportRuntimeEventRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetRuntimeOperationSettings()
    
    
    public OperationCallSettings<ResetRuntimeRequest,Runtime,OperationMetadata> resetRuntimeOperationSettings()

Returns the object with the settings used for calls to resetRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResetRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ResetRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### resetRuntimeSettings()
    
    
    public UnaryCallSettings<ResetRuntimeRequest,Operation> resetRuntimeSettings()

Returns the object with the settings used for calls to resetRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.ResetRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### startRuntimeOperationSettings()
    
    
    public OperationCallSettings<StartRuntimeRequest,Runtime,OperationMetadata> startRuntimeOperationSettings()

Returns the object with the settings used for calls to startRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.StartRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### startRuntimeSettings()
    
    
    public UnaryCallSettings<StartRuntimeRequest,Operation> startRuntimeSettings()

Returns the object with the settings used for calls to startRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.StartRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopRuntimeOperationSettings()
    
    
    public OperationCallSettings<StopRuntimeRequest,Runtime,OperationMetadata> stopRuntimeOperationSettings()

Returns the object with the settings used for calls to stopRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.StopRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### stopRuntimeSettings()
    
    
    public UnaryCallSettings<StopRuntimeRequest,Operation> stopRuntimeSettings()

Returns the object with the settings used for calls to stopRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.StopRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### switchRuntimeOperationSettings()
    
    
    public OperationCallSettings<SwitchRuntimeRequest,Runtime,OperationMetadata> switchRuntimeOperationSettings()

Returns the object with the settings used for calls to switchRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SwitchRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.SwitchRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### switchRuntimeSettings()
    
    
    public UnaryCallSettings<SwitchRuntimeRequest,Operation> switchRuntimeSettings()

Returns the object with the settings used for calls to switchRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SwitchRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.SwitchRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public ManagedNotebookServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[ManagedNotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.stub.ManagedNotebookServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateRuntimeOperationSettings()
    
    
    public OperationCallSettings<UpdateRuntimeRequest,Runtime,OperationMetadata> updateRuntimeOperationSettings()

Returns the object with the settings used for calls to updateRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.UpdateRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### updateRuntimeSettings()
    
    
    public UnaryCallSettings<UpdateRuntimeRequest,Operation> updateRuntimeSettings()

Returns the object with the settings used for calls to updateRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.UpdateRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### upgradeRuntimeOperationSettings()
    
    
    public OperationCallSettings<UpgradeRuntimeRequest,Runtime,OperationMetadata> upgradeRuntimeOperationSettings()

Returns the object with the settings used for calls to upgradeRuntime.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpgradeRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.UpgradeRuntimeRequest),[Runtime](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.Runtime),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.OperationMetadata)>` |   
  
### upgradeRuntimeSettings()
    
    
    public UnaryCallSettings<UpgradeRuntimeRequest,Operation> upgradeRuntimeSettings()

Returns the object with the settings used for calls to upgradeRuntime.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpgradeRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1.UpgradeRuntimeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
