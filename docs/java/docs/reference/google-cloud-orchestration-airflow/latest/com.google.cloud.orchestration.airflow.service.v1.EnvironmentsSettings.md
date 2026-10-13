---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings
title: Class EnvironmentsSettings (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:57.659488+00:00
---

# Class EnvironmentsSettings (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EnvironmentsSettings (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0 
    
    
    public class EnvironmentsSettings extends ClientSettings<EnvironmentsSettings>

Settings class to configure an instance of [EnvironmentsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1beta1.EnvironmentsClient).

The default instance has everything set to sensible defaults:

  * The default service address (composer.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getEnvironment:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EnvironmentsSettings.Builder environmentsSettingsBuilder = EnvironmentsSettings.newBuilder();
     environmentsSettingsBuilder
         .getEnvironmentSettings()
         .setRetrySettings(
             environmentsSettingsBuilder
                 .getEnvironmentSettings()
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
     EnvironmentsSettings environmentsSettings = environmentsSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createEnvironment:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EnvironmentsSettings.Builder environmentsSettingsBuilder = EnvironmentsSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     environmentsSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > EnvironmentsSettings

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

### create(EnvironmentsStubSettings stub)
    
    
    public static final EnvironmentsSettings create(EnvironmentsStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EnvironmentsStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.stub.EnvironmentsStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings)` |   
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
    
    
    public static EnvironmentsSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static EnvironmentsSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static EnvironmentsSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings.Builder)` |   
  
## Constructors 

### EnvironmentsSettings(EnvironmentsSettings.Builder settingsBuilder)
    
    
    protected EnvironmentsSettings(EnvironmentsSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[EnvironmentsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings.Builder)`  
  
  
## Methods 

### checkUpgradeOperationSettings()
    
    
    public OperationCallSettings<CheckUpgradeRequest,CheckUpgradeResponse,OperationMetadata> checkUpgradeOperationSettings()

Returns the object with the settings used for calls to checkUpgrade.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeRequest),[CheckUpgradeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### checkUpgradeSettings()
    
    
    public UnaryCallSettings<CheckUpgradeRequest,Operation> checkUpgradeSettings()

Returns the object with the settings used for calls to checkUpgrade.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CheckUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CheckUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEnvironmentOperationSettings()
    
    
    public OperationCallSettings<CreateEnvironmentRequest,Environment,OperationMetadata> createEnvironmentOperationSettings()

Returns the object with the settings used for calls to createEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### createEnvironmentSettings()
    
    
    public UnaryCallSettings<CreateEnvironmentRequest,Operation> createEnvironmentSettings()

Returns the object with the settings used for calls to createEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createUserWorkloadsConfigMapSettings()
    
    
    public UnaryCallSettings<CreateUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> createUserWorkloadsConfigMapSettings()

Returns the object with the settings used for calls to createUserWorkloadsConfigMap.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### createUserWorkloadsSecretSettings()
    
    
    public UnaryCallSettings<CreateUserWorkloadsSecretRequest,UserWorkloadsSecret> createUserWorkloadsSecretSettings()

Returns the object with the settings used for calls to createUserWorkloadsSecret.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.CreateUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
### databaseFailoverOperationSettings()
    
    
    public OperationCallSettings<DatabaseFailoverRequest,DatabaseFailoverResponse,OperationMetadata> databaseFailoverOperationSettings()

Returns the object with the settings used for calls to databaseFailover.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverRequest),[DatabaseFailoverResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### databaseFailoverSettings()
    
    
    public UnaryCallSettings<DatabaseFailoverRequest,Operation> databaseFailoverSettings()

Returns the object with the settings used for calls to databaseFailover.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DatabaseFailoverRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DatabaseFailoverRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEnvironmentOperationSettings()
    
    
    public OperationCallSettings<DeleteEnvironmentRequest,Empty,OperationMetadata> deleteEnvironmentOperationSettings()

Returns the object with the settings used for calls to deleteEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteEnvironmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### deleteEnvironmentSettings()
    
    
    public UnaryCallSettings<DeleteEnvironmentRequest,Operation> deleteEnvironmentSettings()

Returns the object with the settings used for calls to deleteEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteUserWorkloadsConfigMapSettings()
    
    
    public UnaryCallSettings<DeleteUserWorkloadsConfigMapRequest,Empty> deleteUserWorkloadsConfigMapSettings()

Returns the object with the settings used for calls to deleteUserWorkloadsConfigMap.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsConfigMapRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserWorkloadsSecretSettings()
    
    
    public UnaryCallSettings<DeleteUserWorkloadsSecretRequest,Empty> deleteUserWorkloadsSecretSettings()

Returns the object with the settings used for calls to deleteUserWorkloadsSecret.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.DeleteUserWorkloadsSecretRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeAirflowCommandSettings()
    
    
    public UnaryCallSettings<ExecuteAirflowCommandRequest,ExecuteAirflowCommandResponse> executeAirflowCommandSettings()

Returns the object with the settings used for calls to executeAirflowCommand.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExecuteAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandRequest),[ExecuteAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ExecuteAirflowCommandResponse)>` |   
  
### fetchDatabasePropertiesSettings()
    
    
    public UnaryCallSettings<FetchDatabasePropertiesRequest,FetchDatabasePropertiesResponse> fetchDatabasePropertiesSettings()

Returns the object with the settings used for calls to fetchDatabaseProperties.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchDatabasePropertiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesRequest),[FetchDatabasePropertiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.FetchDatabasePropertiesResponse)>` |   
  
### getEnvironmentSettings()
    
    
    public UnaryCallSettings<GetEnvironmentRequest,Environment> getEnvironmentSettings()

Returns the object with the settings used for calls to getEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment)>` |   
  
### getUserWorkloadsConfigMapSettings()
    
    
    public UnaryCallSettings<GetUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> getUserWorkloadsConfigMapSettings()

Returns the object with the settings used for calls to getUserWorkloadsConfigMap.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### getUserWorkloadsSecretSettings()
    
    
    public UnaryCallSettings<GetUserWorkloadsSecretRequest,UserWorkloadsSecret> getUserWorkloadsSecretSettings()

Returns the object with the settings used for calls to getUserWorkloadsSecret.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.GetUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
### listEnvironmentsSettings()
    
    
    public PagedCallSettings<ListEnvironmentsRequest,ListEnvironmentsResponse,EnvironmentsClient.ListEnvironmentsPagedResponse> listEnvironmentsSettings()

Returns the object with the settings used for calls to listEnvironments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsRequest),[ListEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListEnvironmentsResponse),[ListEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListEnvironmentsPagedResponse)>` |   
  
### listUserWorkloadsConfigMapsSettings()
    
    
    public PagedCallSettings<ListUserWorkloadsConfigMapsRequest,ListUserWorkloadsConfigMapsResponse,EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse> listUserWorkloadsConfigMapsSettings()

Returns the object with the settings used for calls to listUserWorkloadsConfigMaps.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUserWorkloadsConfigMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsRequest),[ListUserWorkloadsConfigMapsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsConfigMapsResponse),[ListUserWorkloadsConfigMapsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsConfigMapsPagedResponse)>` |   
  
### listUserWorkloadsSecretsSettings()
    
    
    public PagedCallSettings<ListUserWorkloadsSecretsRequest,ListUserWorkloadsSecretsResponse,EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse> listUserWorkloadsSecretsSettings()

Returns the object with the settings used for calls to listUserWorkloadsSecrets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUserWorkloadsSecretsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsRequest),[ListUserWorkloadsSecretsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListUserWorkloadsSecretsResponse),[ListUserWorkloadsSecretsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListUserWorkloadsSecretsPagedResponse)>` |   
  
### listWorkloadsSettings()
    
    
    public PagedCallSettings<ListWorkloadsRequest,ListWorkloadsResponse,EnvironmentsClient.ListWorkloadsPagedResponse> listWorkloadsSettings()

Returns the object with the settings used for calls to listWorkloads.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsRequest),[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.ListWorkloadsResponse),[ListWorkloadsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsClient.ListWorkloadsPagedResponse)>` |   
  
### loadSnapshotOperationSettings()
    
    
    public OperationCallSettings<LoadSnapshotRequest,LoadSnapshotResponse,OperationMetadata> loadSnapshotOperationSettings()

Returns the object with the settings used for calls to loadSnapshot.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotRequest),[LoadSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### loadSnapshotSettings()
    
    
    public UnaryCallSettings<LoadSnapshotRequest,Operation> loadSnapshotSettings()

Returns the object with the settings used for calls to loadSnapshot.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[LoadSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.LoadSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### pollAirflowCommandSettings()
    
    
    public UnaryCallSettings<PollAirflowCommandRequest,PollAirflowCommandResponse> pollAirflowCommandSettings()

Returns the object with the settings used for calls to pollAirflowCommand.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PollAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandRequest),[PollAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.PollAirflowCommandResponse)>` |   
  
### saveSnapshotOperationSettings()
    
    
    public OperationCallSettings<SaveSnapshotRequest,SaveSnapshotResponse,OperationMetadata> saveSnapshotOperationSettings()

Returns the object with the settings used for calls to saveSnapshot.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotRequest),[SaveSnapshotResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### saveSnapshotSettings()
    
    
    public UnaryCallSettings<SaveSnapshotRequest,Operation> saveSnapshotSettings()

Returns the object with the settings used for calls to saveSnapshot.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SaveSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.SaveSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopAirflowCommandSettings()
    
    
    public UnaryCallSettings<StopAirflowCommandRequest,StopAirflowCommandResponse> stopAirflowCommandSettings()

Returns the object with the settings used for calls to stopAirflowCommand.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopAirflowCommandRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandRequest),[StopAirflowCommandResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.StopAirflowCommandResponse)>` |   
  
### toBuilder()
    
    
    public EnvironmentsSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[EnvironmentsSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.EnvironmentsSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateEnvironmentOperationSettings()
    
    
    public OperationCallSettings<UpdateEnvironmentRequest,Environment,OperationMetadata> updateEnvironmentOperationSettings()

Returns the object with the settings used for calls to updateEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateEnvironmentRequest),[Environment](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.Environment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.OperationMetadata)>` |   
  
### updateEnvironmentSettings()
    
    
    public UnaryCallSettings<UpdateEnvironmentRequest,Operation> updateEnvironmentSettings()

Returns the object with the settings used for calls to updateEnvironment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEnvironmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateEnvironmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateUserWorkloadsConfigMapSettings()
    
    
    public UnaryCallSettings<UpdateUserWorkloadsConfigMapRequest,UserWorkloadsConfigMap> updateUserWorkloadsConfigMapSettings()

Returns the object with the settings used for calls to updateUserWorkloadsConfigMap.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateUserWorkloadsConfigMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsConfigMapRequest),[UserWorkloadsConfigMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsConfigMap)>` |   
  
### updateUserWorkloadsSecretSettings()
    
    
    public UnaryCallSettings<UpdateUserWorkloadsSecretRequest,UserWorkloadsSecret> updateUserWorkloadsSecretSettings()

Returns the object with the settings used for calls to updateUserWorkloadsSecret.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateUserWorkloadsSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UpdateUserWorkloadsSecretRequest),[UserWorkloadsSecret](https://docs.cloud.google.com/java/docs/reference/google-cloud-orchestration-airflow/latest/com.google.cloud.orchestration.airflow.service.v1.UserWorkloadsSecret)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
