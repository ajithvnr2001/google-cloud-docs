---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings
title: Class LineageStubSettings (0.91.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:35.974981+00:00
---

# Class LineageStubSettings (0.91.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LineageStubSettings (0.91.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.91.0 (latest)  0.87.0  0.86.0  0.85.0  0.83.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public class LineageStubSettings extends StubSettings<LineageStubSettings>

Settings class to configure an instance of [LineageStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStub).

The default instance has everything set to sensible defaults:

  * The default service address (datalineage.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of processOpenLineageRunEvent:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LineageStubSettings.Builder lineageSettingsBuilder = LineageStubSettings.newBuilder();
     lineageSettingsBuilder
         .processOpenLineageRunEventSettings()
         .setRetrySettings(
             lineageSettingsBuilder
                 .processOpenLineageRunEventSettings()
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
     LineageStubSettings lineageSettings = lineageSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for deleteProcess:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     LineageStubSettings.Builder lineageSettingsBuilder = LineageStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     lineageSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > LineageStubSettings

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
    
    
    public static LineageStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LineageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static LineageStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[LineageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static LineageStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[LineageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings.Builder)` |   
  
## Constructors 

### LineageStubSettings(LineageStubSettings.Builder settingsBuilder)
    
    
    protected LineageStubSettings(LineageStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[LineageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings.Builder)`  
  
  
## Methods 

### batchSearchLinkProcessesSettings()
    
    
    public PagedCallSettings<BatchSearchLinkProcessesRequest,BatchSearchLinkProcessesResponse,LineageClient.BatchSearchLinkProcessesPagedResponse> batchSearchLinkProcessesSettings()

Returns the object with the settings used for calls to batchSearchLinkProcesses.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.BatchSearchLinkProcessesRequest),[BatchSearchLinkProcessesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.BatchSearchLinkProcessesResponse),[BatchSearchLinkProcessesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.BatchSearchLinkProcessesPagedResponse)>` |   
  
### createLineageEventSettings()
    
    
    public UnaryCallSettings<CreateLineageEventRequest,LineageEvent> createLineageEventSettings()

Returns the object with the settings used for calls to createLineageEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateLineageEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.CreateLineageEventRequest),[LineageEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageEvent)>` |   
  
### createProcessSettings()
    
    
    public UnaryCallSettings<CreateProcessRequest,Process> createProcessSettings()

Returns the object with the settings used for calls to createProcess.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.CreateProcessRequest),[Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Process)>` |   
  
### createRunSettings()
    
    
    public UnaryCallSettings<CreateRunRequest,Run> createRunSettings()

Returns the object with the settings used for calls to createRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.CreateRunRequest),[Run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Run)>` |   
  
### createStub()
    
    
    public LineageStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[LineageStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteLineageEventSettings()
    
    
    public UnaryCallSettings<DeleteLineageEventRequest,Empty> deleteLineageEventSettings()

Returns the object with the settings used for calls to deleteLineageEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteLineageEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.DeleteLineageEventRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteProcessOperationSettings()
    
    
    public OperationCallSettings<DeleteProcessRequest,Empty,OperationMetadata> deleteProcessOperationSettings()

Returns the object with the settings used for calls to deleteProcess.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.DeleteProcessRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.OperationMetadata)>` |   
  
### deleteProcessSettings()
    
    
    public UnaryCallSettings<DeleteProcessRequest,Operation> deleteProcessSettings()

Returns the object with the settings used for calls to deleteProcess.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.DeleteProcessRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRunOperationSettings()
    
    
    public OperationCallSettings<DeleteRunRequest,Empty,OperationMetadata> deleteRunOperationSettings()

Returns the object with the settings used for calls to deleteRun.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.DeleteRunRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.OperationMetadata)>` |   
  
### deleteRunSettings()
    
    
    public UnaryCallSettings<DeleteRunRequest,Operation> deleteRunSettings()

Returns the object with the settings used for calls to deleteRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.DeleteRunRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getLineageEventSettings()
    
    
    public UnaryCallSettings<GetLineageEventRequest,LineageEvent> getLineageEventSettings()

Returns the object with the settings used for calls to getLineageEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetLineageEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.GetLineageEventRequest),[LineageEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageEvent)>` |   
  
### getProcessSettings()
    
    
    public UnaryCallSettings<GetProcessRequest,Process> getProcessSettings()

Returns the object with the settings used for calls to getProcess.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.GetProcessRequest),[Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Process)>` |   
  
### getRunSettings()
    
    
    public UnaryCallSettings<GetRunRequest,Run> getRunSettings()

Returns the object with the settings used for calls to getRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.GetRunRequest),[Run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Run)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listLineageEventsSettings()
    
    
    public PagedCallSettings<ListLineageEventsRequest,ListLineageEventsResponse,LineageClient.ListLineageEventsPagedResponse> listLineageEventsSettings()

Returns the object with the settings used for calls to listLineageEvents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListLineageEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListLineageEventsRequest),[ListLineageEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListLineageEventsResponse),[ListLineageEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.ListLineageEventsPagedResponse)>` |   
  
### listProcessesSettings()
    
    
    public PagedCallSettings<ListProcessesRequest,ListProcessesResponse,LineageClient.ListProcessesPagedResponse> listProcessesSettings()

Returns the object with the settings used for calls to listProcesses.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListProcessesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListProcessesRequest),[ListProcessesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListProcessesResponse),[ListProcessesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.ListProcessesPagedResponse)>` |   
  
### listRunsSettings()
    
    
    public PagedCallSettings<ListRunsRequest,ListRunsResponse,LineageClient.ListRunsPagedResponse> listRunsSettings()

Returns the object with the settings used for calls to listRuns.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListRunsRequest),[ListRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ListRunsResponse),[ListRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.ListRunsPagedResponse)>` |   
  
### processOpenLineageRunEventSettings()
    
    
    public UnaryCallSettings<ProcessOpenLineageRunEventRequest,ProcessOpenLineageRunEventResponse> processOpenLineageRunEventSettings()

Returns the object with the settings used for calls to processOpenLineageRunEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessOpenLineageRunEventRequest),[ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.ProcessOpenLineageRunEventResponse)>` |   
  
### searchLineageStreamingSettings()
    
    
    public ServerStreamingCallSettings<SearchLineageStreamingRequest,SearchLineageStreamingResponse> searchLineageStreamingSettings()

Returns the object with the settings used for calls to searchLineageStreaming.

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings.html)<[SearchLineageStreamingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest),[SearchLineageStreamingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLineageStreamingResponse)>` |   
  
### searchLinksSettings()
    
    
    public PagedCallSettings<SearchLinksRequest,SearchLinksResponse,LineageClient.SearchLinksPagedResponse> searchLinksSettings()

Returns the object with the settings used for calls to searchLinks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLinksRequest),[SearchLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.SearchLinksResponse),[SearchLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.LineageClient.SearchLinksPagedResponse)>` |   
  
### toBuilder()
    
    
    public LineageStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[LineageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.stub.LineageStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateProcessSettings()
    
    
    public UnaryCallSettings<UpdateProcessRequest,Process> updateProcessSettings()

Returns the object with the settings used for calls to updateProcess.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateProcessRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.UpdateProcessRequest),[Process](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Process)>` |   
  
### updateRunSettings()
    
    
    public UnaryCallSettings<UpdateRunRequest,Run> updateRunSettings()

Returns the object with the settings used for calls to updateRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.UpdateRunRequest),[Run](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalineage/latest/com.google.cloud.datacatalog.lineage.v1.Run)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
