---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings
title: Class OracleDatabaseSettings (0.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:30.889797+00:00
---

# Class OracleDatabaseSettings (0.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OracleDatabaseSettings (0.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.48.0 (latest)  0.44.0  0.43.0  0.42.0  0.40.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.29.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class OracleDatabaseSettings extends ClientSettings<OracleDatabaseSettings>

Settings class to configure an instance of [OracleDatabaseClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient).

The default instance has everything set to sensible defaults:

  * The default service address (oracledatabase.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getCloudExadataInfrastructure:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OracleDatabaseSettings.Builder oracleDatabaseSettingsBuilder =
         OracleDatabaseSettings.newBuilder();
     oracleDatabaseSettingsBuilder
         .getCloudExadataInfrastructureSettings()
         .setRetrySettings(
             oracleDatabaseSettingsBuilder
                 .getCloudExadataInfrastructureSettings()
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
     OracleDatabaseSettings oracleDatabaseSettings = oracleDatabaseSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createCloudExadataInfrastructure:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OracleDatabaseSettings.Builder oracleDatabaseSettingsBuilder =
         OracleDatabaseSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     oracleDatabaseSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > OracleDatabaseSettings

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

### create(OracleDatabaseStubSettings stub)
    
    
    public static final OracleDatabaseSettings create(OracleDatabaseStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OracleDatabaseStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.stub.OracleDatabaseStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings)` |   
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
    
    
    public static OracleDatabaseSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static OracleDatabaseSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static OracleDatabaseSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings.Builder)` |   
  
## Constructors 

### OracleDatabaseSettings(OracleDatabaseSettings.Builder settingsBuilder)
    
    
    protected OracleDatabaseSettings(OracleDatabaseSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[OracleDatabaseSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings.Builder)`  
  
  
## Methods 

### configureExascaleCloudExadataInfrastructureOperationSettings()
    
    
    public OperationCallSettings<ConfigureExascaleCloudExadataInfrastructureRequest,CloudExadataInfrastructure,OperationMetadata> configureExascaleCloudExadataInfrastructureOperationSettings()

Returns the object with the settings used for calls to configureExascaleCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ConfigureExascaleCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### configureExascaleCloudExadataInfrastructureSettings()
    
    
    public UnaryCallSettings<ConfigureExascaleCloudExadataInfrastructureRequest,Operation> configureExascaleCloudExadataInfrastructureSettings()

Returns the object with the settings used for calls to configureExascaleCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ConfigureExascaleCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ConfigureExascaleCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<CreateAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> createAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to createAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<CreateAutonomousDatabaseRequest,Operation> createAutonomousDatabaseSettings()

Returns the object with the settings used for calls to createAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCloudExadataInfrastructureOperationSettings()
    
    
    public OperationCallSettings<CreateCloudExadataInfrastructureRequest,CloudExadataInfrastructure,OperationMetadata> createCloudExadataInfrastructureOperationSettings()

Returns the object with the settings used for calls to createCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudExadataInfrastructureSettings()
    
    
    public UnaryCallSettings<CreateCloudExadataInfrastructureRequest,Operation> createCloudExadataInfrastructureSettings()

Returns the object with the settings used for calls to createCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCloudVmClusterOperationSettings()
    
    
    public OperationCallSettings<CreateCloudVmClusterRequest,CloudVmCluster,OperationMetadata> createCloudVmClusterOperationSettings()

Returns the object with the settings used for calls to createCloudVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudVmClusterRequest),[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createCloudVmClusterSettings()
    
    
    public UnaryCallSettings<CreateCloudVmClusterRequest,Operation> createCloudVmClusterSettings()

Returns the object with the settings used for calls to createCloudVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateCloudVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDbSystemOperationSettings()
    
    
    public OperationCallSettings<CreateDbSystemRequest,DbSystem,OperationMetadata> createDbSystemOperationSettings()

Returns the object with the settings used for calls to createDbSystem.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateDbSystemRequest),[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createDbSystemSettings()
    
    
    public UnaryCallSettings<CreateDbSystemRequest,Operation> createDbSystemSettings()

Returns the object with the settings used for calls to createDbSystem.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateDbSystemRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExadbVmClusterOperationSettings()
    
    
    public OperationCallSettings<CreateExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> createExadbVmClusterOperationSettings()

Returns the object with the settings used for calls to createExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExadbVmClusterSettings()
    
    
    public UnaryCallSettings<CreateExadbVmClusterRequest,Operation> createExadbVmClusterSettings()

Returns the object with the settings used for calls to createExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createExascaleDbStorageVaultOperationSettings()
    
    
    public OperationCallSettings<CreateExascaleDbStorageVaultRequest,ExascaleDbStorageVault,OperationMetadata> createExascaleDbStorageVaultOperationSettings()

Returns the object with the settings used for calls to createExascaleDbStorageVault.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExascaleDbStorageVaultRequest),[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createExascaleDbStorageVaultSettings()
    
    
    public UnaryCallSettings<CreateExascaleDbStorageVaultRequest,Operation> createExascaleDbStorageVaultSettings()

Returns the object with the settings used for calls to createExascaleDbStorageVault.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateExascaleDbStorageVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateConnectionAssignmentOperationSettings()
    
    
    public OperationCallSettings<CreateGoldengateConnectionAssignmentRequest,GoldengateConnectionAssignment,OperationMetadata> createGoldengateConnectionAssignmentOperationSettings()

Returns the object with the settings used for calls to createGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionAssignmentRequest),[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionAssignmentSettings()
    
    
    public UnaryCallSettings<CreateGoldengateConnectionAssignmentRequest,Operation> createGoldengateConnectionAssignmentSettings()

Returns the object with the settings used for calls to createGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateConnectionOperationSettings()
    
    
    public OperationCallSettings<CreateGoldengateConnectionRequest,GoldengateConnection,OperationMetadata> createGoldengateConnectionOperationSettings()

Returns the object with the settings used for calls to createGoldengateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionRequest),[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateConnectionSettings()
    
    
    public UnaryCallSettings<CreateGoldengateConnectionRequest,Operation> createGoldengateConnectionSettings()

Returns the object with the settings used for calls to createGoldengateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGoldengateDeploymentOperationSettings()
    
    
    public OperationCallSettings<CreateGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> createGoldengateDeploymentOperationSettings()

Returns the object with the settings used for calls to createGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createGoldengateDeploymentSettings()
    
    
    public UnaryCallSettings<CreateGoldengateDeploymentRequest,Operation> createGoldengateDeploymentSettings()

Returns the object with the settings used for calls to createGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOdbNetworkOperationSettings()
    
    
    public OperationCallSettings<CreateOdbNetworkRequest,OdbNetwork,OperationMetadata> createOdbNetworkOperationSettings()

Returns the object with the settings used for calls to createOdbNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbNetworkRequest),[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbNetworkSettings()
    
    
    public UnaryCallSettings<CreateOdbNetworkRequest,Operation> createOdbNetworkSettings()

Returns the object with the settings used for calls to createOdbNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOdbSubnetOperationSettings()
    
    
    public OperationCallSettings<CreateOdbSubnetRequest,OdbSubnet,OperationMetadata> createOdbSubnetOperationSettings()

Returns the object with the settings used for calls to createOdbSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbSubnetRequest),[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### createOdbSubnetSettings()
    
    
    public UnaryCallSettings<CreateOdbSubnetRequest,Operation> createOdbSubnetSettings()

Returns the object with the settings used for calls to createOdbSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CreateOdbSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<DeleteAutonomousDatabaseRequest,Empty,OperationMetadata> deleteAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to deleteAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteAutonomousDatabaseRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<DeleteAutonomousDatabaseRequest,Operation> deleteAutonomousDatabaseSettings()

Returns the object with the settings used for calls to deleteAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCloudExadataInfrastructureOperationSettings()
    
    
    public OperationCallSettings<DeleteCloudExadataInfrastructureRequest,Empty,OperationMetadata> deleteCloudExadataInfrastructureOperationSettings()

Returns the object with the settings used for calls to deleteCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudExadataInfrastructureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudExadataInfrastructureSettings()
    
    
    public UnaryCallSettings<DeleteCloudExadataInfrastructureRequest,Operation> deleteCloudExadataInfrastructureSettings()

Returns the object with the settings used for calls to deleteCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudExadataInfrastructureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCloudVmClusterOperationSettings()
    
    
    public OperationCallSettings<DeleteCloudVmClusterRequest,Empty,OperationMetadata> deleteCloudVmClusterOperationSettings()

Returns the object with the settings used for calls to deleteCloudVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudVmClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteCloudVmClusterSettings()
    
    
    public UnaryCallSettings<DeleteCloudVmClusterRequest,Operation> deleteCloudVmClusterSettings()

Returns the object with the settings used for calls to deleteCloudVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteCloudVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDbSystemOperationSettings()
    
    
    public OperationCallSettings<DeleteDbSystemRequest,Empty,OperationMetadata> deleteDbSystemOperationSettings()

Returns the object with the settings used for calls to deleteDbSystem.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteDbSystemRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteDbSystemSettings()
    
    
    public UnaryCallSettings<DeleteDbSystemRequest,Operation> deleteDbSystemSettings()

Returns the object with the settings used for calls to deleteDbSystem.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteDbSystemRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExadbVmClusterOperationSettings()
    
    
    public OperationCallSettings<DeleteExadbVmClusterRequest,Empty,OperationMetadata> deleteExadbVmClusterOperationSettings()

Returns the object with the settings used for calls to deleteExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExadbVmClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExadbVmClusterSettings()
    
    
    public UnaryCallSettings<DeleteExadbVmClusterRequest,Operation> deleteExadbVmClusterSettings()

Returns the object with the settings used for calls to deleteExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExascaleDbStorageVaultOperationSettings()
    
    
    public OperationCallSettings<DeleteExascaleDbStorageVaultRequest,Empty,OperationMetadata> deleteExascaleDbStorageVaultOperationSettings()

Returns the object with the settings used for calls to deleteExascaleDbStorageVault.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExascaleDbStorageVaultRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteExascaleDbStorageVaultSettings()
    
    
    public UnaryCallSettings<DeleteExascaleDbStorageVaultRequest,Operation> deleteExascaleDbStorageVaultSettings()

Returns the object with the settings used for calls to deleteExascaleDbStorageVault.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteExascaleDbStorageVaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateConnectionAssignmentOperationSettings()
    
    
    public OperationCallSettings<DeleteGoldengateConnectionAssignmentRequest,Empty,OperationMetadata> deleteGoldengateConnectionAssignmentOperationSettings()

Returns the object with the settings used for calls to deleteGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionAssignmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionAssignmentSettings()
    
    
    public UnaryCallSettings<DeleteGoldengateConnectionAssignmentRequest,Operation> deleteGoldengateConnectionAssignmentSettings()

Returns the object with the settings used for calls to deleteGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionAssignmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateConnectionOperationSettings()
    
    
    public OperationCallSettings<DeleteGoldengateConnectionRequest,Empty,OperationMetadata> deleteGoldengateConnectionOperationSettings()

Returns the object with the settings used for calls to deleteGoldengateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateConnectionSettings()
    
    
    public UnaryCallSettings<DeleteGoldengateConnectionRequest,Operation> deleteGoldengateConnectionSettings()

Returns the object with the settings used for calls to deleteGoldengateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGoldengateDeploymentOperationSettings()
    
    
    public OperationCallSettings<DeleteGoldengateDeploymentRequest,Empty,OperationMetadata> deleteGoldengateDeploymentOperationSettings()

Returns the object with the settings used for calls to deleteGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteGoldengateDeploymentSettings()
    
    
    public UnaryCallSettings<DeleteGoldengateDeploymentRequest,Operation> deleteGoldengateDeploymentSettings()

Returns the object with the settings used for calls to deleteGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOdbNetworkOperationSettings()
    
    
    public OperationCallSettings<DeleteOdbNetworkRequest,Empty,OperationMetadata> deleteOdbNetworkOperationSettings()

Returns the object with the settings used for calls to deleteOdbNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbNetworkSettings()
    
    
    public UnaryCallSettings<DeleteOdbNetworkRequest,Operation> deleteOdbNetworkSettings()

Returns the object with the settings used for calls to deleteOdbNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOdbSubnetOperationSettings()
    
    
    public OperationCallSettings<DeleteOdbSubnetRequest,Empty,OperationMetadata> deleteOdbSubnetOperationSettings()

Returns the object with the settings used for calls to deleteOdbSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbSubnetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### deleteOdbSubnetSettings()
    
    
    public UnaryCallSettings<DeleteOdbSubnetRequest,Operation> deleteOdbSubnetSettings()

Returns the object with the settings used for calls to deleteOdbSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DeleteOdbSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### failoverAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<FailoverAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> failoverAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to failoverAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.FailoverAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### failoverAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<FailoverAutonomousDatabaseRequest,Operation> failoverAutonomousDatabaseSettings()

Returns the object with the settings used for calls to failoverAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FailoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.FailoverAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateAutonomousDatabaseWalletSettings()
    
    
    public UnaryCallSettings<GenerateAutonomousDatabaseWalletRequest,GenerateAutonomousDatabaseWalletResponse> generateAutonomousDatabaseWalletSettings()

Returns the object with the settings used for calls to generateAutonomousDatabaseWallet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GenerateAutonomousDatabaseWalletRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletRequest),[GenerateAutonomousDatabaseWalletResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GenerateAutonomousDatabaseWalletResponse)>` |   
  
### getAutonomousDatabaseRefreshableClonesSettings()
    
    
    public UnaryCallSettings<GetAutonomousDatabaseRefreshableClonesRequest,AutonomousDatabaseRefreshableClones> getAutonomousDatabaseRefreshableClonesSettings()

Returns the object with the settings used for calls to getAutonomousDatabaseRefreshableClones.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAutonomousDatabaseRefreshableClonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRefreshableClonesRequest),[AutonomousDatabaseRefreshableClones](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabaseRefreshableClones)>` |   
  
### getAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<GetAutonomousDatabaseRequest,AutonomousDatabase> getAutonomousDatabaseSettings()

Returns the object with the settings used for calls to getAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase)>` |   
  
### getCloudExadataInfrastructureSettings()
    
    
    public UnaryCallSettings<GetCloudExadataInfrastructureRequest,CloudExadataInfrastructure> getCloudExadataInfrastructureSettings()

Returns the object with the settings used for calls to getCloudExadataInfrastructure.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCloudExadataInfrastructureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudExadataInfrastructureRequest),[CloudExadataInfrastructure](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudExadataInfrastructure)>` |   
  
### getCloudVmClusterSettings()
    
    
    public UnaryCallSettings<GetCloudVmClusterRequest,CloudVmCluster> getCloudVmClusterSettings()

Returns the object with the settings used for calls to getCloudVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCloudVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetCloudVmClusterRequest),[CloudVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.CloudVmCluster)>` |   
  
### getDatabaseSettings()
    
    
    public UnaryCallSettings<GetDatabaseRequest,Database> getDatabaseSettings()

Returns the object with the settings used for calls to getDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.Database)>` |   
  
### getDbSystemSettings()
    
    
    public UnaryCallSettings<GetDbSystemRequest,DbSystem> getDbSystemSettings()

Returns the object with the settings used for calls to getDbSystem.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDbSystemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetDbSystemRequest),[DbSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.DbSystem)>` |   
  
### getExadbVmClusterSettings()
    
    
    public UnaryCallSettings<GetExadbVmClusterRequest,ExadbVmCluster> getExadbVmClusterSettings()

Returns the object with the settings used for calls to getExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster)>` |   
  
### getExascaleDbStorageVaultSettings()
    
    
    public UnaryCallSettings<GetExascaleDbStorageVaultRequest,ExascaleDbStorageVault> getExascaleDbStorageVaultSettings()

Returns the object with the settings used for calls to getExascaleDbStorageVault.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetExascaleDbStorageVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetExascaleDbStorageVaultRequest),[ExascaleDbStorageVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExascaleDbStorageVault)>` |   
  
### getGoldengateConnectionAssignmentSettings()
    
    
    public UnaryCallSettings<GetGoldengateConnectionAssignmentRequest,GoldengateConnectionAssignment> getGoldengateConnectionAssignmentSettings()

Returns the object with the settings used for calls to getGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionAssignmentRequest),[GoldengateConnectionAssignment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnectionAssignment)>` |   
  
### getGoldengateConnectionSettings()
    
    
    public UnaryCallSettings<GetGoldengateConnectionRequest,GoldengateConnection> getGoldengateConnectionSettings()

Returns the object with the settings used for calls to getGoldengateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGoldengateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateConnectionRequest),[GoldengateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateConnection)>` |   
  
### getGoldengateDeploymentSettings()
    
    
    public UnaryCallSettings<GetGoldengateDeploymentRequest,GoldengateDeployment> getGoldengateDeploymentSettings()

Returns the object with the settings used for calls to getGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOdbNetworkSettings()
    
    
    public UnaryCallSettings<GetOdbNetworkRequest,OdbNetwork> getOdbNetworkSettings()

Returns the object with the settings used for calls to getOdbNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOdbNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbNetworkRequest),[OdbNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbNetwork)>` |   
  
### getOdbSubnetSettings()
    
    
    public UnaryCallSettings<GetOdbSubnetRequest,OdbSubnet> getOdbSubnetSettings()

Returns the object with the settings used for calls to getOdbSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOdbSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetOdbSubnetRequest),[OdbSubnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OdbSubnet)>` |   
  
### getPluggableDatabaseSettings()
    
    
    public UnaryCallSettings<GetPluggableDatabaseRequest,PluggableDatabase> getPluggableDatabaseSettings()

Returns the object with the settings used for calls to getPluggableDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPluggableDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GetPluggableDatabaseRequest),[PluggableDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.PluggableDatabase)>` |   
  
### listAutonomousDatabaseBackupsSettings()
    
    
    public PagedCallSettings<ListAutonomousDatabaseBackupsRequest,ListAutonomousDatabaseBackupsResponse,OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse> listAutonomousDatabaseBackupsSettings()

Returns the object with the settings used for calls to listAutonomousDatabaseBackups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAutonomousDatabaseBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsRequest),[ListAutonomousDatabaseBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseBackupsResponse),[ListAutonomousDatabaseBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseBackupsPagedResponse)>` |   
  
### listAutonomousDatabaseCharacterSetsSettings()
    
    
    public PagedCallSettings<ListAutonomousDatabaseCharacterSetsRequest,ListAutonomousDatabaseCharacterSetsResponse,OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse> listAutonomousDatabaseCharacterSetsSettings()

Returns the object with the settings used for calls to listAutonomousDatabaseCharacterSets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAutonomousDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsRequest),[ListAutonomousDatabaseCharacterSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabaseCharacterSetsResponse),[ListAutonomousDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabaseCharacterSetsPagedResponse)>` |   
  
### listAutonomousDatabasesSettings()
    
    
    public PagedCallSettings<ListAutonomousDatabasesRequest,ListAutonomousDatabasesResponse,OracleDatabaseClient.ListAutonomousDatabasesPagedResponse> listAutonomousDatabasesSettings()

Returns the object with the settings used for calls to listAutonomousDatabases.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAutonomousDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesRequest),[ListAutonomousDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDatabasesResponse),[ListAutonomousDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDatabasesPagedResponse)>` |   
  
### listAutonomousDbVersionsSettings()
    
    
    public PagedCallSettings<ListAutonomousDbVersionsRequest,ListAutonomousDbVersionsResponse,OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse> listAutonomousDbVersionsSettings()

Returns the object with the settings used for calls to listAutonomousDbVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsRequest),[ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListAutonomousDbVersionsResponse),[ListAutonomousDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListAutonomousDbVersionsPagedResponse)>` |   
  
### listCloudExadataInfrastructuresSettings()
    
    
    public PagedCallSettings<ListCloudExadataInfrastructuresRequest,ListCloudExadataInfrastructuresResponse,OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse> listCloudExadataInfrastructuresSettings()

Returns the object with the settings used for calls to listCloudExadataInfrastructures.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCloudExadataInfrastructuresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresRequest),[ListCloudExadataInfrastructuresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudExadataInfrastructuresResponse),[ListCloudExadataInfrastructuresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudExadataInfrastructuresPagedResponse)>` |   
  
### listCloudVmClustersSettings()
    
    
    public PagedCallSettings<ListCloudVmClustersRequest,ListCloudVmClustersResponse,OracleDatabaseClient.ListCloudVmClustersPagedResponse> listCloudVmClustersSettings()

Returns the object with the settings used for calls to listCloudVmClusters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCloudVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersRequest),[ListCloudVmClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListCloudVmClustersResponse),[ListCloudVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListCloudVmClustersPagedResponse)>` |   
  
### listDatabaseCharacterSetsSettings()
    
    
    public PagedCallSettings<ListDatabaseCharacterSetsRequest,ListDatabaseCharacterSetsResponse,OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse> listDatabaseCharacterSetsSettings()

Returns the object with the settings used for calls to listDatabaseCharacterSets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDatabaseCharacterSetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsRequest),[ListDatabaseCharacterSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabaseCharacterSetsResponse),[ListDatabaseCharacterSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabaseCharacterSetsPagedResponse)>` |   
  
### listDatabasesSettings()
    
    
    public PagedCallSettings<ListDatabasesRequest,ListDatabasesResponse,OracleDatabaseClient.ListDatabasesPagedResponse> listDatabasesSettings()

Returns the object with the settings used for calls to listDatabases.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesRequest),[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDatabasesResponse),[ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDatabasesPagedResponse)>` |   
  
### listDbNodesSettings()
    
    
    public PagedCallSettings<ListDbNodesRequest,ListDbNodesResponse,OracleDatabaseClient.ListDbNodesPagedResponse> listDbNodesSettings()

Returns the object with the settings used for calls to listDbNodes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesRequest),[ListDbNodesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbNodesResponse),[ListDbNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbNodesPagedResponse)>` |   
  
### listDbServersSettings()
    
    
    public PagedCallSettings<ListDbServersRequest,ListDbServersResponse,OracleDatabaseClient.ListDbServersPagedResponse> listDbServersSettings()

Returns the object with the settings used for calls to listDbServers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersRequest),[ListDbServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbServersResponse),[ListDbServersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbServersPagedResponse)>` |   
  
### listDbSystemInitialStorageSizesSettings()
    
    
    public PagedCallSettings<ListDbSystemInitialStorageSizesRequest,ListDbSystemInitialStorageSizesResponse,OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse> listDbSystemInitialStorageSizesSettings()

Returns the object with the settings used for calls to listDbSystemInitialStorageSizes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbSystemInitialStorageSizesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesRequest),[ListDbSystemInitialStorageSizesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemInitialStorageSizesResponse),[ListDbSystemInitialStorageSizesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemInitialStorageSizesPagedResponse)>` |   
  
### listDbSystemShapesSettings()
    
    
    public PagedCallSettings<ListDbSystemShapesRequest,ListDbSystemShapesResponse,OracleDatabaseClient.ListDbSystemShapesPagedResponse> listDbSystemShapesSettings()

Returns the object with the settings used for calls to listDbSystemShapes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbSystemShapesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesRequest),[ListDbSystemShapesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemShapesResponse),[ListDbSystemShapesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemShapesPagedResponse)>` |   
  
### listDbSystemsSettings()
    
    
    public PagedCallSettings<ListDbSystemsRequest,ListDbSystemsResponse,OracleDatabaseClient.ListDbSystemsPagedResponse> listDbSystemsSettings()

Returns the object with the settings used for calls to listDbSystems.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbSystemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsRequest),[ListDbSystemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbSystemsResponse),[ListDbSystemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbSystemsPagedResponse)>` |   
  
### listDbVersionsSettings()
    
    
    public PagedCallSettings<ListDbVersionsRequest,ListDbVersionsResponse,OracleDatabaseClient.ListDbVersionsPagedResponse> listDbVersionsSettings()

Returns the object with the settings used for calls to listDbVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDbVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsRequest),[ListDbVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListDbVersionsResponse),[ListDbVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListDbVersionsPagedResponse)>` |   
  
### listEntitlementsSettings()
    
    
    public PagedCallSettings<ListEntitlementsRequest,ListEntitlementsResponse,OracleDatabaseClient.ListEntitlementsPagedResponse> listEntitlementsSettings()

Returns the object with the settings used for calls to listEntitlements.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsRequest),[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListEntitlementsResponse),[ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListEntitlementsPagedResponse)>` |   
  
### listExadbVmClustersSettings()
    
    
    public PagedCallSettings<ListExadbVmClustersRequest,ListExadbVmClustersResponse,OracleDatabaseClient.ListExadbVmClustersPagedResponse> listExadbVmClustersSettings()

Returns the object with the settings used for calls to listExadbVmClusters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListExadbVmClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersRequest),[ListExadbVmClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExadbVmClustersResponse),[ListExadbVmClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExadbVmClustersPagedResponse)>` |   
  
### listExascaleDbStorageVaultsSettings()
    
    
    public PagedCallSettings<ListExascaleDbStorageVaultsRequest,ListExascaleDbStorageVaultsResponse,OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse> listExascaleDbStorageVaultsSettings()

Returns the object with the settings used for calls to listExascaleDbStorageVaults.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListExascaleDbStorageVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsRequest),[ListExascaleDbStorageVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListExascaleDbStorageVaultsResponse),[ListExascaleDbStorageVaultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListExascaleDbStorageVaultsPagedResponse)>` |   
  
### listGiVersionsSettings()
    
    
    public PagedCallSettings<ListGiVersionsRequest,ListGiVersionsResponse,OracleDatabaseClient.ListGiVersionsPagedResponse> listGiVersionsSettings()

Returns the object with the settings used for calls to listGiVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGiVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsRequest),[ListGiVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGiVersionsResponse),[ListGiVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGiVersionsPagedResponse)>` |   
  
### listGoldengateConnectionAssignmentsSettings()
    
    
    public PagedCallSettings<ListGoldengateConnectionAssignmentsRequest,ListGoldengateConnectionAssignmentsResponse,OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse> listGoldengateConnectionAssignmentsSettings()

Returns the object with the settings used for calls to listGoldengateConnectionAssignments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateConnectionAssignmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsRequest),[ListGoldengateConnectionAssignmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionAssignmentsResponse),[ListGoldengateConnectionAssignmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionAssignmentsPagedResponse)>` |   
  
### listGoldengateConnectionTypesSettings()
    
    
    public PagedCallSettings<ListGoldengateConnectionTypesRequest,ListGoldengateConnectionTypesResponse,OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse> listGoldengateConnectionTypesSettings()

Returns the object with the settings used for calls to listGoldengateConnectionTypes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateConnectionTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesRequest),[ListGoldengateConnectionTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionTypesResponse),[ListGoldengateConnectionTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionTypesPagedResponse)>` |   
  
### listGoldengateConnectionsSettings()
    
    
    public PagedCallSettings<ListGoldengateConnectionsRequest,ListGoldengateConnectionsResponse,OracleDatabaseClient.ListGoldengateConnectionsPagedResponse> listGoldengateConnectionsSettings()

Returns the object with the settings used for calls to listGoldengateConnections.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsRequest),[ListGoldengateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateConnectionsResponse),[ListGoldengateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateConnectionsPagedResponse)>` |   
  
### listGoldengateDeploymentEnvironmentsSettings()
    
    
    public PagedCallSettings<ListGoldengateDeploymentEnvironmentsRequest,ListGoldengateDeploymentEnvironmentsResponse,OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse> listGoldengateDeploymentEnvironmentsSettings()

Returns the object with the settings used for calls to listGoldengateDeploymentEnvironments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateDeploymentEnvironmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsRequest),[ListGoldengateDeploymentEnvironmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentEnvironmentsResponse),[ListGoldengateDeploymentEnvironmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentEnvironmentsPagedResponse)>` |   
  
### listGoldengateDeploymentTypesSettings()
    
    
    public PagedCallSettings<ListGoldengateDeploymentTypesRequest,ListGoldengateDeploymentTypesResponse,OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse> listGoldengateDeploymentTypesSettings()

Returns the object with the settings used for calls to listGoldengateDeploymentTypes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateDeploymentTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesRequest),[ListGoldengateDeploymentTypesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentTypesResponse),[ListGoldengateDeploymentTypesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentTypesPagedResponse)>` |   
  
### listGoldengateDeploymentVersionsSettings()
    
    
    public PagedCallSettings<ListGoldengateDeploymentVersionsRequest,ListGoldengateDeploymentVersionsResponse,OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse> listGoldengateDeploymentVersionsSettings()

Returns the object with the settings used for calls to listGoldengateDeploymentVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateDeploymentVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsRequest),[ListGoldengateDeploymentVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentVersionsResponse),[ListGoldengateDeploymentVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentVersionsPagedResponse)>` |   
  
### listGoldengateDeploymentsSettings()
    
    
    public PagedCallSettings<ListGoldengateDeploymentsRequest,ListGoldengateDeploymentsResponse,OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse> listGoldengateDeploymentsSettings()

Returns the object with the settings used for calls to listGoldengateDeployments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGoldengateDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsRequest),[ListGoldengateDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListGoldengateDeploymentsResponse),[ListGoldengateDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListGoldengateDeploymentsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,OracleDatabaseClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListLocationsPagedResponse)>` |   
  
### listMinorVersionsSettings()
    
    
    public PagedCallSettings<ListMinorVersionsRequest,ListMinorVersionsResponse,OracleDatabaseClient.ListMinorVersionsPagedResponse> listMinorVersionsSettings()

Returns the object with the settings used for calls to listMinorVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMinorVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsRequest),[ListMinorVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListMinorVersionsResponse),[ListMinorVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListMinorVersionsPagedResponse)>` |   
  
### listOdbNetworksSettings()
    
    
    public PagedCallSettings<ListOdbNetworksRequest,ListOdbNetworksResponse,OracleDatabaseClient.ListOdbNetworksPagedResponse> listOdbNetworksSettings()

Returns the object with the settings used for calls to listOdbNetworks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOdbNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksRequest),[ListOdbNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbNetworksResponse),[ListOdbNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbNetworksPagedResponse)>` |   
  
### listOdbSubnetsSettings()
    
    
    public PagedCallSettings<ListOdbSubnetsRequest,ListOdbSubnetsResponse,OracleDatabaseClient.ListOdbSubnetsPagedResponse> listOdbSubnetsSettings()

Returns the object with the settings used for calls to listOdbSubnets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOdbSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsRequest),[ListOdbSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListOdbSubnetsResponse),[ListOdbSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListOdbSubnetsPagedResponse)>` |   
  
### listPluggableDatabasesSettings()
    
    
    public PagedCallSettings<ListPluggableDatabasesRequest,ListPluggableDatabasesResponse,OracleDatabaseClient.ListPluggableDatabasesPagedResponse> listPluggableDatabasesSettings()

Returns the object with the settings used for calls to listPluggableDatabases.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPluggableDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesRequest),[ListPluggableDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ListPluggableDatabasesResponse),[ListPluggableDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseClient.ListPluggableDatabasesPagedResponse)>` |   
  
### refreshAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<RefreshAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> refreshAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to refreshAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RefreshAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### refreshAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<RefreshAutonomousDatabaseRequest,Operation> refreshAutonomousDatabaseSettings()

Returns the object with the settings used for calls to refreshAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RefreshAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RefreshAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### removeVirtualMachineExadbVmClusterOperationSettings()
    
    
    public OperationCallSettings<RemoveVirtualMachineExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> removeVirtualMachineExadbVmClusterOperationSettings()

Returns the object with the settings used for calls to removeVirtualMachineExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RemoveVirtualMachineExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### removeVirtualMachineExadbVmClusterSettings()
    
    
    public UnaryCallSettings<RemoveVirtualMachineExadbVmClusterRequest,Operation> removeVirtualMachineExadbVmClusterSettings()

Returns the object with the settings used for calls to removeVirtualMachineExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveVirtualMachineExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RemoveVirtualMachineExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<RestartAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> restartAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to restartAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestartAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restartAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<RestartAutonomousDatabaseRequest,Operation> restartAutonomousDatabaseSettings()

Returns the object with the settings used for calls to restartAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RestartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestartAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<RestoreAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> restoreAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to restoreAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestoreAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### restoreAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<RestoreAutonomousDatabaseRequest,Operation> restoreAutonomousDatabaseSettings()

Returns the object with the settings used for calls to restoreAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RestoreAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.RestoreAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<StartAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> startAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to startAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<StartAutonomousDatabaseRequest,Operation> startAutonomousDatabaseSettings()

Returns the object with the settings used for calls to startAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startGoldengateDeploymentOperationSettings()
    
    
    public OperationCallSettings<StartGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> startGoldengateDeploymentOperationSettings()

Returns the object with the settings used for calls to startGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### startGoldengateDeploymentSettings()
    
    
    public UnaryCallSettings<StartGoldengateDeploymentRequest,Operation> startGoldengateDeploymentSettings()

Returns the object with the settings used for calls to startGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StartGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<StopAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> stopAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to stopAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<StopAutonomousDatabaseRequest,Operation> stopAutonomousDatabaseSettings()

Returns the object with the settings used for calls to stopAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopGoldengateDeploymentOperationSettings()
    
    
    public OperationCallSettings<StopGoldengateDeploymentRequest,GoldengateDeployment,OperationMetadata> stopGoldengateDeploymentOperationSettings()

Returns the object with the settings used for calls to stopGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopGoldengateDeploymentRequest),[GoldengateDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.GoldengateDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### stopGoldengateDeploymentSettings()
    
    
    public UnaryCallSettings<StopGoldengateDeploymentRequest,Operation> stopGoldengateDeploymentSettings()

Returns the object with the settings used for calls to stopGoldengateDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopGoldengateDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.StopGoldengateDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### switchoverAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<SwitchoverAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> switchoverAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to switchoverAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.SwitchoverAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### switchoverAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<SwitchoverAutonomousDatabaseRequest,Operation> switchoverAutonomousDatabaseSettings()

Returns the object with the settings used for calls to switchoverAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SwitchoverAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.SwitchoverAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### testGoldengateConnectionAssignmentSettings()
    
    
    public UnaryCallSettings<TestGoldengateConnectionAssignmentRequest,TestGoldengateConnectionAssignmentResponse> testGoldengateConnectionAssignmentSettings()

Returns the object with the settings used for calls to testGoldengateConnectionAssignment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[TestGoldengateConnectionAssignmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentRequest),[TestGoldengateConnectionAssignmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.TestGoldengateConnectionAssignmentResponse)>` |   
  
### toBuilder()
    
    
    public OracleDatabaseSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[OracleDatabaseSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OracleDatabaseSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateAutonomousDatabaseOperationSettings()
    
    
    public OperationCallSettings<UpdateAutonomousDatabaseRequest,AutonomousDatabase,OperationMetadata> updateAutonomousDatabaseOperationSettings()

Returns the object with the settings used for calls to updateAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateAutonomousDatabaseRequest),[AutonomousDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.AutonomousDatabase),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateAutonomousDatabaseSettings()
    
    
    public UnaryCallSettings<UpdateAutonomousDatabaseRequest,Operation> updateAutonomousDatabaseSettings()

Returns the object with the settings used for calls to updateAutonomousDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAutonomousDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateAutonomousDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateExadbVmClusterOperationSettings()
    
    
    public OperationCallSettings<UpdateExadbVmClusterRequest,ExadbVmCluster,OperationMetadata> updateExadbVmClusterOperationSettings()

Returns the object with the settings used for calls to updateExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateExadbVmClusterRequest),[ExadbVmCluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.ExadbVmCluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.OperationMetadata)>` |   
  
### updateExadbVmClusterSettings()
    
    
    public UnaryCallSettings<UpdateExadbVmClusterRequest,Operation> updateExadbVmClusterSettings()

Returns the object with the settings used for calls to updateExadbVmCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateExadbVmClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-oracledatabase/latest/com.google.cloud.oracledatabase.v1.UpdateExadbVmClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
