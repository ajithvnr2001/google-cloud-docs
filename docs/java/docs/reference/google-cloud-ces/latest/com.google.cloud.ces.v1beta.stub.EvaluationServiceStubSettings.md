---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings
title: Class EvaluationServiceStubSettings (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:43.512688+00:00
---

# Class EvaluationServiceStubSettings (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EvaluationServiceStubSettings (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class EvaluationServiceStubSettings extends StubSettings<EvaluationServiceStubSettings>

Settings class to configure an instance of [EvaluationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (ces.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of uploadEvaluationAudio:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EvaluationServiceStubSettings.Builder evaluationServiceSettingsBuilder =
         EvaluationServiceStubSettings.newBuilder();
     evaluationServiceSettingsBuilder
         .uploadEvaluationAudioSettings()
         .setRetrySettings(
             evaluationServiceSettingsBuilder
                 .uploadEvaluationAudioSettings()
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
     EvaluationServiceStubSettings evaluationServiceSettings =
         evaluationServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for runEvaluation:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EvaluationServiceStubSettings.Builder evaluationServiceSettingsBuilder =
         EvaluationServiceStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     evaluationServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > EvaluationServiceStubSettings

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
    
    
    public static EvaluationServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EvaluationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static EvaluationServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[EvaluationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static EvaluationServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EvaluationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings.Builder)` |   
  
## Constructors 

### EvaluationServiceStubSettings(EvaluationServiceStubSettings.Builder settingsBuilder)
    
    
    protected EvaluationServiceStubSettings(EvaluationServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[EvaluationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings.Builder)`  
  
  
## Methods 

### createEvaluationDatasetSettings()
    
    
    public UnaryCallSettings<CreateEvaluationDatasetRequest,EvaluationDataset> createEvaluationDatasetSettings()

Returns the object with the settings used for calls to createEvaluationDataset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEvaluationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateEvaluationDatasetRequest),[EvaluationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationDataset)>` |   
  
### createEvaluationExpectationSettings()
    
    
    public UnaryCallSettings<CreateEvaluationExpectationRequest,EvaluationExpectation> createEvaluationExpectationSettings()

Returns the object with the settings used for calls to createEvaluationExpectation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEvaluationExpectationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateEvaluationExpectationRequest),[EvaluationExpectation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationExpectation)>` |   
  
### createEvaluationSettings()
    
    
    public UnaryCallSettings<CreateEvaluationRequest,Evaluation> createEvaluationSettings()

Returns the object with the settings used for calls to createEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateEvaluationRequest),[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Evaluation)>` |   
  
### createScheduledEvaluationRunSettings()
    
    
    public UnaryCallSettings<CreateScheduledEvaluationRunRequest,ScheduledEvaluationRun> createScheduledEvaluationRunSettings()

Returns the object with the settings used for calls to createScheduledEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateScheduledEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.CreateScheduledEvaluationRunRequest),[ScheduledEvaluationRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ScheduledEvaluationRun)>` |   
  
### createStub()
    
    
    public EvaluationServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[EvaluationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteEvaluationDatasetSettings()
    
    
    public UnaryCallSettings<DeleteEvaluationDatasetRequest,Empty> deleteEvaluationDatasetSettings()

Returns the object with the settings used for calls to deleteEvaluationDataset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEvaluationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationDatasetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteEvaluationExpectationSettings()
    
    
    public UnaryCallSettings<DeleteEvaluationExpectationRequest,Empty> deleteEvaluationExpectationSettings()

Returns the object with the settings used for calls to deleteEvaluationExpectation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEvaluationExpectationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationExpectationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteEvaluationResultSettings()
    
    
    public UnaryCallSettings<DeleteEvaluationResultRequest,Empty> deleteEvaluationResultSettings()

Returns the object with the settings used for calls to deleteEvaluationResult.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEvaluationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationResultRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteEvaluationRunOperationSettings()
    
    
    public OperationCallSettings<DeleteEvaluationRunRequest,Empty,DeleteEvaluationRunOperationMetadata> deleteEvaluationRunOperationSettings()

Returns the object with the settings used for calls to deleteEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationRunRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteEvaluationRunOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationRunOperationMetadata)>` |   
  
### deleteEvaluationRunSettings()
    
    
    public UnaryCallSettings<DeleteEvaluationRunRequest,Operation> deleteEvaluationRunSettings()

Returns the object with the settings used for calls to deleteEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationRunRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEvaluationSettings()
    
    
    public UnaryCallSettings<DeleteEvaluationRequest,Empty> deleteEvaluationSettings()

Returns the object with the settings used for calls to deleteEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteEvaluationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteScheduledEvaluationRunSettings()
    
    
    public UnaryCallSettings<DeleteScheduledEvaluationRunRequest,Empty> deleteScheduledEvaluationRunSettings()

Returns the object with the settings used for calls to deleteScheduledEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteScheduledEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.DeleteScheduledEvaluationRunRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### exportEvaluationResultsOperationSettings()
    
    
    public OperationCallSettings<ExportEvaluationResultsRequest,ExportEvaluationResultsResponse,ExportEvaluationResultsOperationMetadata> exportEvaluationResultsOperationSettings()

Returns the object with the settings used for calls to exportEvaluationResults.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExportEvaluationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationResultsRequest),[ExportEvaluationResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationResultsResponse),[ExportEvaluationResultsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationResultsOperationMetadata)>` |   
  
### exportEvaluationResultsSettings()
    
    
    public UnaryCallSettings<ExportEvaluationResultsRequest,Operation> exportEvaluationResultsSettings()

Returns the object with the settings used for calls to exportEvaluationResults.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExportEvaluationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationResultsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportEvaluationRunsOperationSettings()
    
    
    public OperationCallSettings<ExportEvaluationRunsRequest,ExportEvaluationRunsResponse,ExportEvaluationRunsOperationMetadata> exportEvaluationRunsOperationSettings()

Returns the object with the settings used for calls to exportEvaluationRuns.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExportEvaluationRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsRequest),[ExportEvaluationRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsResponse),[ExportEvaluationRunsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsOperationMetadata)>` |   
  
### exportEvaluationRunsSettings()
    
    
    public UnaryCallSettings<ExportEvaluationRunsRequest,Operation> exportEvaluationRunsSettings()

Returns the object with the settings used for calls to exportEvaluationRuns.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExportEvaluationRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationRunsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportEvaluationsOperationSettings()
    
    
    public OperationCallSettings<ExportEvaluationsRequest,ExportEvaluationsResponse,OperationMetadata> exportEvaluationsOperationSettings()

Returns the object with the settings used for calls to exportEvaluations.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExportEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationsRequest),[ExportEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.OperationMetadata)>` |   
  
### exportEvaluationsSettings()
    
    
    public UnaryCallSettings<ExportEvaluationsRequest,Operation> exportEvaluationsSettings()

Returns the object with the settings used for calls to exportEvaluations.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExportEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ExportEvaluationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateEvaluationOperationSettings()
    
    
    public OperationCallSettings<GenerateEvaluationRequest,Evaluation,GenerateEvaluationOperationMetadata> generateEvaluationOperationSettings()

Returns the object with the settings used for calls to generateEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[GenerateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateEvaluationRequest),[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Evaluation),[GenerateEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateEvaluationOperationMetadata)>` |   
  
### generateEvaluationSettings()
    
    
    public UnaryCallSettings<GenerateEvaluationRequest,Operation> generateEvaluationSettings()

Returns the object with the settings used for calls to generateEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GenerateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GenerateEvaluationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getEvaluationDatasetSettings()
    
    
    public UnaryCallSettings<GetEvaluationDatasetRequest,EvaluationDataset> getEvaluationDatasetSettings()

Returns the object with the settings used for calls to getEvaluationDataset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEvaluationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetEvaluationDatasetRequest),[EvaluationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationDataset)>` |   
  
### getEvaluationExpectationSettings()
    
    
    public UnaryCallSettings<GetEvaluationExpectationRequest,EvaluationExpectation> getEvaluationExpectationSettings()

Returns the object with the settings used for calls to getEvaluationExpectation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEvaluationExpectationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetEvaluationExpectationRequest),[EvaluationExpectation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationExpectation)>` |   
  
### getEvaluationResultSettings()
    
    
    public UnaryCallSettings<GetEvaluationResultRequest,EvaluationResult> getEvaluationResultSettings()

Returns the object with the settings used for calls to getEvaluationResult.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEvaluationResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetEvaluationResultRequest),[EvaluationResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationResult)>` |   
  
### getEvaluationRunSettings()
    
    
    public UnaryCallSettings<GetEvaluationRunRequest,EvaluationRun> getEvaluationRunSettings()

Returns the object with the settings used for calls to getEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetEvaluationRunRequest),[EvaluationRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationRun)>` |   
  
### getEvaluationSettings()
    
    
    public UnaryCallSettings<GetEvaluationRequest,Evaluation> getEvaluationSettings()

Returns the object with the settings used for calls to getEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetEvaluationRequest),[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Evaluation)>` |   
  
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
  
### getScheduledEvaluationRunSettings()
    
    
    public UnaryCallSettings<GetScheduledEvaluationRunRequest,ScheduledEvaluationRun> getScheduledEvaluationRunSettings()

Returns the object with the settings used for calls to getScheduledEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetScheduledEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.GetScheduledEvaluationRunRequest),[ScheduledEvaluationRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ScheduledEvaluationRun)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### importEvaluationsOperationSettings()
    
    
    public OperationCallSettings<ImportEvaluationsRequest,ImportEvaluationsResponse,ImportEvaluationsOperationMetadata> importEvaluationsOperationSettings()

Returns the object with the settings used for calls to importEvaluations.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ImportEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest),[ImportEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsResponse),[ImportEvaluationsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsOperationMetadata)>` |   
  
### importEvaluationsSettings()
    
    
    public UnaryCallSettings<ImportEvaluationsRequest,Operation> importEvaluationsSettings()

Returns the object with the settings used for calls to importEvaluations.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ImportEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ImportEvaluationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listEvaluationDatasetsSettings()
    
    
    public PagedCallSettings<ListEvaluationDatasetsRequest,ListEvaluationDatasetsResponse,EvaluationServiceClient.ListEvaluationDatasetsPagedResponse> listEvaluationDatasetsSettings()

Returns the object with the settings used for calls to listEvaluationDatasets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEvaluationDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationDatasetsRequest),[ListEvaluationDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationDatasetsResponse),[ListEvaluationDatasetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListEvaluationDatasetsPagedResponse)>` |   
  
### listEvaluationExpectationsSettings()
    
    
    public PagedCallSettings<ListEvaluationExpectationsRequest,ListEvaluationExpectationsResponse,EvaluationServiceClient.ListEvaluationExpectationsPagedResponse> listEvaluationExpectationsSettings()

Returns the object with the settings used for calls to listEvaluationExpectations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEvaluationExpectationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationExpectationsRequest),[ListEvaluationExpectationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationExpectationsResponse),[ListEvaluationExpectationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListEvaluationExpectationsPagedResponse)>` |   
  
### listEvaluationResultsSettings()
    
    
    public PagedCallSettings<ListEvaluationResultsRequest,ListEvaluationResultsResponse,EvaluationServiceClient.ListEvaluationResultsPagedResponse> listEvaluationResultsSettings()

Returns the object with the settings used for calls to listEvaluationResults.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEvaluationResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationResultsRequest),[ListEvaluationResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationResultsResponse),[ListEvaluationResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListEvaluationResultsPagedResponse)>` |   
  
### listEvaluationRunsSettings()
    
    
    public PagedCallSettings<ListEvaluationRunsRequest,ListEvaluationRunsResponse,EvaluationServiceClient.ListEvaluationRunsPagedResponse> listEvaluationRunsSettings()

Returns the object with the settings used for calls to listEvaluationRuns.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEvaluationRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationRunsRequest),[ListEvaluationRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationRunsResponse),[ListEvaluationRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListEvaluationRunsPagedResponse)>` |   
  
### listEvaluationsSettings()
    
    
    public PagedCallSettings<ListEvaluationsRequest,ListEvaluationsResponse,EvaluationServiceClient.ListEvaluationsPagedResponse> listEvaluationsSettings()

Returns the object with the settings used for calls to listEvaluations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationsRequest),[ListEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListEvaluationsResponse),[ListEvaluationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListEvaluationsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,EvaluationServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListLocationsPagedResponse)>` |   
  
### listScheduledEvaluationRunsSettings()
    
    
    public PagedCallSettings<ListScheduledEvaluationRunsRequest,ListScheduledEvaluationRunsResponse,EvaluationServiceClient.ListScheduledEvaluationRunsPagedResponse> listScheduledEvaluationRunsSettings()

Returns the object with the settings used for calls to listScheduledEvaluationRuns.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListScheduledEvaluationRunsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListScheduledEvaluationRunsRequest),[ListScheduledEvaluationRunsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ListScheduledEvaluationRunsResponse),[ListScheduledEvaluationRunsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationServiceClient.ListScheduledEvaluationRunsPagedResponse)>` |   
  
### runEvaluationOperationSettings()
    
    
    public OperationCallSettings<RunEvaluationRequest,RunEvaluationResponse,RunEvaluationOperationMetadata> runEvaluationOperationSettings()

Returns the object with the settings used for calls to runEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RunEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationRequest),[RunEvaluationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationResponse),[RunEvaluationOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationOperationMetadata)>` |   
  
### runEvaluationResultMetricsOperationSettings()
    
    
    public OperationCallSettings<RunEvaluationResultMetricsRequest,RunEvaluationResultMetricsResponse,RunEvaluationResultMetricsOperationMetadata> runEvaluationResultMetricsOperationSettings()

Returns the object with the settings used for calls to runEvaluationResultMetrics.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RunEvaluationResultMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationResultMetricsRequest),[RunEvaluationResultMetricsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationResultMetricsResponse),[RunEvaluationResultMetricsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationResultMetricsOperationMetadata)>` |   
  
### runEvaluationResultMetricsSettings()
    
    
    public UnaryCallSettings<RunEvaluationResultMetricsRequest,Operation> runEvaluationResultMetricsSettings()

Returns the object with the settings used for calls to runEvaluationResultMetrics.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RunEvaluationResultMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationResultMetricsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runEvaluationSettings()
    
    
    public UnaryCallSettings<RunEvaluationRequest,Operation> runEvaluationSettings()

Returns the object with the settings used for calls to runEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RunEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.RunEvaluationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### testPersonaVoiceSettings()
    
    
    public UnaryCallSettings<TestPersonaVoiceRequest,TestPersonaVoiceResponse> testPersonaVoiceSettings()

Returns the object with the settings used for calls to testPersonaVoice.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[TestPersonaVoiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.TestPersonaVoiceRequest),[TestPersonaVoiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.TestPersonaVoiceResponse)>` |   
  
### toBuilder()
    
    
    public EvaluationServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[EvaluationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.stub.EvaluationServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateEvaluationDatasetSettings()
    
    
    public UnaryCallSettings<UpdateEvaluationDatasetRequest,EvaluationDataset> updateEvaluationDatasetSettings()

Returns the object with the settings used for calls to updateEvaluationDataset.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEvaluationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateEvaluationDatasetRequest),[EvaluationDataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationDataset)>` |   
  
### updateEvaluationExpectationSettings()
    
    
    public UnaryCallSettings<UpdateEvaluationExpectationRequest,EvaluationExpectation> updateEvaluationExpectationSettings()

Returns the object with the settings used for calls to updateEvaluationExpectation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEvaluationExpectationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateEvaluationExpectationRequest),[EvaluationExpectation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.EvaluationExpectation)>` |   
  
### updateEvaluationSettings()
    
    
    public UnaryCallSettings<UpdateEvaluationRequest,Evaluation> updateEvaluationSettings()

Returns the object with the settings used for calls to updateEvaluation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateEvaluationRequest),[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Evaluation)>` |   
  
### updateScheduledEvaluationRunSettings()
    
    
    public UnaryCallSettings<UpdateScheduledEvaluationRunRequest,ScheduledEvaluationRun> updateScheduledEvaluationRunSettings()

Returns the object with the settings used for calls to updateScheduledEvaluationRun.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateScheduledEvaluationRunRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UpdateScheduledEvaluationRunRequest),[ScheduledEvaluationRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ScheduledEvaluationRun)>` |   
  
### uploadEvaluationAudioSettings()
    
    
    public UnaryCallSettings<UploadEvaluationAudioRequest,UploadEvaluationAudioResponse> uploadEvaluationAudioSettings()

Returns the object with the settings used for calls to uploadEvaluationAudio.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UploadEvaluationAudioRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UploadEvaluationAudioRequest),[UploadEvaluationAudioResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.UploadEvaluationAudioResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
