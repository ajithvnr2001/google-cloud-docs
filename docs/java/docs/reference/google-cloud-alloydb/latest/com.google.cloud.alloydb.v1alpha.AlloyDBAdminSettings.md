---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings
title: Class AlloyDBAdminSettings (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:37.498978+00:00
---

# Class AlloyDBAdminSettings (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AlloyDBAdminSettings (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class AlloyDBAdminSettings extends ClientSettings<AlloyDBAdminSettings>

Settings class to configure an instance of [AlloyDBAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AlloyDBAdminClient).

The default instance has everything set to sensible defaults:

  * The default service address (alloydb.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getCluster:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBAdminSettings.Builder alloyDBAdminSettingsBuilder = AlloyDBAdminSettings.newBuilder();
     alloyDBAdminSettingsBuilder
         .getClusterSettings()
         .setRetrySettings(
             alloyDBAdminSettingsBuilder
                 .getClusterSettings()
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
     AlloyDBAdminSettings alloyDBAdminSettings = alloyDBAdminSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createCluster:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AlloyDBAdminSettings.Builder alloyDBAdminSettingsBuilder = AlloyDBAdminSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     alloyDBAdminSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > AlloyDBAdminSettings

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

### create(AlloyDBAdminStubSettings stub)
    
    
    public static final AlloyDBAdminSettings create(AlloyDBAdminStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AlloyDBAdminStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.stub.AlloyDBAdminStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings)` |   
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
    
    
    public static AlloyDBAdminSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static AlloyDBAdminSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static AlloyDBAdminSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings.Builder)` |   
  
## Constructors 

### AlloyDBAdminSettings(AlloyDBAdminSettings.Builder settingsBuilder)
    
    
    protected AlloyDBAdminSettings(AlloyDBAdminSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[AlloyDBAdminSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings.Builder)`  
  
  
## Methods 

### batchCreateInstancesOperationSettings()
    
    
    public OperationCallSettings<BatchCreateInstancesRequest,BatchCreateInstancesResponse,OperationMetadata> batchCreateInstancesOperationSettings()

Returns the object with the settings used for calls to batchCreateInstances.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.BatchCreateInstancesRequest),[BatchCreateInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.BatchCreateInstancesResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### batchCreateInstancesSettings()
    
    
    public UnaryCallSettings<BatchCreateInstancesRequest,Operation> batchCreateInstancesSettings()

Returns the object with the settings used for calls to batchCreateInstances.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[BatchCreateInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.BatchCreateInstancesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBackupOperationSettings()
    
    
    public OperationCallSettings<CreateBackupRequest,Backup,OperationMetadata> createBackupOperationSettings()

Returns the object with the settings used for calls to createBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### createBackupSettings()
    
    
    public UnaryCallSettings<CreateBackupRequest,Operation> createBackupSettings()

Returns the object with the settings used for calls to createBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createClusterOperationSettings()
    
    
    public OperationCallSettings<CreateClusterRequest,Cluster,OperationMetadata> createClusterOperationSettings()

Returns the object with the settings used for calls to createCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### createClusterSettings()
    
    
    public UnaryCallSettings<CreateClusterRequest,Operation> createClusterSettings()

Returns the object with the settings used for calls to createCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDatabaseSettings()
    
    
    public UnaryCallSettings<CreateDatabaseRequest,Database> createDatabaseSettings()

Returns the object with the settings used for calls to createDatabase.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Database)>` |   
  
### createInstanceOperationSettings()
    
    
    public OperationCallSettings<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationSettings()

Returns the object with the settings used for calls to createInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### createInstanceSettings()
    
    
    public UnaryCallSettings<CreateInstanceRequest,Operation> createInstanceSettings()

Returns the object with the settings used for calls to createInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSecondaryClusterOperationSettings()
    
    
    public OperationCallSettings<CreateSecondaryClusterRequest,Cluster,OperationMetadata> createSecondaryClusterOperationSettings()

Returns the object with the settings used for calls to createSecondaryCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSecondaryClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateSecondaryClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### createSecondaryClusterSettings()
    
    
    public UnaryCallSettings<CreateSecondaryClusterRequest,Operation> createSecondaryClusterSettings()

Returns the object with the settings used for calls to createSecondaryCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSecondaryClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateSecondaryClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSecondaryInstanceOperationSettings()
    
    
    public OperationCallSettings<CreateSecondaryInstanceRequest,Instance,OperationMetadata> createSecondaryInstanceOperationSettings()

Returns the object with the settings used for calls to createSecondaryInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateSecondaryInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### createSecondaryInstanceSettings()
    
    
    public UnaryCallSettings<CreateSecondaryInstanceRequest,Operation> createSecondaryInstanceSettings()

Returns the object with the settings used for calls to createSecondaryInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSecondaryInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateSecondaryInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createUserSettings()
    
    
    public UnaryCallSettings<CreateUserRequest,User> createUserSettings()

Returns the object with the settings used for calls to createUser.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.CreateUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.User)>` |   
  
### deleteBackupOperationSettings()
    
    
    public OperationCallSettings<DeleteBackupRequest,Empty,OperationMetadata> deleteBackupOperationSettings()

Returns the object with the settings used for calls to deleteBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### deleteBackupSettings()
    
    
    public UnaryCallSettings<DeleteBackupRequest,Operation> deleteBackupSettings()

Returns the object with the settings used for calls to deleteBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteClusterOperationSettings()
    
    
    public OperationCallSettings<DeleteClusterRequest,Empty,OperationMetadata> deleteClusterOperationSettings()

Returns the object with the settings used for calls to deleteCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteClusterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### deleteClusterSettings()
    
    
    public UnaryCallSettings<DeleteClusterRequest,Operation> deleteClusterSettings()

Returns the object with the settings used for calls to deleteCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationSettings()
    
    
    public OperationCallSettings<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationSettings()

Returns the object with the settings used for calls to deleteInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### deleteInstanceSettings()
    
    
    public UnaryCallSettings<DeleteInstanceRequest,Operation> deleteInstanceSettings()

Returns the object with the settings used for calls to deleteInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteUserSettings()
    
    
    public UnaryCallSettings<DeleteUserRequest,Empty> deleteUserSettings()

Returns the object with the settings used for calls to deleteUser.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.DeleteUserRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeSqlSettings()
    
    
    public UnaryCallSettings<ExecuteSqlRequest,ExecuteSqlResponse> executeSqlSettings()

Returns the object with the settings used for calls to executeSql.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExecuteSqlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ExecuteSqlRequest),[ExecuteSqlResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ExecuteSqlResponse)>` |   
  
### exportClusterOperationSettings()
    
    
    public OperationCallSettings<ExportClusterRequest,ExportClusterResponse,OperationMetadata> exportClusterOperationSettings()

Returns the object with the settings used for calls to exportCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ExportClusterRequest),[ExportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ExportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### exportClusterSettings()
    
    
    public UnaryCallSettings<ExportClusterRequest,Operation> exportClusterSettings()

Returns the object with the settings used for calls to exportCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ExportClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### failoverInstanceOperationSettings()
    
    
    public OperationCallSettings<FailoverInstanceRequest,Instance,OperationMetadata> failoverInstanceOperationSettings()

Returns the object with the settings used for calls to failoverInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[FailoverInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.FailoverInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### failoverInstanceSettings()
    
    
    public UnaryCallSettings<FailoverInstanceRequest,Operation> failoverInstanceSettings()

Returns the object with the settings used for calls to failoverInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FailoverInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.FailoverInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### generateClientCertificateSettings()
    
    
    public UnaryCallSettings<GenerateClientCertificateRequest,GenerateClientCertificateResponse> generateClientCertificateSettings()

Returns the object with the settings used for calls to generateClientCertificate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GenerateClientCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GenerateClientCertificateRequest),[GenerateClientCertificateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GenerateClientCertificateResponse)>` |   
  
### getBackupSettings()
    
    
    public UnaryCallSettings<GetBackupRequest,Backup> getBackupSettings()

Returns the object with the settings used for calls to getBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Backup)>` |   
  
### getClusterSettings()
    
    
    public UnaryCallSettings<GetClusterRequest,Cluster> getClusterSettings()

Returns the object with the settings used for calls to getCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster)>` |   
  
### getConnectionInfoSettings()
    
    
    public UnaryCallSettings<GetConnectionInfoRequest,ConnectionInfo> getConnectionInfoSettings()

Returns the object with the settings used for calls to getConnectionInfo.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetConnectionInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GetConnectionInfoRequest),[ConnectionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ConnectionInfo)>` |   
  
### getInstanceSettings()
    
    
    public UnaryCallSettings<GetInstanceRequest,Instance> getInstanceSettings()

Returns the object with the settings used for calls to getInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getUserSettings()
    
    
    public UnaryCallSettings<GetUserRequest,User> getUserSettings()

Returns the object with the settings used for calls to getUser.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.GetUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.User)>` |   
  
### importClusterOperationSettings()
    
    
    public OperationCallSettings<ImportClusterRequest,ImportClusterResponse,OperationMetadata> importClusterOperationSettings()

Returns the object with the settings used for calls to importCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ImportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ImportClusterRequest),[ImportClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ImportClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### importClusterSettings()
    
    
    public UnaryCallSettings<ImportClusterRequest,Operation> importClusterSettings()

Returns the object with the settings used for calls to importCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ImportClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ImportClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### injectFaultOperationSettings()
    
    
    public OperationCallSettings<InjectFaultRequest,Instance,OperationMetadata> injectFaultOperationSettings()

Returns the object with the settings used for calls to injectFault.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[InjectFaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.InjectFaultRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### injectFaultSettings()
    
    
    public UnaryCallSettings<InjectFaultRequest,Operation> injectFaultSettings()

Returns the object with the settings used for calls to injectFault.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[InjectFaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.InjectFaultRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### listBackupsSettings()
    
    
    public PagedCallSettings<ListBackupsRequest,ListBackupsResponse,AlloyDBAdminClient.ListBackupsPagedResponse> listBackupsSettings()

Returns the object with the settings used for calls to listBackups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListBackupsResponse),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListBackupsPagedResponse)>` |   
  
### listClustersSettings()
    
    
    public PagedCallSettings<ListClustersRequest,ListClustersResponse,AlloyDBAdminClient.ListClustersPagedResponse> listClustersSettings()

Returns the object with the settings used for calls to listClusters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListClustersResponse),[ListClustersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListClustersPagedResponse)>` |   
  
### listDatabasesSettings()
    
    
    public PagedCallSettings<ListDatabasesRequest,ListDatabasesResponse,AlloyDBAdminClient.ListDatabasesPagedResponse> listDatabasesSettings()

Returns the object with the settings used for calls to listDatabases.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListDatabasesRequest),[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListDatabasesResponse),[ListDatabasesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListDatabasesPagedResponse)>` |   
  
### listInstancesSettings()
    
    
    public PagedCallSettings<ListInstancesRequest,ListInstancesResponse,AlloyDBAdminClient.ListInstancesPagedResponse> listInstancesSettings()

Returns the object with the settings used for calls to listInstances.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListInstancesResponse),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListInstancesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,AlloyDBAdminClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListLocationsPagedResponse)>` |   
  
### listSupportedDatabaseFlagsSettings()
    
    
    public PagedCallSettings<ListSupportedDatabaseFlagsRequest,ListSupportedDatabaseFlagsResponse,AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse> listSupportedDatabaseFlagsSettings()

Returns the object with the settings used for calls to listSupportedDatabaseFlags.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSupportedDatabaseFlagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListSupportedDatabaseFlagsRequest),[ListSupportedDatabaseFlagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListSupportedDatabaseFlagsResponse),[ListSupportedDatabaseFlagsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListSupportedDatabaseFlagsPagedResponse)>` |   
  
### listUsersSettings()
    
    
    public PagedCallSettings<ListUsersRequest,ListUsersResponse,AlloyDBAdminClient.ListUsersPagedResponse> listUsersSettings()

Returns the object with the settings used for calls to listUsers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListUsersRequest),[ListUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.ListUsersResponse),[ListUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminClient.ListUsersPagedResponse)>` |   
  
### promoteClusterOperationSettings()
    
    
    public OperationCallSettings<PromoteClusterRequest,Cluster,OperationMetadata> promoteClusterOperationSettings()

Returns the object with the settings used for calls to promoteCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[PromoteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.PromoteClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### promoteClusterSettings()
    
    
    public UnaryCallSettings<PromoteClusterRequest,Operation> promoteClusterSettings()

Returns the object with the settings used for calls to promoteCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PromoteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.PromoteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restartInstanceOperationSettings()
    
    
    public OperationCallSettings<RestartInstanceRequest,Instance,OperationMetadata> restartInstanceOperationSettings()

Returns the object with the settings used for calls to restartInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestartInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### restartInstanceSettings()
    
    
    public UnaryCallSettings<RestartInstanceRequest,Operation> restartInstanceSettings()

Returns the object with the settings used for calls to restartInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RestartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestartInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreClusterOperationSettings()
    
    
    public OperationCallSettings<RestoreClusterRequest,Cluster,OperationMetadata> restoreClusterOperationSettings()

Returns the object with the settings used for calls to restoreCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RestoreClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestoreClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### restoreClusterSettings()
    
    
    public UnaryCallSettings<RestoreClusterRequest,Operation> restoreClusterSettings()

Returns the object with the settings used for calls to restoreCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RestoreClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.RestoreClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### switchoverClusterOperationSettings()
    
    
    public OperationCallSettings<SwitchoverClusterRequest,Cluster,OperationMetadata> switchoverClusterOperationSettings()

Returns the object with the settings used for calls to switchoverCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SwitchoverClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.SwitchoverClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### switchoverClusterSettings()
    
    
    public UnaryCallSettings<SwitchoverClusterRequest,Operation> switchoverClusterSettings()

Returns the object with the settings used for calls to switchoverCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SwitchoverClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.SwitchoverClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder()
    
    
    public AlloyDBAdminSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[AlloyDBAdminSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.AlloyDBAdminSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateBackupOperationSettings()
    
    
    public OperationCallSettings<UpdateBackupRequest,Backup,OperationMetadata> updateBackupOperationSettings()

Returns the object with the settings used for calls to updateBackup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### updateBackupSettings()
    
    
    public UnaryCallSettings<UpdateBackupRequest,Operation> updateBackupSettings()

Returns the object with the settings used for calls to updateBackup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateClusterOperationSettings()
    
    
    public OperationCallSettings<UpdateClusterRequest,Cluster,OperationMetadata> updateClusterOperationSettings()

Returns the object with the settings used for calls to updateCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Cluster),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### updateClusterSettings()
    
    
    public UnaryCallSettings<UpdateClusterRequest,Operation> updateClusterSettings()

Returns the object with the settings used for calls to updateCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationSettings()
    
    
    public OperationCallSettings<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationSettings()

Returns the object with the settings used for calls to updateInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### updateInstanceSettings()
    
    
    public UnaryCallSettings<UpdateInstanceRequest,Operation> updateInstanceSettings()

Returns the object with the settings used for calls to updateInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateUserSettings()
    
    
    public UnaryCallSettings<UpdateUserRequest,User> updateUserSettings()

Returns the object with the settings used for calls to updateUser.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpdateUserRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.User)>` |   
  
### upgradeClusterOperationSettings()
    
    
    public OperationCallSettings<UpgradeClusterRequest,UpgradeClusterResponse,OperationMetadata> upgradeClusterOperationSettings()

Returns the object with the settings used for calls to upgradeCluster.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpgradeClusterRequest),[UpgradeClusterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpgradeClusterResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.OperationMetadata)>` |   
  
### upgradeClusterSettings()
    
    
    public UnaryCallSettings<UpgradeClusterRequest,Operation> upgradeClusterSettings()

Returns the object with the settings used for calls to upgradeCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpgradeClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1alpha.UpgradeClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
