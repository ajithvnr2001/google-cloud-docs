---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings
title: Class EdgeNetworkSettings (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:49.555070+00:00
---

# Class EdgeNetworkSettings (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class EdgeNetworkSettings (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class EdgeNetworkSettings extends ClientSettings<EdgeNetworkSettings>

Settings class to configure an instance of [EdgeNetworkClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient).

The default instance has everything set to sensible defaults:

  * The default service address (edgenetwork.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of initializeZone:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EdgeNetworkSettings.Builder edgeNetworkSettingsBuilder = EdgeNetworkSettings.newBuilder();
     edgeNetworkSettingsBuilder
         .initializeZoneSettings()
         .setRetrySettings(
             edgeNetworkSettingsBuilder
                 .initializeZoneSettings()
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
     EdgeNetworkSettings edgeNetworkSettings = edgeNetworkSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createNetwork:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     EdgeNetworkSettings.Builder edgeNetworkSettingsBuilder = EdgeNetworkSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     edgeNetworkSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > EdgeNetworkSettings

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

### create(EdgeNetworkStubSettings stub)
    
    
    public static final EdgeNetworkSettings create(EdgeNetworkStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[EdgeNetworkStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.stub.EdgeNetworkStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings)` |   
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
    
    
    public static EdgeNetworkSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static EdgeNetworkSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static EdgeNetworkSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings.Builder)` |   
  
## Constructors 

### EdgeNetworkSettings(EdgeNetworkSettings.Builder settingsBuilder)
    
    
    protected EdgeNetworkSettings(EdgeNetworkSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[EdgeNetworkSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings.Builder)`  
  
  
## Methods 

### createInterconnectAttachmentOperationSettings()
    
    
    public OperationCallSettings<CreateInterconnectAttachmentRequest,InterconnectAttachment,OperationMetadata> createInterconnectAttachmentOperationSettings()

Returns the object with the settings used for calls to createInterconnectAttachment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest),[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createInterconnectAttachmentSettings()
    
    
    public UnaryCallSettings<CreateInterconnectAttachmentRequest,Operation> createInterconnectAttachmentSettings()

Returns the object with the settings used for calls to createInterconnectAttachment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNetworkOperationSettings()
    
    
    public OperationCallSettings<CreateNetworkRequest,Network,OperationMetadata> createNetworkOperationSettings()

Returns the object with the settings used for calls to createNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createNetworkSettings()
    
    
    public UnaryCallSettings<CreateNetworkRequest,Operation> createNetworkSettings()

Returns the object with the settings used for calls to createNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createRouterOperationSettings()
    
    
    public OperationCallSettings<CreateRouterRequest,Router,OperationMetadata> createRouterOperationSettings()

Returns the object with the settings used for calls to createRouter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createRouterSettings()
    
    
    public UnaryCallSettings<CreateRouterRequest,Operation> createRouterSettings()

Returns the object with the settings used for calls to createRouter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSubnetOperationSettings()
    
    
    public OperationCallSettings<CreateSubnetRequest,Subnet,OperationMetadata> createSubnetOperationSettings()

Returns the object with the settings used for calls to createSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### createSubnetSettings()
    
    
    public UnaryCallSettings<CreateSubnetRequest,Operation> createSubnetSettings()

Returns the object with the settings used for calls to createSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.CreateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInterconnectAttachmentOperationSettings()
    
    
    public OperationCallSettings<DeleteInterconnectAttachmentRequest,Empty,OperationMetadata> deleteInterconnectAttachmentOperationSettings()

Returns the object with the settings used for calls to deleteInterconnectAttachment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteInterconnectAttachmentSettings()
    
    
    public UnaryCallSettings<DeleteInterconnectAttachmentRequest,Operation> deleteInterconnectAttachmentSettings()

Returns the object with the settings used for calls to deleteInterconnectAttachment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteInterconnectAttachmentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNetworkOperationSettings()
    
    
    public OperationCallSettings<DeleteNetworkRequest,Empty,OperationMetadata> deleteNetworkOperationSettings()

Returns the object with the settings used for calls to deleteNetwork.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteNetworkSettings()
    
    
    public UnaryCallSettings<DeleteNetworkRequest,Operation> deleteNetworkSettings()

Returns the object with the settings used for calls to deleteNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteRouterOperationSettings()
    
    
    public OperationCallSettings<DeleteRouterRequest,Empty,OperationMetadata> deleteRouterOperationSettings()

Returns the object with the settings used for calls to deleteRouter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteRouterSettings()
    
    
    public UnaryCallSettings<DeleteRouterRequest,Operation> deleteRouterSettings()

Returns the object with the settings used for calls to deleteRouter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSubnetOperationSettings()
    
    
    public OperationCallSettings<DeleteSubnetRequest,Empty,OperationMetadata> deleteSubnetOperationSettings()

Returns the object with the settings used for calls to deleteSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### deleteSubnetSettings()
    
    
    public UnaryCallSettings<DeleteSubnetRequest,Operation> deleteSubnetSettings()

Returns the object with the settings used for calls to deleteSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DeleteSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### diagnoseInterconnectSettings()
    
    
    public UnaryCallSettings<DiagnoseInterconnectRequest,DiagnoseInterconnectResponse> diagnoseInterconnectSettings()

Returns the object with the settings used for calls to diagnoseInterconnect.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DiagnoseInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectRequest),[DiagnoseInterconnectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseInterconnectResponse)>` |   
  
### diagnoseNetworkSettings()
    
    
    public UnaryCallSettings<DiagnoseNetworkRequest,DiagnoseNetworkResponse> diagnoseNetworkSettings()

Returns the object with the settings used for calls to diagnoseNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DiagnoseNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkRequest),[DiagnoseNetworkResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseNetworkResponse)>` |   
  
### diagnoseRouterSettings()
    
    
    public UnaryCallSettings<DiagnoseRouterRequest,DiagnoseRouterResponse> diagnoseRouterSettings()

Returns the object with the settings used for calls to diagnoseRouter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DiagnoseRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterRequest),[DiagnoseRouterResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.DiagnoseRouterResponse)>` |   
  
### getInterconnectAttachmentSettings()
    
    
    public UnaryCallSettings<GetInterconnectAttachmentRequest,InterconnectAttachment> getInterconnectAttachmentSettings()

Returns the object with the settings used for calls to getInterconnectAttachment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInterconnectAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectAttachmentRequest),[InterconnectAttachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InterconnectAttachment)>` |   
  
### getInterconnectSettings()
    
    
    public UnaryCallSettings<GetInterconnectRequest,Interconnect> getInterconnectSettings()

Returns the object with the settings used for calls to getInterconnect.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetInterconnectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetInterconnectRequest),[Interconnect](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Interconnect)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getNetworkSettings()
    
    
    public UnaryCallSettings<GetNetworkRequest,Network> getNetworkSettings()

Returns the object with the settings used for calls to getNetwork.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetNetworkRequest),[Network](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Network)>` |   
  
### getRouterSettings()
    
    
    public UnaryCallSettings<GetRouterRequest,Router> getRouterSettings()

Returns the object with the settings used for calls to getRouter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router)>` |   
  
### getSubnetSettings()
    
    
    public UnaryCallSettings<GetSubnetRequest,Subnet> getSubnetSettings()

Returns the object with the settings used for calls to getSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet)>` |   
  
### getZoneSettings() (deprecated)
    
    
    public UnaryCallSettings<GetZoneRequest,Zone> getZoneSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to getZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.GetZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Zone)>` |   
  
### initializeZoneSettings()
    
    
    public UnaryCallSettings<InitializeZoneRequest,InitializeZoneResponse> initializeZoneSettings()

Returns the object with the settings used for calls to initializeZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[InitializeZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneRequest),[InitializeZoneResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.InitializeZoneResponse)>` |   
  
### listInterconnectAttachmentsSettings()
    
    
    public PagedCallSettings<ListInterconnectAttachmentsRequest,ListInterconnectAttachmentsResponse,EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse> listInterconnectAttachmentsSettings()

Returns the object with the settings used for calls to listInterconnectAttachments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsRequest),[ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectAttachmentsResponse),[ListInterconnectAttachmentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectAttachmentsPagedResponse)>` |   
  
### listInterconnectsSettings()
    
    
    public PagedCallSettings<ListInterconnectsRequest,ListInterconnectsResponse,EdgeNetworkClient.ListInterconnectsPagedResponse> listInterconnectsSettings()

Returns the object with the settings used for calls to listInterconnects.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListInterconnectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsRequest),[ListInterconnectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListInterconnectsResponse),[ListInterconnectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListInterconnectsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,EdgeNetworkClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListLocationsPagedResponse)>` |   
  
### listNetworksSettings()
    
    
    public PagedCallSettings<ListNetworksRequest,ListNetworksResponse,EdgeNetworkClient.ListNetworksPagedResponse> listNetworksSettings()

Returns the object with the settings used for calls to listNetworks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksRequest),[ListNetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListNetworksResponse),[ListNetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListNetworksPagedResponse)>` |   
  
### listRoutersSettings()
    
    
    public PagedCallSettings<ListRoutersRequest,ListRoutersResponse,EdgeNetworkClient.ListRoutersPagedResponse> listRoutersSettings()

Returns the object with the settings used for calls to listRouters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersRequest),[ListRoutersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListRoutersResponse),[ListRoutersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListRoutersPagedResponse)>` |   
  
### listSubnetsSettings()
    
    
    public PagedCallSettings<ListSubnetsRequest,ListSubnetsResponse,EdgeNetworkClient.ListSubnetsPagedResponse> listSubnetsSettings()

Returns the object with the settings used for calls to listSubnets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSubnetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsRequest),[ListSubnetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListSubnetsResponse),[ListSubnetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListSubnetsPagedResponse)>` |   
  
### listZonesSettings() (deprecated)
    
    
    public PagedCallSettings<ListZonesRequest,ListZonesResponse,EdgeNetworkClient.ListZonesPagedResponse> listZonesSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to listZones.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesRequest),[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.ListZonesResponse),[ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkClient.ListZonesPagedResponse)>` |   
  
### toBuilder()
    
    
    public EdgeNetworkSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[EdgeNetworkSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.EdgeNetworkSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateRouterOperationSettings()
    
    
    public OperationCallSettings<UpdateRouterRequest,Router,OperationMetadata> updateRouterOperationSettings()

Returns the object with the settings used for calls to updateRouter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Router),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateRouterSettings()
    
    
    public UnaryCallSettings<UpdateRouterRequest,Operation> updateRouterSettings()

Returns the object with the settings used for calls to updateRouter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubnetOperationSettings()
    
    
    public OperationCallSettings<UpdateSubnetRequest,Subnet,OperationMetadata> updateSubnetOperationSettings()

Returns the object with the settings used for calls to updateSubnet.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest),[Subnet](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.Subnet),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.OperationMetadata)>` |   
  
### updateSubnetSettings()
    
    
    public UnaryCallSettings<UpdateSubnetRequest,Operation> updateSubnetSettings()

Returns the object with the settings used for calls to updateSubnet.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSubnetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-edgenetwork/latest/com.google.cloud.edgenetwork.v1.UpdateSubnetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
