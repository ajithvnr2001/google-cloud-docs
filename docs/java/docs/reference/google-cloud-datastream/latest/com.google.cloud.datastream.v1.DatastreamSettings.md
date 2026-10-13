---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings
title: Class DatastreamSettings (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:36:42.485537+00:00
---

# Class DatastreamSettings (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DatastreamSettings (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 
    
    
    public class DatastreamSettings extends ClientSettings<DatastreamSettings>

Settings class to configure an instance of [DatastreamClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1alpha1.DatastreamClient).

The default instance has everything set to sensible defaults:

  * The default service address (datastream.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getConnectionProfile:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatastreamSettings.Builder datastreamSettingsBuilder = DatastreamSettings.newBuilder();
     datastreamSettingsBuilder
         .getConnectionProfileSettings()
         .setRetrySettings(
             datastreamSettingsBuilder
                 .getConnectionProfileSettings()
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
     DatastreamSettings datastreamSettings = datastreamSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createConnectionProfile:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DatastreamSettings.Builder datastreamSettingsBuilder = DatastreamSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     datastreamSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > DatastreamSettings

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

### create(DatastreamStubSettings stub)
    
    
    public static final DatastreamSettings create(DatastreamStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DatastreamStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.stub.DatastreamStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings)` |   
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
    
    
    public static DatastreamSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DatastreamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static DatastreamSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatastreamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static DatastreamSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[DatastreamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings.Builder)` |   
  
## Constructors 

### DatastreamSettings(DatastreamSettings.Builder settingsBuilder)
    
    
    protected DatastreamSettings(DatastreamSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[DatastreamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings.Builder)`  
  
  
## Methods 

### createConnectionProfileOperationSettings()
    
    
    public OperationCallSettings<CreateConnectionProfileRequest,ConnectionProfile,OperationMetadata> createConnectionProfileOperationSettings()

Returns the object with the settings used for calls to createConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createConnectionProfileSettings()
    
    
    public UnaryCallSettings<CreateConnectionProfileRequest,Operation> createConnectionProfileSettings()

Returns the object with the settings used for calls to createConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPrivateConnectionOperationSettings()
    
    
    public OperationCallSettings<CreatePrivateConnectionRequest,PrivateConnection,OperationMetadata> createPrivateConnectionOperationSettings()

Returns the object with the settings used for calls to createPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreatePrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createPrivateConnectionSettings()
    
    
    public UnaryCallSettings<CreatePrivateConnectionRequest,Operation> createPrivateConnectionSettings()

Returns the object with the settings used for calls to createPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreatePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRouteOperationSettings()
    
    
    public OperationCallSettings<CreateRouteRequest,Route,OperationMetadata> createRouteOperationSettings()

Returns the object with the settings used for calls to createRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createRouteSettings()
    
    
    public UnaryCallSettings<CreateRouteRequest,Operation> createRouteSettings()

Returns the object with the settings used for calls to createRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStreamOperationSettings()
    
    
    public OperationCallSettings<CreateStreamRequest,Stream,OperationMetadata> createStreamOperationSettings()

Returns the object with the settings used for calls to createStream.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### createStreamSettings()
    
    
    public UnaryCallSettings<CreateStreamRequest,Operation> createStreamSettings()

Returns the object with the settings used for calls to createStream.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.CreateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteConnectionProfileOperationSettings()
    
    
    public OperationCallSettings<DeleteConnectionProfileRequest,Empty,OperationMetadata> deleteConnectionProfileOperationSettings()

Returns the object with the settings used for calls to deleteConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteConnectionProfileRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteConnectionProfileSettings()
    
    
    public UnaryCallSettings<DeleteConnectionProfileRequest,Operation> deleteConnectionProfileSettings()

Returns the object with the settings used for calls to deleteConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePrivateConnectionOperationSettings()
    
    
    public OperationCallSettings<DeletePrivateConnectionRequest,Empty,OperationMetadata> deletePrivateConnectionOperationSettings()

Returns the object with the settings used for calls to deletePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeletePrivateConnectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deletePrivateConnectionSettings()
    
    
    public UnaryCallSettings<DeletePrivateConnectionRequest,Operation> deletePrivateConnectionSettings()

Returns the object with the settings used for calls to deletePrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeletePrivateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRouteOperationSettings()
    
    
    public OperationCallSettings<DeleteRouteRequest,Empty,OperationMetadata> deleteRouteOperationSettings()

Returns the object with the settings used for calls to deleteRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteRouteSettings()
    
    
    public UnaryCallSettings<DeleteRouteRequest,Operation> deleteRouteSettings()

Returns the object with the settings used for calls to deleteRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteStreamOperationSettings()
    
    
    public OperationCallSettings<DeleteStreamRequest,Empty,OperationMetadata> deleteStreamOperationSettings()

Returns the object with the settings used for calls to deleteStream.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteStreamRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### deleteStreamSettings()
    
    
    public UnaryCallSettings<DeleteStreamRequest,Operation> deleteStreamSettings()

Returns the object with the settings used for calls to deleteStream.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DeleteStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### discoverConnectionProfileSettings()
    
    
    public UnaryCallSettings<DiscoverConnectionProfileRequest,DiscoverConnectionProfileResponse> discoverConnectionProfileSettings()

Returns the object with the settings used for calls to discoverConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileRequest),[DiscoverConnectionProfileResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DiscoverConnectionProfileResponse)>` |   
  
### fetchStaticIpsSettings()
    
    
    public PagedCallSettings<FetchStaticIpsRequest,FetchStaticIpsResponse,DatastreamClient.FetchStaticIpsPagedResponse> fetchStaticIpsSettings()

Returns the object with the settings used for calls to fetchStaticIps.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FetchStaticIpsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsRequest),[FetchStaticIpsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.FetchStaticIpsResponse),[FetchStaticIpsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.FetchStaticIpsPagedResponse)>` |   
  
### getConnectionProfileSettings()
    
    
    public UnaryCallSettings<GetConnectionProfileRequest,ConnectionProfile> getConnectionProfileSettings()

Returns the object with the settings used for calls to getConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getPrivateConnectionSettings()
    
    
    public UnaryCallSettings<GetPrivateConnectionRequest,PrivateConnection> getPrivateConnectionSettings()

Returns the object with the settings used for calls to getPrivateConnection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPrivateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetPrivateConnectionRequest),[PrivateConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnection)>` |   
  
### getRouteSettings()
    
    
    public UnaryCallSettings<GetRouteRequest,Route> getRouteSettings()

Returns the object with the settings used for calls to getRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetRouteRequest),[Route](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Route)>` |   
  
### getStreamObjectSettings()
    
    
    public UnaryCallSettings<GetStreamObjectRequest,StreamObject> getStreamObjectSettings()

Returns the object with the settings used for calls to getStreamObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamObjectRequest),[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)>` |   
  
### getStreamSettings()
    
    
    public UnaryCallSettings<GetStreamRequest,Stream> getStreamSettings()

Returns the object with the settings used for calls to getStream.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GetStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream)>` |   
  
### listConnectionProfilesSettings()
    
    
    public PagedCallSettings<ListConnectionProfilesRequest,ListConnectionProfilesResponse,DatastreamClient.ListConnectionProfilesPagedResponse> listConnectionProfilesSettings()

Returns the object with the settings used for calls to listConnectionProfiles.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListConnectionProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesRequest),[ListConnectionProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListConnectionProfilesResponse),[ListConnectionProfilesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListConnectionProfilesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,DatastreamClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListLocationsPagedResponse)>` |   
  
### listPrivateConnectionsSettings()
    
    
    public PagedCallSettings<ListPrivateConnectionsRequest,ListPrivateConnectionsResponse,DatastreamClient.ListPrivateConnectionsPagedResponse> listPrivateConnectionsSettings()

Returns the object with the settings used for calls to listPrivateConnections.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPrivateConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsRequest),[ListPrivateConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListPrivateConnectionsResponse),[ListPrivateConnectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListPrivateConnectionsPagedResponse)>` |   
  
### listRoutesSettings()
    
    
    public PagedCallSettings<ListRoutesRequest,ListRoutesResponse,DatastreamClient.ListRoutesPagedResponse> listRoutesSettings()

Returns the object with the settings used for calls to listRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesRequest),[ListRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListRoutesResponse),[ListRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListRoutesPagedResponse)>` |   
  
### listStreamObjectsSettings()
    
    
    public PagedCallSettings<ListStreamObjectsRequest,ListStreamObjectsResponse,DatastreamClient.ListStreamObjectsPagedResponse> listStreamObjectsSettings()

Returns the object with the settings used for calls to listStreamObjects.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListStreamObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsRequest),[ListStreamObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamObjectsResponse),[ListStreamObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamObjectsPagedResponse)>` |   
  
### listStreamsSettings()
    
    
    public PagedCallSettings<ListStreamsRequest,ListStreamsResponse,DatastreamClient.ListStreamsPagedResponse> listStreamsSettings()

Returns the object with the settings used for calls to listStreams.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListStreamsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsRequest),[ListStreamsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ListStreamsResponse),[ListStreamsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamClient.ListStreamsPagedResponse)>` |   
  
### lookupStreamObjectSettings()
    
    
    public UnaryCallSettings<LookupStreamObjectRequest,StreamObject> lookupStreamObjectSettings()

Returns the object with the settings used for calls to lookupStreamObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[LookupStreamObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.LookupStreamObjectRequest),[StreamObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StreamObject)>` |   
  
### runStreamOperationSettings()
    
    
    public OperationCallSettings<RunStreamRequest,Stream,OperationMetadata> runStreamOperationSettings()

Returns the object with the settings used for calls to runStream.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RunStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.RunStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### runStreamSettings()
    
    
    public UnaryCallSettings<RunStreamRequest,Operation> runStreamSettings()

Returns the object with the settings used for calls to runStream.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RunStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.RunStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startBackfillJobSettings()
    
    
    public UnaryCallSettings<StartBackfillJobRequest,StartBackfillJobResponse> startBackfillJobSettings()

Returns the object with the settings used for calls to startBackfillJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobRequest),[StartBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StartBackfillJobResponse)>` |   
  
### stopBackfillJobSettings()
    
    
    public UnaryCallSettings<StopBackfillJobRequest,StopBackfillJobResponse> stopBackfillJobSettings()

Returns the object with the settings used for calls to stopBackfillJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StopBackfillJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobRequest),[StopBackfillJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StopBackfillJobResponse)>` |   
  
### toBuilder()
    
    
    public DatastreamSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[DatastreamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.DatastreamSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateConnectionProfileOperationSettings()
    
    
    public OperationCallSettings<UpdateConnectionProfileRequest,ConnectionProfile,OperationMetadata> updateConnectionProfileOperationSettings()

Returns the object with the settings used for calls to updateConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateConnectionProfileRequest),[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateConnectionProfileSettings()
    
    
    public UnaryCallSettings<UpdateConnectionProfileRequest,Operation> updateConnectionProfileSettings()

Returns the object with the settings used for calls to updateConnectionProfile.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateConnectionProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateConnectionProfileRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateStreamOperationSettings()
    
    
    public OperationCallSettings<UpdateStreamRequest,Stream,OperationMetadata> updateStreamOperationSettings()

Returns the object with the settings used for calls to updateStream.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateStreamRequest),[Stream](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.Stream),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OperationMetadata)>` |   
  
### updateStreamSettings()
    
    
    public UnaryCallSettings<UpdateStreamRequest,Operation> updateStreamSettings()

Returns the object with the settings used for calls to updateStream.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateStreamRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.UpdateStreamRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
