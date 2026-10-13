---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings
title: Class NotebookServiceStubSettings (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:58.991515+00:00
---

# Class NotebookServiceStubSettings (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NotebookServiceStubSettings (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.3  1.0.6  0.6.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class NotebookServiceStubSettings extends StubSettings<NotebookServiceStubSettings>

Settings class to configure an instance of [NotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (notebooks.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getInstance:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NotebookServiceStubSettings.Builder notebookServiceSettingsBuilder =
         NotebookServiceStubSettings.newBuilder();
     notebookServiceSettingsBuilder
         .getInstanceSettings()
         .setRetrySettings(
             notebookServiceSettingsBuilder
                 .getInstanceSettings()
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
     NotebookServiceStubSettings notebookServiceSettings = notebookServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createInstance:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NotebookServiceStubSettings.Builder notebookServiceSettingsBuilder =
         NotebookServiceStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     notebookServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > NotebookServiceStubSettings

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
    
    
    public static NotebookServiceStubSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static NotebookServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings.Builder)` |   
  
## Constructors 

### NotebookServiceStubSettings(NotebookServiceStubSettings.Builder settingsBuilder)
    
    
    protected NotebookServiceStubSettings(NotebookServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[NotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings.Builder)`  
  
  
## Methods 

### createEnvironmentOperationSettings()
    
    
    public OperationCallSettings<CreateEnvironmentRequest,Environment,OperationMetadata> createEnvironmentOperationSettings()

Returns the object with the settings used for calls to createEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### createEnvironmentSettings()
    
    
    public UnaryCallSettings<CreateEnvironmentRequest,Operation> createEnvironmentSettings()

Returns the object with the settings used for calls to createEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationSettings()
    
    
    public OperationCallSettings<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationSettings()

Returns the object with the settings used for calls to createInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### createInstanceSettings()
    
    
    public UnaryCallSettings<CreateInstanceRequest,Operation> createInstanceSettings()

Returns the object with the settings used for calls to createInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public NotebookServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteEnvironmentOperationSettings()
    
    
    public OperationCallSettings<DeleteEnvironmentRequest,Empty,OperationMetadata> deleteEnvironmentOperationSettings()

Returns the object with the settings used for calls to deleteEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### deleteEnvironmentSettings()
    
    
    public UnaryCallSettings<DeleteEnvironmentRequest,Operation> deleteEnvironmentSettings()

Returns the object with the settings used for calls to deleteEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationSettings()
    
    
    public OperationCallSettings<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationSettings()

Returns the object with the settings used for calls to deleteInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### deleteInstanceSettings()
    
    
    public UnaryCallSettings<DeleteInstanceRequest,Operation> deleteInstanceSettings()

Returns the object with the settings used for calls to deleteInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getEnvironmentSettings()
    
    
    public UnaryCallSettings<GetEnvironmentRequest,Environment> getEnvironmentSettings()

Returns the object with the settings used for calls to getEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.GetEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Environment)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getInstanceSettings()
    
    
    public UnaryCallSettings<GetInstanceRequest,Instance> getInstanceSettings()

Returns the object with the settings used for calls to getInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance)>` |   
  
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
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### isInstanceUpgradeableSettings() (deprecated)
    
    
    public UnaryCallSettings<IsInstanceUpgradeableRequest,IsInstanceUpgradeableResponse> isInstanceUpgradeableSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to isInstanceUpgradeable.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[IsInstanceUpgradeableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableRequest),[IsInstanceUpgradeableResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.IsInstanceUpgradeableResponse)>` |   
  
### listEnvironmentsSettings()
    
    
    public PagedCallSettings<ListEnvironmentsRequest,ListEnvironmentsResponse,NotebookServiceClient.ListEnvironmentsPagedResponse> listEnvironmentsSettings()

Returns the object with the settings used for calls to listEnvironments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListEnvironmentsRequest),[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListEnvironmentsResponse),[ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.NotebookServiceClient.ListEnvironmentsPagedResponse)>` |   
  
### listInstancesSettings()
    
    
    public PagedCallSettings<ListInstancesRequest,ListInstancesResponse,NotebookServiceClient.ListInstancesPagedResponse> listInstancesSettings()

Returns the object with the settings used for calls to listInstances.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ListInstancesResponse),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.NotebookServiceClient.ListInstancesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,NotebookServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.NotebookServiceClient.ListLocationsPagedResponse)>` |   
  
### registerInstanceOperationSettings()
    
    
    public OperationCallSettings<RegisterInstanceRequest,Instance,OperationMetadata> registerInstanceOperationSettings()

Returns the object with the settings used for calls to registerInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RegisterInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.RegisterInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### registerInstanceSettings()
    
    
    public UnaryCallSettings<RegisterInstanceRequest,Operation> registerInstanceSettings()

Returns the object with the settings used for calls to registerInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RegisterInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.RegisterInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### reportInstanceInfoOperationSettings()
    
    
    public OperationCallSettings<ReportInstanceInfoRequest,Instance,OperationMetadata> reportInstanceInfoOperationSettings()

Returns the object with the settings used for calls to reportInstanceInfo.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReportInstanceInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### reportInstanceInfoSettings()
    
    
    public UnaryCallSettings<ReportInstanceInfoRequest,Operation> reportInstanceInfoSettings()

Returns the object with the settings used for calls to reportInstanceInfo.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReportInstanceInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ReportInstanceInfoRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### resetInstanceOperationSettings()
    
    
    public OperationCallSettings<ResetInstanceRequest,Instance,OperationMetadata> resetInstanceOperationSettings()

Returns the object with the settings used for calls to resetInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ResetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### resetInstanceSettings()
    
    
    public UnaryCallSettings<ResetInstanceRequest,Operation> resetInstanceSettings()

Returns the object with the settings used for calls to resetInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ResetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.ResetInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### setInstanceAcceleratorOperationSettings()
    
    
    public OperationCallSettings<SetInstanceAcceleratorRequest,Instance,OperationMetadata> setInstanceAcceleratorOperationSettings()

Returns the object with the settings used for calls to setInstanceAccelerator.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetInstanceAcceleratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### setInstanceAcceleratorSettings()
    
    
    public UnaryCallSettings<SetInstanceAcceleratorRequest,Operation> setInstanceAcceleratorSettings()

Returns the object with the settings used for calls to setInstanceAccelerator.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetInstanceAcceleratorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceAcceleratorRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setInstanceLabelsOperationSettings()
    
    
    public OperationCallSettings<SetInstanceLabelsRequest,Instance,OperationMetadata> setInstanceLabelsOperationSettings()

Returns the object with the settings used for calls to setInstanceLabels.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetInstanceLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### setInstanceLabelsSettings()
    
    
    public UnaryCallSettings<SetInstanceLabelsRequest,Operation> setInstanceLabelsSettings()

Returns the object with the settings used for calls to setInstanceLabels.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetInstanceLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setInstanceMachineTypeOperationSettings()
    
    
    public OperationCallSettings<SetInstanceMachineTypeRequest,Instance,OperationMetadata> setInstanceMachineTypeOperationSettings()

Returns the object with the settings used for calls to setInstanceMachineType.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### setInstanceMachineTypeSettings()
    
    
    public UnaryCallSettings<SetInstanceMachineTypeRequest,Operation> setInstanceMachineTypeSettings()

Returns the object with the settings used for calls to setInstanceMachineType.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.SetInstanceMachineTypeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startInstanceOperationSettings()
    
    
    public OperationCallSettings<StartInstanceRequest,Instance,OperationMetadata> startInstanceOperationSettings()

Returns the object with the settings used for calls to startInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StartInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### startInstanceSettings()
    
    
    public UnaryCallSettings<StartInstanceRequest,Operation> startInstanceSettings()

Returns the object with the settings used for calls to startInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopInstanceOperationSettings()
    
    
    public OperationCallSettings<StopInstanceRequest,Instance,OperationMetadata> stopInstanceOperationSettings()

Returns the object with the settings used for calls to stopInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StopInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### stopInstanceSettings()
    
    
    public UnaryCallSettings<StopInstanceRequest,Operation> stopInstanceSettings()

Returns the object with the settings used for calls to stopInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.StopInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public NotebookServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.stub.NotebookServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### upgradeInstanceInternalOperationSettings()
    
    
    public OperationCallSettings<UpgradeInstanceInternalRequest,Instance,OperationMetadata> upgradeInstanceInternalOperationSettings()

Returns the object with the settings used for calls to upgradeInstanceInternal.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpgradeInstanceInternalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### upgradeInstanceInternalSettings() (deprecated)
    
    
    public UnaryCallSettings<UpgradeInstanceInternalRequest,Operation> upgradeInstanceInternalSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to upgradeInstanceInternal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpgradeInstanceInternalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceInternalRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### upgradeInstanceOperationSettings()
    
    
    public OperationCallSettings<UpgradeInstanceRequest,Instance,OperationMetadata> upgradeInstanceOperationSettings()

Returns the object with the settings used for calls to upgradeInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.OperationMetadata)>` |   
  
### upgradeInstanceSettings() (deprecated)
    
    
    public UnaryCallSettings<UpgradeInstanceRequest,Operation> upgradeInstanceSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to upgradeInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpgradeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-notebooks/latest/com.google.cloud.notebooks.v1beta1.UpgradeInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
